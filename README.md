# 🎓 Flask Student Management System

A simple and user-friendly **Student Management System** built using **Python Flask, SQLite, HTML, CSS, and Jinja2**.

This mini project allows users to add students, view student records, and delete students through a clean web interface.

## 🚀 Features

* ➕ Add new students
* 👀 View all student records
* 🗑️ Delete student records
* 💾 SQLite database integration
* 🌐 Flask web application
* 🎨 Clean and responsive UI
* 🔄 Dynamic data rendering using Jinja2

## 🛠️ Technologies Used

* **Python**
* **Flask**
* **SQLite**
* **HTML5**
* **CSS3**
* **Jinja2**

## 📂 Project Structure

```text
Flask Mini Project/
│
├── app.py
├── students.db
│
├── templates/
│   ├── index.html
│   └── add_student.html
│
├── static/
│   └── style.css
│
├── .gitignore
└── README.md
```

## ⚙️ Installation & Setup

### 1. Clone the repository

```bash
git clone YOUR_REPOSITORY_URL
```

### 2. Open the project

```bash
cd "Flask Mini Project"
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

**Windows:**

```powershell
.\venv\Scripts\activate
```

### 5. Install Flask

```bash
pip install flask
```

### 6. Run the application

```bash
python app.py
```

### 7. Open in browser

Go to:

```text
http://127.0.0.1:5000
```

## 📋 How It Works

1. Open the application in your browser.
2. Click **Add Student**.
3. Enter the student's name, email, and course.
4. Submit the form.
5. Student data is stored in the SQLite database.
6. All students are displayed on the home page.
7. Use the **Delete** button to remove a student.

## 🗄️ Database

The application uses **SQLite** to store student information.

Each student record contains:

* Student ID
* Name
* Email
* Course

The database table is automatically created when the application starts.

## 🎯 Learning Objectives

This project helped in understanding:

* Flask application structure
* Flask routing
* GET and POST requests
* HTML forms
* Jinja2 templates
* SQLite database operations
* CRUD concepts
* Connecting frontend with backend
* Running a Python web application locally

## 🔮 Future Improvements

* ✏️ Edit student information
* 🔍 Search students
* 📄 Pagination
* 🎨 Bootstrap-based UI
* 🔐 User authentication
* 📊 Student dashboard
* 🌐 REST API integration

## 👨‍💻 Author

**Ayush Singh**

B.Tech CSE Student

---

⭐ If you find this project useful, consider giving the repository a star!
