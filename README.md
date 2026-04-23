# 🚀 AutoStream Chatbot

An AI-powered chatbot built using **Flask + Gemini API** that helps users with social media growth tips and captures leads.

---

## 📌 Features

* 💬 Smart chatbot with intent detection
* 🤖 AI responses using Gemini
* 📊 Lead collection (name, email, platform)
* 💾 Chat logging (CSV)
* 📈 Social media guidance (Instagram, YouTube)

---

## 🛠️ Tech Stack

* Python
* Flask
* HTML/CSS
* Google Gemini API

---

## 📂 Project Structure

```
autostream-agent/
│── app_web.py        # Main backend
│── app.py            # Optional backend
│── templates/
│    └── index.html   # Frontend UI
│── knowledge.json
│── chat_log.csv
│── leads.csv
```

---

## ▶️ How to Run

1. Install dependencies:

```
pip install flask google-generativeai
```

2. Run the app:

```
python app_web.py
```

3. Open in browser:

```
http://127.0.0.1:5000
```

---

## ⚠️ Note

* Gemini API key is required
* Current version uses deprecated `google.generativeai` (can be upgraded)

---

## 🌟 Future Improvements

* Deploy online
* Improve UI design
* Add database instead of CSV
* Use latest Gemini SDK

---

## 👩‍💻 Author

Sahana Bhairav
