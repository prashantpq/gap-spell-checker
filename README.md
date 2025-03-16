# Contextual Spell Checker using Flask & PySpellChecker

## 📌 Overview
This project implements a **Contextual Spell Checker** using **Flask** and **PySpellChecker**. It allows users to input a sentence, detects spelling mistakes, and provides corrected text while highlighting the errors.  

You can try the **live version** here:  
🔗 **[GCP Spell Checker Web App](https://gcp-spellchecker-project.uc.r.appspot.com)**  

---

## 🚀 Installation & Setup

### 1️⃣ Clone the repository:
```sh
git clone https://github.com/yourusername/gcp-spellchecker.git
cd gcp-spellchecker
```

### 2️⃣ Create & Activate a Virtual Environment:
```sh
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate     # On Windows
```

### 3️⃣ Install Required Dependencies:
```sh
pip install -r requirements.txt
```

---

## 🛠 Running the Project Locally

1️⃣ Start the Flask application:
```sh
python main.py
```
2️⃣ Open your browser and go to:
   **http://127.0.0.1:5000/**
3️⃣ Enter a sentence with spelling mistakes and check the corrected text.

---

## 📜 Features

✔ **Spell Checking:** Detects and corrects misspelled words.  
✔ **Highlighted Fixes:** Misspelled words are highlighted in yellow after correction.  
✔ **User-Friendly Interface:** Simple input field with a **Check Spelling** button.  
✔ **Copy Button:** Allows users to copy the corrected text.  
✔ **Deployed on Google Cloud:** Available at **[this link](https://gcp-spellchecker-project.uc.r.appspot.com)**  

---

## 📂 Project Structure
```
gcp-spellchecker/
├── templates/
│   ├── index.html  # Frontend UI (HTML, CSS, JS)
├── main.py         # Flask API handling spell checking
├── requirements.txt  # Project dependencies
├── app.yaml        # Google Cloud App Engine configuration
├── README.md       # Project documentation
└── config.py       # (Optional) Configuration settings
```

---

## 🛠 Technologies Used
- **Python** (Flask)
- **PySpellChecker** (for spell correction)
- **HTML, CSS, JavaScript** (Frontend)
- **Google Cloud App Engine** (Hosting)

---

## 📌 Future Improvements
🔹 Improve UI with better styling.  
🔹 Add **Grammar Checking** support.  
🔹 Implement **Sentence Context Analysis**.  

---

## 📜 License
This project is open-source and available for free use.

---

**🎉 Enjoy using your Contextual Spell Checker! 🚀🔥**  
🔗 **Try it now:** [https://gcp-spellchecker-project.uc.r.appspot.com](https://gcp-spellchecker-project.uc.r.appspot.com)
