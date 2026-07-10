# Django Todo REST API

A production-ready Todo REST API built with **Django REST Framework**, **MySQL**, and **JWT Authentication**.

The project follows clean architecture principles by using the **Repository Pattern**, **Global Exception Handling**, and **Custom User Authentication**.

---

# Features

- User Registration
- User Login (JWT Authentication)
- Protected Todo APIs
- Create Todo
- Get All Todos
- Get Single Todo
- Update Todo
- Delete Todo
- Global Exception Handling
- Repository Pattern
- MySQL Database
- Django Fixtures Support

---

# Tech Stack

- Python 3
- Django
- Django REST Framework
- Simple JWT
- MySQL
- Postman

---

# Project Structure

```text
myproject/
│
├── myproject/
│   ├── settings.py
│   ├── urls.py
│   └── ...
│
├── users/
│   ├── models.py
│   ├── serializers.py
│   ├── repositories.py
│   ├── exceptions.py
│   ├── views.py
│   └── urls.py
│
├── todo/
│   ├── models.py
│   ├── serializers.py
│   ├── repositories.py
│   ├── exceptions.py
│   ├── views.py
│   └── urls.py
│
├── utils/
│   └── exceptions.py
│
├── /todos.json
│
│
├── requirements.txt
├── README.md
└── manage.py
```

---

# Installation

## Clone Repository

```bash
git clone https://github.com/muhammadzohaib/Todos_in_Django.git

cd Todos_in_Django
```

---

## Create Virtual Environment

Mac/Linux

```bash
python3 -m venv .venv
```

Windows

```bash
python -m venv .venv
```

---

## Activate Virtual Environment

Mac/Linux

```bash
source .venv/bin/activate
```

Windows

```bash
.venv\Scripts\activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Configure MySQL

Create a database.

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

# Apply Database Migrations

```bash
python manage.py makemigrations
```

```bash
python manage.py migrate
```

---

# Load Sample Data (Fixtures)

The project contains sample data inside the `fixtures` folder.

Load it using:

```bash
python manage.py loaddata todos.json
```

To create your own fixture:

```bash
python manage.py dumpdata todo.Todo --indent 4 > todos.json
```

---

# Run Development Server

```bash
python manage.py runserver
```

Server:

```
http://127.0.0.1:8000/
```

---

# Authentication APIs

| Method | Endpoint        |
| ------ | --------------- |
| POST   | /Auth/register/ |
| POST   | /Auth/login/    |

---

# Todo APIs

> All Todo APIs require a valid JWT Access Token.

| Method | Endpoint            | Description     |
| ------ | ------------------- | --------------- |
| GET    | /api/v1/todos/      | Get All Todos   |
| GET    | /api/v1/todos/<id>/ | Get Single Todo |
| POST   | /api/v1/todos/      | Create Todo     |
| PUT    | /api/v1/todos/<id>/ | Update Todo     |
| DELETE | /api/v1/todos/<id>/ | Delete Todo     |

---

# JWT Authentication

After login, you'll receive:

```json
{
  "access": "your_access_token",
  "refresh": "your_refresh_token",
  "message" : ""
}
```

Use the Access Token in Postman.

```
Authorization

Bearer <access_token>
```

---

# Architecture

This project follows a layered architecture.

```
Request
     │
     ▼
APIView
     │
     ▼
Repository Layer
     │
     ▼
Database
```

Additional Components

- Global Exception Handler
- Custom Exceptions
- JWT Authentication
- Repository Pattern

---

# Global Exception Handling

All exceptions are handled centrally through:

```
utils/exceptions.py
```

Supported Exception Handling:

- Validation Errors
- Database Errors
- Object Not Found
- Custom Business Exceptions
- Unexpected Server Errors

---

# Fixtures

The project includes Django Fixtures for importing sample data.

Export data

```bash
python manage.py dumpdata todo.Todo --indent 4 > todos.json
```

Import data

```bash
python manage.py loaddata todos.json
```

# Author

**Muhammad Zohaib**

Backend Developer

- Python
- Django
- Django REST Framework
- MySQL
- JWT Authentication
