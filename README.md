# 🧘 Mindful Journal - دفتر اليوميات الواعي 📝

[![Python Version](https://img.shields.io/badge/python-3.9%2B-blue.svg)](https://www.python.org/) [![Framework](https://img.shields.io/badge/framework-Flask-green.svg)](https://flask.palletsprojects.com/) [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT) <!-- Add license file later -->

**رحلة نحو الهدوء الداخلي والتأمل الذاتي عبر تدوين يومي بسيط وفعال.**

هذا المشروع هو تطبيق ويب صغير مبني باستخدام Flask يهدف إلى توفير مساحة رقمية هادئة لتسجيل الأفكار والمشاعر اليومية، مع التركيز على الوعي الذاتي من خلال أسئلة توجيهية ملهمة.

<!-- ![Screenshot Placeholder](placeholder.png) -->
<!-- **ملاحظة:** استبدل `placeholder.png` بلقطة شاشة فعلية للتطبيق! -->

---

## ✨ الميزات الرئيسية

*   **📝 إضافة تدوينات سهلة:** واجهة بسيطة لتسجيل مزاجك الحالي، الإجابة على سؤال توجيهي (اختياري)، وتدوين أفكارك ومشاعرك.
*   **🤔 أسئلة توجيهية:** مجموعة من الأسئلة المتغيرة التي تساعد على التأمل وتحفيز التفكير الذاتي.
*   **😊 تتبع المزاج:** سجل حالتك المزاجية مع كل تدوينة.
*   **📖 عرض التدوينات:** استعراض جميع تدويناتك السابقة مرتبة حسب التاريخ.
*   **💾 تخزين محلي:** استخدام قاعدة بيانات SQLite لتخزين جميع بياناتك بشكل آمن على جهازك.
*   **🎨 تصميم حديث وجذاب:** واجهة مستخدم نظيفة وهادئة بصريًا باستخدام HTML و CSS حديث.

---

## 🛠️ التقنيات المستخدمة

*   **Backend:** Python 3, Flask
*   **Database:** SQLite 3
*   **Frontend:** HTML5, CSS3 (مع متغيرات CSS وتصميم متجاوب أساسي), Jinja2 (محرك القوالب)
*   **Version Control:** Git, GitHub

---

## 🚀 الإعداد والتشغيل المحلي

لتشغيل هذا التطبيق على جهازك المحلي، اتبع الخطوات التالية:

1.  **استنساخ المستودع:**
    ```bash
    git clone https://github.com/s7so/Mindful-Journaling-Mini.git
    cd Mindful-Journaling-Mini
    ```

2.  **إنشاء وتفعيل بيئة افتراضية:** (موصى به بشدة)
    ```bash
    # أنشئ بيئة افتراضية (استبدل .venv بالاسم الذي تفضله إذا أردت)
    python -m venv .venv

    # قم بتفعيل البيئة:
    # Windows (cmd.exe):
    # .venv\Scripts\activate
    # Windows (PowerShell):
    # .venv\Scripts\Activate.ps1
    # macOS / Linux:
    # source .venv/bin/activate
    ```

3.  **تثبيت المتطلبات:**
    ```bash
    pip install Flask
    # في المستقبل، يمكن إنشاء ملف requirements.txt لتثبيت كل شيء مرة واحدة
    # pip install -r requirements.txt
    ```

4.  **تشغيل التطبيق:**
    ```bash
    python main.py
    ```

5.  **افتح المتصفح:** انتقل إلى العنوان `http://127.0.0.1:5000` (أو العنوان الذي يظهر في الطرفية).

---

## 💡 كيفية الاستخدام

*   **الصفحة الرئيسية:** تعرض جميع التدوينات السابقة.
*   **إضافة تدوينة جديدة:** انقر على رابط "إضافة تدوينة جديدة" في شريط التنقل.
    *   اختر مزاجك الحالي من القائمة المنسدلة.
    *   اقرأ سؤال اليوم واجب عليه (اختياري).
    *   اكتب أفكارك ومشاعرك في المساحة المخصصة.
    *   انقر على "حفظ التدوينة". سيتم حفظ التدوينة وإعادتك إلى الصفحة الرئيسية.

---

## 🤝 المساهمة (اختياري)

إذا كنت ترغب في المساهمة في تطوير هذا المشروع، يمكنك:
*   فتح Issue للإبلاغ عن الأخطاء أو اقتراح ميزات جديدة.
*   عمل Fork للمستودع وإنشاء Pull Request بالتغييرات التي قمت بها.

---

## 📄 الترخيص (اختياري)

هذا المشروع مرخص تحت رخصة MIT. انظر ملف `LICENSE` للمزيد من التفاصيل (سيتم إضافته لاحقًا إذا لزم الأمر).
