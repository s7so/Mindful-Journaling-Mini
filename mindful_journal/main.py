import sqlite3
import random # Add random for prompts
from flask import Flask, render_template, request, redirect, url_for, g, flash # Add flash
from datetime import datetime # Add datetime
import markupsafe # For custom filter safety
import re # For custom filter regex

DATABASE = 'journal.db'

app = Flask(__name__)
# !!! SECURITY WARNING: Change this key immediately! Generate a strong, random key.
# In production, load this from an environment variable or config file.
# Example generation: python -c 'import secrets; print(secrets.token_hex(16))'
app.config['SECRET_KEY'] = 'your secret key' # Needs to be a unique, secret value

# --- Custom Jinja2 Filter ---

_paragraph_re = re.compile(r'(?:\r\n|\r|\n){2,}')

@app.template_filter()
def nl2br(value):
    """Converts newlines into <p> and <br> tags."""
    result = u'\n\n'.join(u'<p>%s</p>' % p.replace('\n', '<br>\n')
                          for p in _paragraph_re.split(markupsafe.escape(value)))
    return markupsafe.Markup(result)

# --- Database Functions ---

def get_db():
    """Opens a new database connection if there is none yet for the
    current application context.
    """
    if 'db' not in g:
        g.db = sqlite3.connect(DATABASE)
        g.db.row_factory = sqlite3.Row # Return rows that behave like dicts
    return g.db

@app.teardown_appcontext
def close_db(error):
    """Closes the database again at the end of the request."""
    if hasattr(g, 'db'):
        g.db.close()

def init_db():
    """Initializes the database."""
    db = get_db()
    with app.open_resource('schema.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()
    print("Initialized the database.")

@app.cli.command('initdb')
def initdb_command():
    """Creates the database tables."""
    init_db()
    print('Initialized the database.')

def create_tables():
    """Creates the database table if it doesn't exist."""
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS entries (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
            mood TEXT NOT NULL,
            prompt_question TEXT,
            prompt_answer TEXT,
            main_content TEXT NOT NULL
        );
    """)
    conn.commit()
    conn.close()
    print("Database table 'entries' checked/created.")

# --- Prompts ---
# List of potential prompts
PROMPTS = [
    "ما هو الشيء الوحيد الذي جعلك تبتسم اليوم؟",
    "صف شعورًا صعبًا واجهته مؤخرًا وكيف تعاملت معه.",
    "ما هو الشيء الذي أنت ممتن له الآن؟",
    "ما هو هدف صغير يمكنك تحقيقه غدًا؟",
    "اكتب عن لحظة شعرت فيها بالسلام أو الهدوء.",
    "ما هو الشيء الذي تعلمته عن نفسك مؤخرًا؟",
    "صف شيئًا جميلًا لاحظته اليوم في محيطك.",
]

# --- Routes ---

@app.route('/')
def index():
    """Show the main page, listing all journal entries."""
    db = get_db()
    rows = db.execute(
        'SELECT id, timestamp, mood, prompt_question, prompt_answer, main_content'
        ' FROM entries ORDER BY timestamp DESC'
    ).fetchall()

    # Convert Row objects to dictionaries and parse timestamp string to datetime object
    entries = []
    for row in rows:
        entry = dict(row) # Convert Row to mutable dict
        try:
            # SQLite default timestamp format is usually '%Y-%m-%d %H:%M:%S'
            entry['timestamp'] = datetime.strptime(entry['timestamp'], '%Y-%m-%d %H:%M:%S')
        except (ValueError, TypeError) as e:
            # Handle cases where timestamp might be NULL or in an unexpected format
            print(f"Warning: Could not parse timestamp '{entry['timestamp']}'. Error: {e}")
            # Keep the original string or set a default if parsing fails
            # For display, keeping the original string might be acceptable if parsing fails
            pass
        entries.append(entry)

    return render_template('index.html', entries=entries)

@app.route('/add', methods=('GET', 'POST'))
def add_entry():
    """Add a new journal entry."""
    prompt_question = random.choice(PROMPTS) # Select a random prompt

    if request.method == 'POST':
        mood = request.form['mood']
        # prompt_question is submitted via hidden input
        prompt_question_submitted = request.form['prompt_question']
        prompt_answer = request.form['prompt_answer']
        main_content = request.form['main_content']
        error = None

        if not mood:
            error = 'Mood is required.'
        elif not main_content:
            error = 'Main content is required.'

        if error is None:
            try:
                db = get_db()
                db.execute(
                    'INSERT INTO entries (mood, prompt_question, prompt_answer, main_content)'
                    ' VALUES (?, ?, ?, ?)',
                    (mood, prompt_question_submitted, prompt_answer, main_content)
                )
                db.commit()
            except db.IntegrityError:
                error = f"Database error occurred." # Generic error
            else:
                flash('تم حفظ التدوينة بنجاح!', 'success')
                return redirect(url_for('index'))

        if error:
            flash(error, 'error') # Consider adding error display in template

    # For GET request or if POST had an error, render the form
    return render_template('add_entry.html', prompt_question=prompt_question)


# --- Main Execution ---

if __name__ == '__main__':
    create_tables() # Ensure table exists when app starts
    app.run(debug=True) # Run in debug mode for development
