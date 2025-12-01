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

##  Installation & Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/aminmoha20/To_do-list-group-3.git
   cd To_do-list-group-3

2. **Create and activate a virtual environment**
   ```bash
   python -m venv env
   env\Scripts\activate # Windows

3. **Install dependencies**
    ```bash
    pip install django

4. **Apply migrations**
    ```bash
    python manage.py makemigrations
    python manage.py migrate

5. **Start the development server** 
    ```bash
    python manage.py runserver

6. **Open Server**
    ```bash
    Visit: http://127.0.0.1:8000/

8. **Creating a Superuser (Admin Panel)**
   ```bash
   python manage.py createsuperuser
   Admin login: group3
   Password: 12345
   Admin Panel: http://127.0.0.1:8000/admin/
   ```

##  Project Structure

```text
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
 ```
## License
MIT License — All Rights Reserved © 2025 Group 3 Meta To-do list Project

