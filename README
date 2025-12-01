# To-Do List App (Django)

A simple but fully functional **To-Do List Web Application** built with Django.  
Each user can register, log in, and manage their own tasks securely.

---

## Features

###  Authentication
- User registration (`/register`)
- User login (`/login`)
- User logout (`/logout`)
- Redirects to the task list after login
- Prevents access to task pages when not logged in

### Task Management
- Add new tasks
- Edit/update task titles
- Mark tasks complete/incomplete
- Delete tasks
- Each task belongs to a specific user (foreign key)

**Task model includes:**
- `title`
- `complete`
- `created_at`
- `due_date`
- Overdue indicator

###  Smart Behavior
- Tasks are filtered by the logged-in user
- Default user applied to old tasks using `update()`
- URLs are named properly (`index`, `update_task`, etc.)
- Modern HTML templates styled with a clean, responsive UI

---

## ⚙️ Installation & Setup

1. **Clone the repository**
   ```bash
   git clone <your-repository-url>
   cd To_do-list-group-3

2. **Create and activate a virtual environment**

bash
python -m venv env
# Windows
env\Scripts\activate
Install dependencies

bash
pip install django
Apply migrations

bash
python manage.py makemigrations
python manage.py migrate
Start the development server

bash
python manage.py runserver
👉 Visit: http://127.0.0.1:8000/

👨‍💻 Creating a Superuser (Admin Panel)
bash
python manage.py createsuperuser
Admin login: group3

Password: 12345

Admin Panel: http://127.0.0.1:8000/admin/

📂 Project Structure
Code
To_do-list-group-3/
│── manage.py
│── to_do_list/        # Main Django app
│   ├── templates/     # HTML templates
│   ├── static/        # CSS, JS, images
│   ├── models.py      # Task model
│   ├── views.py       # App logic
│   ├── urls.py        # URL routing
│── db.sqlite3         # Database
│── requirements.txt   # Dependencies
📜 License
MIT License — All Rights Reserved © 2025

