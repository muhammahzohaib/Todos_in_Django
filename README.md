# Django Todo CRUD API

A simple Todo CRUD REST API built with **Django REST Framework** and **MySQL**.

## Features

- Create Todo
- Get All Todos
- Get Single Todo
- Update Todo
- Delete Todo

---

## Tech Stack

- Python
- Django
- Django REST Framework (DRF)
- MySQL
- Postman

---

## Project Structure

````
myproject/
│
├── myproject/                # Main configuration folder
│   ├── __init__.py
│   ├── settings.py           # Installed apps: 'users', 'todo', 'rest_framework'
│   └── urls.py               # Routes to: api/v1/auth/ and api/v1/todos/
│
├── users/                    # NEW: Dedicated Auth App
│   ├── models.py             # Custom User Model
|   |─- repositories.py       # Data isolation layer 
│   ├── serializers.py.       # RegisterSerializer, LoginSerializer
│   ├── views.py              # RegisterAPIView, LoginAPIView
│   └── urls.py               # Routes for login/ and register/
│
└── todo/                     # Existing Core Feature App
    ├── models.py             # Todo Model
    ├── repositories.py       # TodoRepository (Data isolation layer)
    ├── serializers.py        # TodoSerializer
    ├── views.py              # TodoAPIView (Locked down with IsAuthenticated)
    └── urls.py               # Routes for CRUD tasks

---

## Installation

### Clone the repository

```bash
git clone https://github.com/muhammahzohaib/Todos_in_Django
````

### Create a virtual environment

```bash
python -m venv .venv
```

### Activate the virtual environment

Mac/Linux

```bash
source .venv/bin/activate
```

Windows

```bash
.venv\Scripts\activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

---

## Configure MySQL

Create a MySQL database.

Example:

```sql
CREATE DATABASE todo_db;
```

Update your `settings.py`.

```python
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "todo_db",
        "USER": "root",
        "PASSWORD": "your_password",
        "HOST": "localhost",
        "PORT": "3306",
    }
}
```

---

## Apply Migrations

```bash
python manage.py makemigrations
```

```bash
python manage.py migrate
```

---

## Run Server

```bash
python manage.py runserver
```

Server runs at:

```
http://127.0.0.1:8000/
```

---

## API Endpoints

| Method | Endpoint            | Description     |
| ------ | ------------------- | --------------- |
| POST   | `/api/create/`      | Create Todo     |
| GET    | `/api/list/`        | Get All Todos   |
| GET    | `/api/detail/<id>/` | Get Single Todo |
| PUT    | `/api/update/<id>/` | Update Todo     |
| DELETE | `/api/delete/<id>/` | Delete Todo     |

---

## Example Request

### POST

```
POST /api/create/
```

Body

```json
{
  "title": "Learn Django",
  "description": "Practice CRUD APIs",
  "completed": false,
  "priority": "HIGH",
  "due_date": "2026-07-10"
}
```

---

## Author

**Muhammad Zohaib**

Backend Developer | Django | Django REST Framework | Python
