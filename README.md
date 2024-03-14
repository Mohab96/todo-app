# Introduction

This is RESTful API for a simple task management app. It is built using Django and Django Rest Framework. The API allows users to create, read, update and delete tasks. It also allows users to put tags on tasks and filter tasks by tags and much more.

## Features

- Create, Read, Update and Delete tasks
- Add tags to tasks
- Filter tasks by tags
- Search tasks by title
- Sort tasks by title, due date and priority
- User authentication
- User registration
- User login
- User logout
- User profile
- User password reset
- User password change
- User email verification
- User email change
- User email resend verification

## Technologies

- Python
- Django
- Django Rest Framework
- PostgreSQL
- Gunicorn
- Celery
- Swagger
- JWT
- Celery Beat

## Installation

1. Clone the repository

```bash
git clone https://github.com/Mohab96/todo-app.git
```

2. Change to the project directory

```bash
cd task-manager
```

3. Create a virtual environment

```bash
python -m venv venv
```

4. Activate the virtual environment

```bash
source venv/bin/activate
```

5. Install the project dependencies

```bash
pip install -r requirements.txt
```

6. Create a `.env` file in the root of the project and add the following environment variables

```env
SECRET_KEY=your_secret_key
DEBUG=True
ALLOWED_HOSTS=localhost
DATABASE_URL=postgres://your_db_user:your_db_password@localhost:5432/your_db_name
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_HOST_USER=your_email
EMAIL_HOST_PASSWORD=your_email_password
EMAIL_USE_TLS=True
EMAIL_USE_SSL=False
```

7. Run the migrations

```bash
python manage.py migrate
```

8. Create a superuser

```bash
python manage.py createsuperuser
```

9. Run the development server

```bash
python manage.py runserver
```

10. Open your browser and navigate to `http://localhost:8000/api/`

## API Documentation

The API documentation is available at `http://localhost:8000/swagger/`
