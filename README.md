# Contextual Spell Checker using Flask & PySpellChecker

## 📌 Overview
This project implements a **Contextual Spell Checker** using **Flask** and **PySpellChecker**. It allows users to input a sentence, detects spelling mistakes, and provides corrected text while highlighting the errors. The application is deployed on **Google Cloud App Engine**, making it accessible from anywhere.

---

## 🚀 Installation & Setup

### 1️⃣ Clone the repository:
```sh
git clone https://github.com/prashantpq/gcp-spell-checker.git
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

### 4️⃣ Set Up Google Cloud Authentication:
1. **Download your service account key** from [Google Cloud IAM](https://console.cloud.google.com/iam-admin/serviceaccounts).
2. **Move the key to your project folder:**
   ```sh
   mv ~/Downloads/YOUR-KEY-FILE.json ~/Desktop/gcp-spellchecker/
   ```
3. **Set the environment variable manually:**
   ```sh
   export GOOGLE_APPLICATION_CREDENTIALS="$HOME/Desktop/gcp-spellchecker/YOUR-KEY-FILE.json"
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

## 🚀 Deploying to Google Cloud

### 1️⃣ Authenticate with Google Cloud:
```sh
gcloud auth application-default login
gcloud config set project your-gcp-project-id
```

### 2️⃣ Deploy the App to App Engine:
```sh
gcloud app deploy --no-cache
```

### 3️⃣ Open the Deployed Application:
```sh
gcloud app browse
```

---

## 📜 Features

✔ **Spell Checking:** Detects and corrects misspelled words.  
✔ **Highlighted Fixes:** Misspelled words are highlighted in yellow after correction.  
✔ **User-Friendly Interface:** Simple input field with a **Check Spelling** button.  
✔ **Copy Button:** Allows users to copy the corrected text.  
✔ **Deployed on Google Cloud:** Runs as a Flask web app on **Google Cloud App Engine**.

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
- **Google Cloud App Engine** (Deployment)

---

## 📌 Future Improvements
🔹 Improve UI with better styling.  
🔹 Add **Grammar Checking** support.  
🔹 Implement **Sentence Context Analysis**.

---

## 📜 License
MIT LICENSE.

---

**🎉 Enjoy using your Contextual Spell Checker! 🚀🔥**
