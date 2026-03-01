# Django Movie Management System

## 📌 Overview
The Django Movie Management System is a web-based application that allows users to add and view movie details.  
It provides a simple interface to store movie information such as release date, movie name, hero, heroine, and ratings.

This project demonstrates CRUD operations using Django Models, ModelForms, and Function-Based Views.

---

## 🚀 Concepts Used
- Django Models
- Django ModelForm
- Function-Based Views (FBV)
- ORM (Object Relational Mapping)
- Template Rendering
- Static Files Handling
- Admin Panel Customization
- CSRF Protection
- Bootstrap for UI Styling

---

## 📂 Project Structure
```
MOVIESPROJECT/
│
├── moviesproject/              # Main Project Folder
│   ├── __pycache__/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── static/                     # Static Files Folder
│   └── css/
│       └── style.css
│
├── templates/                  # Global Templates Folder
│   └── testapp/
│       ├── addmovie.html
│       ├── index.html
│       └── movies_list.html
│
├── testapp/                    # Django App Folder
│   ├── __pycache__/
│   ├── migrations/
│   │   └── __init__.py
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
│
├── .gitignore
├── db.sqlite3
├── manage.py
└── requirements.txt
```

--- 

## ▶️ How to Run

- Clone the Repository ```git clone https://github.com/yourusername/django-movie-management-system.git
cd django-movie-management-system```
- Install Dependencies
`
pip install -r requirements.txt
`
- Apply Migrations
`
python manage.py migrate
`
- Create Superuser (Optional for Admin Access)
`
python manage.py createsuperuser
`
- Run Development Server
`
python manage.py runserver
`
- Open in Browser
`
http://127.0.0.1:8000/
`

---

## Author & Contact

<strong>Rajat Kumar Bal</strong><br>
📧 Email: rajatkumarbal961@gmail.com<br>
🔗 <a href="https://www.linkedin.com/in/rajat-kumar-bal">LinkedIn</a>
<div align='center'>
  Made With 💖 by <strong>Rajat</strong>
</div>
