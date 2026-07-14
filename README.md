# Django Todo REST API

A production-ready Todo REST API built with **Django REST Framework**, **MySQL**, and **JWT Authentication**.

This project demonstrates how to build a scalable REST API using **Clean Architecture** principles by separating business logic, data access, authentication, and exception handling into independent layers.

---

## Features

### Authentication

- User Registration
- User Login
- JWT Access & Refresh Tokens
- Custom JWT Authentication Middleware
- Protected APIs

### Todo Management

- Create Todo
- Get All Todos
- Get Single Todo
- Update Todo
- Delete Todo

### Architecture & Clean Code

- Repository Pattern
- Service Layer
- Global Exception Handling
- Custom Business Exceptions
- Layered Architecture
- Reusable JWT Service
- Django Fixtures Support

---

# Tech Stack

- Python 3
- Django
- Django REST Framework
- SimpleJWT
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
│   ├── services.py
│   ├── jwt_service.py
│   ├── authentication.py
│   ├── exceptions.py
│   ├── views.py
│   └── urls.py
│
├── todo/
│   ├── models.py
│   ├── serializers.py
│   ├── repositories.py
│   ├── services.py
│   ├── exceptions.py
│   ├── views.py
│   └── urls.py
│
├── utils/
│   └── exceptions.py
│
├── fixtures/
│   └── todos.json
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

Mac / Linux

```bash
python3 -m venv .venv
```

Windows

```bash
python -m venv .venv
```

---

## Activate Virtual Environment

Mac / Linux

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

# Database Configuration

Create a MySQL database.

```sql
CREATE DATABASE todo_db;
```

Create a `.env` file in the project root and add the following variables:

```env
DB_NAME=todo_db
DB_USER=your_mysql_username
DB_PASSWORD=your_mysql_password
DB_HOST=localhost
DB_PORT=3306
```

The project automatically loads these environment variables from the `.env` file.

---

# Apply Migrations

```bash
python manage.py makemigrations
```

```bash
python manage.py migrate
```

---

# Create Superuser

```bash
python manage.py createsuperuser
```

---

# Load Sample Data

```bash
python manage.py loaddata fixtures/todos.json
```

Export Fixtures

```bash
python manage.py dumpdata todo.Todo --indent 4 > fixtures/todos.json
```

---

# Run Server

```bash
python manage.py runserver
```

Server

```
http://127.0.0.1:8000/
```

---

# API Endpoints

## Authentication

| Method | Endpoint        | Description   |
| ------ | --------------- | ------------- |
| POST   | /Auth/register/ | Register User |
| POST   | /Auth/login/    | Login User    |

---

## Todos

> All Todo APIs require a valid JWT Access Token.

| Method | Endpoint     | Description     |
| ------ | ------------ | --------------- |
| GET    | /todos/      | Get All Todos   |
| GET    | /todos/<id>/ | Get Single Todo |
| POST   | /todos/      | Create Todo     |
| PUT    | /todos/<id>/ | Update Todo     |
| DELETE | /todos/<id>/ | Delete Todo     |

---

# Authentication

After login, the API returns

```json
{
  "message": "Logged in successfully.",
  "tokens": {
    "access": "<access_token>",
    "refresh": "<refresh_token>"
  }
}
```

Use the Access Token

```
Authorization: Bearer <access_token>
```

---

# Architecture

```
                 HTTP Request
                       │
                       ▼
                 Django APIView
                       │
                       ▼
            Authentication Layer
                       │
                       ▼
                Service Layer
                       │
                       ▼
              Repository Layer
                       │
                       ▼
                  MySQL Database
```

---

# Design Principles

- Clean Architecture
- Repository Pattern
- Service Layer Pattern
- Separation of Concerns (SoC)
- Single Responsibility Principle (SRP)
- Dependency Inversion Ready
- Reusable JWT Service
- Centralized Exception Handling

---

# Global Exception Handling

All API exceptions are handled centrally inside

```
utils/exceptions.py
```

Supported Errors

- Validation Errors
- Invalid JWT Token
- Authentication Errors
- Database Errors
- Object Not Found
- Custom Business Exceptions
- Internal Server Errors

---

# Fixtures

Load

```bash
python manage.py loaddata fixtures/todos.json
```

Export

```bash
python manage.py dumpdata todo.Todo --indent 4 > fixtures/todos.json
```

# Author

**Muhammad Zohaib**

Backend Developer

**Tech Stack**

- Python
- Django
- Django REST Framework
- MySQL
- JWT Authentication
- Clean Architecture
- Repository Pattern
- REST APIs
