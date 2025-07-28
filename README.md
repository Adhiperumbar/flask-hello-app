# 🌐 Flask Starter App by Adhi

This is a simple Flask web application created by **Adhishri P** to explore and learn the basics of web development using Flask.

---

## ✨ Features

- ✅ Home Page with welcome message
- ✅ About Page with app information
- ✅ Dynamic Routing (e.g., `/hello/Adhi`)
- ✅ HTML Templates using Jinja2 (`render_template`)
- ✅ Interlinked navigation between pages
- ✅ Basic CSS Styling via Static Folder

---

## 📁 Project Structure

flask_project/
│
├── app.py
├── templates/
│ ├── home.html
│ └── about.html
├── static/
│ └── style.css
├── .gitignore 
└── README.md 
---

## 🛠️ Setup & Running the App

### 1. Install Flask (if not already installed)
```bash
pip install flask

### 2. Run the Flask App
bash
Copy
Edit
python app.py

### 3. Open in Browser
Go to:

cpp
Copy
Edit
http://127.0.0.1:5000/

Routes Overview
Route	Description
/	Home Page
/about	About Page
/hello/<name>	Dynamic Greeting (e.g., /hello/Adhi)

Notes
HTML files are stored inside the templates/ folder.

CSS (if added) should be placed in static/ and linked in your HTML using:
html
Copy
Edit
<link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
You can improve the app further by adding forms, connecting databases, or deploying it.

## 👤 Author

Made by [Adhishri P](https://github.com/Adhiperumbar)
