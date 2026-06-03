# Smart Todo Dashboard

## Project Overview

Smart Todo Dashboard is a Full Stack Task Management Application built using Django REST Framework and JavaScript.

The project demonstrates frontend-backend integration through REST APIs using Fetch API and Async/Await.

Users can register, login, create tasks, update tasks, delete tasks, search tasks, filter tasks, and view task statistics through a responsive dashboard.

---

<img width="1147" height="643" alt="Screenshot 2026-06-04 020020" src="https://github.com/user-attachments/assets/1f0af532-6d6b-4fe9-9335-f92cf5051f5b" />


## Project Objective

The objective of this project is to demonstrate:

* API Integration
* Asynchronous JavaScript
* Frontend and Backend Communication
* RESTful API Design
* JWT Authentication
* Dynamic DOM Manipulation
* CRUD Operations
* Dashboard Analytics
* Secure Coding Practices

---

## Technologies Used

### Backend

* Python
* Django
* Django REST Framework
* Simple JWT Authentication
* SQLite Database

### Frontend

* HTML5
* CSS3
* Bootstrap 5
* JavaScript (ES6)

### API Communication

* Fetch API
* Async/Await

---

## Features

### User Authentication

* User Registration
* User Login
* JWT Token Authentication
* Token Refresh

---
<img width="939" height="574" alt="Screenshot 2026-06-04 020237" src="https://github.com/user-attachments/assets/d6878849-dfef-4223-aa9e-bb16e5882586" />


### Task Management

* Create Task
* View Tasks
* Update Task
* Delete Task
* Mark Task Complete
* Change Task Status

---

<img width="611" height="315" alt="Screenshot 2026-06-04 020306" src="https://github.com/user-attachments/assets/3f303c39-01db-4998-b345-f20e559b0c52" />


<img width="1109" height="317" alt="Screenshot 2026-06-04 020254" src="https://github.com/user-attachments/assets/1aa0a0b9-df8e-4df1-85fa-eefb8f08336e" />

### Dashboard Analytics

* Total Tasks Count
* Completed Tasks Count
* Pending Tasks Count

---

### Search & Filtering

* Search Tasks
* Filter By Priority
* Filter By Status

---

## Database Models

### User Model

```python
class User(AbstractUser):
    full_name
    email
    profile_image
    phone_number
```

Features:

* Custom User Model
* Email Based Authentication
* Profile Image Support

---

### Task Model

```python
class Task(models.Model):
    title
    description
    priority
    status
    due_date
    completed
    user
```

Features:

* Task Ownership
* Priority Management
* Status Tracking
* Completion Tracking

---

## REST API Endpoints

### Authentication

```http
POST   /api/register/
POST   /api/login/
POST   /token/refresh/
```

---

### Tasks

```http
GET      /api/tasks/
POST     /api/tasks/

GET      /api/tasks/<id>/
PUT      /api/tasks/<id>/
DELETE   /api/tasks/<id>/
```

---

### Dashboard

```http
GET   /api/dashboard/
```

---

### Search

```http
GET   /api/search/?q=taskname
```

---

### Filters

```http
GET   /api/filter/priority/
GET   /api/filter/status/
```

---

## Frontend Pages

### Home Page

Landing page for application.

### Register Page

New user registration.

### Login Page

User authentication.

### Dashboard Page

Displays:

* Task List
* Statistics
* Add Task Modal
* Search & Filters

---

## API Integration Using Fetch

Example:

```javascript
async function loadTasks() {

    const response = await fetch(
        "/api/tasks/"
    );

    const data = await response.json();

    displayTasks(data);
}
```

Benefits:

* Faster UI Updates
* No Page Refresh
* Better User Experience

---

## Async/Await Implementation

The project uses Async/Await for asynchronous operations.

Example:

```javascript
async function createTask() {

    const response = await fetch(
        "/api/tasks/",
        {
            method: "POST"
        }
    );

    const data = await response.json();
}
```

Advantages:

* Cleaner Code
* Easy Error Handling
* Better Readability

---

## Input → Process → Output Flow

### Input (Sensory Layer)

Frontend sends requests using:

* Fetch API
* Forms
* Buttons

Example:

```text
User Clicks Add Task
```

---

### Process (Cognitive Layer)

Django Backend:

* Validates Data
* Authenticates User
* Executes ORM Queries
* Processes Requests

Example:

```python
Task.objects.create(...)
```

---

### Output (Motor Layer)

Frontend dynamically updates:

* Task List
* Dashboard Counts
* Status Changes

Without page refresh.

---

## HTTP Method Matrix

| Method | Purpose        |
| ------ | -------------- |
| GET    | Retrieve Tasks |
| POST   | Create Task    |
| PUT    | Update Task    |
| PATCH  | Partial Update |
| DELETE | Delete Task    |

---

## Security Features

### JWT Authentication

Secure API access using access and refresh tokens.

---

### Django ORM Protection

Database operations use ORM instead of raw SQL.

Example:

```python
Task.objects.filter(user=request.user)
```

Benefits:

* Parameterized Queries
* SQL Injection Protection

---

### XSS Prevention

User-generated content is inserted using:

```javascript
textContent
```

instead of:

```javascript
innerHTML
```

This prevents Cross-Site Scripting (XSS) attacks.

---

### Error Handling

Implemented using:

```javascript
try {
    // API Call
}
catch(error) {
    console.log(error);
}
finally {
    // Cleanup
}
```

Benefits:

* Better Reliability
* Improved User Experience

---

## Project Structure

```text
smart_todo_dashboard/

│
├── accounts/
│   ├── models.py
│   ├── views.py
│   ├── serializers.py
│   ├── urls.py
│
├── templates/
│   ├── home.html
│   ├── login.html
│   ├── register.html
│   ├── dashboard.html
│
├── static/
│   ├── css/
│   │   └── style.css
│   ├── js/
│   │   └── app.js
│
├── media/
│
├── db.sqlite3
├── manage.py
└── README.md
```

---

## Testing

The application was tested using:

* Django REST Framework Browser API
* Thunder Client
* Browser Developer Tools

---

## Learning Outcomes

Through this project, I learned:

* Full Stack Development
* API Integration
* Fetch API
* Async/Await
* JWT Authentication
* CRUD Operations
* Dynamic DOM Manipulation
* Dashboard Development
* Django REST Framework
* Database Integration
* Search and Filtering
* Error Handling
* Security Best Practices
* RESTful API Design

---

## Future Enhancements

* Email Verification
* Password Reset
* Task Categories
* File Attachments
* Notifications
* Dark Mode
* Task Sharing
* Deployment on AWS / Render

---

## Author

Mithra Tarvin

Diploma in Computer Science Engineering

GitHub: https://github.com/Nikhat2325
