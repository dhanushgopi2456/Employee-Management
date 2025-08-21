# 🧑‍💼 Employee Management System

A web-based **Employee Management System** built with **Django** that allows administrators to manage employee records efficiently.  
This project demonstrates CRUD operations, Django models, templates, and database integration.

---

## 🚀 Features
- Add, update, delete, and view employee records  
- Django Admin Panel integration for quick management  
- SQLite database support (can be extended to MySQL/PostgreSQL)  
- Modular structure with `emp_app` for business logic and `emp_mgt` for project settings  

---

## 🛠️ Tech Stack
- **Backend**: Django (Python)  
- **Database**: SQLite (default)  
- **Frontend**: Django Templates (HTML, CSS, Bootstrap)  

---

## 📂 Project Structure
Employee-Management/
│
├── emp_app/                  # Main application folder
│   ├── migrations/           # Database migration files
│   ├── templates/            # HTML templates for UI
│   ├── __init__.py           # Package initializer
│   ├── admin.py              # Django admin configurations
│   ├── apps.py               # App configuration
│   ├── models.py             # Database models (Employee, etc.)
│   ├── tests.py              # Unit tests
│   ├── urls.py               # App-level URL routing
│   └── views.py              # View functions / logic
│
├── emp_mgt/                  # Project settings folder
│   ├── __init__.py
│   ├── asgi.py               # ASGI entry point
│   ├── settings.py           # Project settings
│   ├── urls.py               # Project-level URL routing
│   └── wsgi.py               # WSGI entry point
│
├── db.sqlite3                # SQLite database file
├── manage.py                 # Django project management script
└── README.md                 # (To be created)

Employee-Management/
├── emp_app/ # Application logic
├── emp_mgt/ # Project settings
├── db.sqlite3 # Database
└── manage.py # Management script


---

## ⚡ Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/dhanushgopi2456/Employee-Management.git
cd Employee-Management

2. Install dependencies
pip install -r requirements.txt

3. Run migrations
python manage.py migrate

4. Start the server
python manage.py runserver


Now open http://127.0.0.1:8000/
 in your browser 🚀
