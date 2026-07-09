Link to the webapp: https://job-application-tracker-1-8gk2.onrender.com



# Job Application Tracker

A modern Django web application for tracking job applications, managing application status, storing job links, uploading CVs and cover letters, and keeping notes for each application.

This project was built as a portfolio project to practice Django, authentication, database models, CRUD operations, file uploads, search/filter functionality, Bootstrap UI, and deployment preparation.

---

## Table of Contents

- [About the Project](#about-the-project)
- [Project Goal](#project-goal)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Screenshots](#screenshots)
- [Project Structure](#project-structure)
- [Database Model](#database-model)
- [How the App Works](#how-the-app-works)
- [How to Run Locally](#how-to-run-locally)
- [Environment Setup](#environment-setup)
- [Admin Panel](#admin-panel)
- [Main Pages](#main-pages)
- [Deployment Preparation](#deployment-preparation)
- [Future Improvements](#future-improvements)
- [What I Learned](#what-i-learned)
- [Author](#author)

---

## About the Project

When applying for many jobs, it can become difficult to remember:

- Which company I applied to
- Which position I applied for
- When I applied
- What the current status is
- Whether I already uploaded or sent my CV
- Whether I wrote a cover letter
- Which applications are still waiting
- Which ones resulted in interviews
- Which ones were rejected or accepted

This web application solves that problem by giving the user one simple dashboard where all job applications can be saved and managed.

The user can log in, add a new job application, edit existing applications, delete old applications, upload documents, and filter/search through applications.

---

## Project Goal

The goal of this project is to build a practical full-stack web application using Django.

This project focuses on:

- Building a real Django project from scratch
- Creating a custom database model
- Using Django authentication
- Creating CRUD functionality
- Handling file uploads
- Building a user-friendly dashboard
- Improving the UI with Bootstrap
- Preparing the app for deployment
- Writing clean and understandable code

---

## Features

### User Authentication

The app supports user login and logout using Django's built-in authentication system.

Each user can only see their own job applications.

### Dashboard

The dashboard shows useful statistics:

- Total applications
- Applied applications
- Waiting applications
- Interview applications
- Rejected applications
- Accepted applications

### Add Job Application

Users can add a new job application with:

- Company name
- Job title
- Job link
- Location
- Application status
- Application date
- CV file
- Cover letter file
- Notes

### Edit Job Application

Users can update existing applications.

For example, the user can change the status from:

```txt
Applied
```

to:

```txt
Interview
```

or:

```txt
Rejected
```

### Delete Job Application

Users can delete applications they no longer need.

Before deleting, the app shows a confirmation page to prevent accidental deletion.

### File Uploads

Users can upload:

- CV file
- Cover letter file

These files can later be opened from the dashboard.

### Search

Users can search applications by:

- Company name
- Job title
- Location
- Notes

### Filter

Users can filter applications by status:

- Applied
- Waiting
- Interview
- Rejected
- Accepted

### Responsive UI

The app uses Bootstrap and custom CSS to create a more modern and user-friendly interface.

The interface includes:

- Navbar
- Gradient header
- Statistic cards
- Search and filter area
- Application cards
- Status badges
- Better forms
- Better login page

---

## Tech Stack

### Backend

- Python
- Django

### Frontend

- HTML
- CSS
- Bootstrap
- Bootstrap Icons

### Database

- SQLite for local development
- PostgreSQL for deployment

### Deployment Tools

- Gunicorn
- WhiteNoise
- Render-ready setup

### Version Control

- Git
- GitHub

---

## Screenshots

Add screenshots later after pushing the project.

Recommended folder:

```txt
screenshots/
```

Example screenshot links:

```md
![Dashboard Screenshot](screenshots/dashboard.png)
![Add Application Page](screenshots/add-application.png)
![Login Page](screenshots/login.png)
```

Suggested screenshots:

1. Dashboard page
2. Add application page
3. Edit application page
4. Login page
5. Admin panel

---

## Project Structure

```txt
job-application-tracker/
│
├── applications/
│   ├── migrations/
│   ├── templates/
│   │   ├── applications/
│   │   │   ├── base.html
│   │   │   ├── dashboard.html
│   │   │   ├── add_application.html
│   │   │   ├── edit_application.html
│   │   │   └── delete_application.html
│   │   │
│   │   └── registration/
│   │       └── login.html
│   │
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
│
├── config/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── media/
├── staticfiles/
├── manage.py
├── requirements.txt
├── build.sh
├── Procfile
├── .gitignore
└── README.md
```

---

## Database Model

The main model in this project is `JobApplication`.

Each job application stores information about one job.

Main fields:

| Field | Description |
|---|---|
| user | The user who owns the application |
| company_name | Name of the company |
| job_title | Title of the job |
| job_link | Link to the job post |
| location | Job location |
| status | Current status of the application |
| application_date | Date when the user applied |
| cv_file | Uploaded CV file |
| cover_letter_file | Uploaded cover letter |
| notes | Extra notes |
| created_at | Date and time when the application was created |

Status options:

```python
STATUS_CHOICES = [
    ('applied', 'Applied'),
    ('interview', 'Interview'),
    ('rejected', 'Rejected'),
    ('accepted', 'Accepted'),
    ('waiting', 'Waiting'),
]
```

---

## How the App Works

### 1. User logs in

The user opens the website and logs in using a username and password.

### 2. Dashboard loads

After login, the user is redirected to the dashboard.

The dashboard shows all applications that belong to the logged-in user.

### 3. User adds an application

The user clicks:

```txt
Add New Application
```

Then fills in the form and saves the application.

### 4. Application appears on dashboard

The new application appears as a card on the dashboard.

The card shows:

- Company name
- Job title
- Status
- Date
- Location
- Notes
- Files
- Edit button
- Delete button

### 5. User updates status

When something changes, the user can click edit and update the status.

Example:

```txt
Applied -> Interview
```

### 6. User searches or filters

The user can search by company, job title, location, or notes.

The user can also filter by application status.

---

## How to Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/halazozo/job-application-tracker.git
cd job-application-tracker
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

### 3. Activate the virtual environment

On Windows CMD:

```bash
.venv\Scripts\activate.bat
```

On Windows PowerShell:

```bash
.venv\Scripts\activate
```

On Mac/Linux:

```bash
source .venv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Run migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Create a superuser

```bash
python manage.py createsuperuser
```

### 7. Start the development server

```bash
python manage.py runserver
```

### 8. Open the app

Open this URL in the browser:

```txt
http://127.0.0.1:8000/
```

---

## Environment Setup

For local development, the app can run with SQLite.

For production, the app can use environment variables such as:

```txt
DEBUG=False
SECRET_KEY=your-secret-key
DATABASE_URL=your-database-url
```

Recommended production setup:

```txt
DEBUG=False
```

A real production project should not expose the secret key in GitHub.

---

## Admin Panel

The Django admin panel is available at:

```txt
http://127.0.0.1:8000/admin/
```

The admin panel can be used to:

- View applications
- Add applications
- Edit applications
- Delete applications
- Manage users

To access it, create a superuser:

```bash
python manage.py createsuperuser
```

---

## Main Pages

| Page | URL | Description |
|---|---|---|
| Dashboard | `/` | Shows all applications |
| Add Application | `/add/` | Add a new job application |
| Edit Application | `/edit/<id>/` | Edit an existing application |
| Delete Application | `/delete/<id>/` | Delete an application |
| Login | `/accounts/login/` | User login page |
| Logout | `/accounts/logout/` | User logout |
| Admin | `/admin/` | Django admin panel |

---

## Important Files

### `models.py`

Contains the database structure for job applications.

### `forms.py`

Contains the form used to add and edit applications.

### `views.py`

Contains the logic for:

- Dashboard
- Add application
- Edit application
- Delete application

### `urls.py`

Connects URLs to views.

### `base.html`

Main layout file used by the other templates.

### `dashboard.html`

Main user dashboard.

### `settings.py`

Main Django settings file.

---

## Deployment Preparation

This project includes files that help deploy the app online.

### `requirements.txt`

Contains all Python packages needed to run the project.

### `Procfile`

Used by hosting services to know how to start the app.

```txt
web: gunicorn config.wsgi:application
```

### `build.sh`

Used to install requirements, collect static files, and migrate the database.

```bash
#!/usr/bin/env bash

pip install -r requirements.txt
python manage.py collectstatic --no-input
python manage.py migrate
```

### WhiteNoise

WhiteNoise is used to serve static files in production.

### Gunicorn

Gunicorn is used as the production server.

---

## Deployment Steps Summary

A simple deployment process could be:

1. Push the project to GitHub
2. Create a Render account
3. Create a new Web Service
4. Connect the GitHub repository
5. Add build command:

```bash
./build.sh
```

6. Add start command:

```bash
gunicorn config.wsgi:application
```

7. Add environment variables:

```txt
DEBUG=False
SECRET_KEY=your-secret-key
DATABASE_URL=your-postgres-url
```

8. Deploy the app

---

## Git Commands Used

Initialize Git:

```bash
git init
```

Add files:

```bash
git add .
```

Commit changes:

```bash
git commit -m "Initial project commit"
```

Add remote repository:

```bash
git remote add origin https://github.com/halazozo/job-application-tracker.git
```

Push to GitHub:

```bash
git branch -M main
git push -u origin main
```

For later updates:

```bash
git add .
git commit -m "Update project"
git push
```

---

## Future Improvements

This project can be improved with more advanced features.

Possible future features:

### User Registration

Add a page where new users can create an account without using the admin panel.

### Email Reminders

Send reminders when the user should follow up with a company.

Example:

```txt
You applied to Amazon 7 days ago. Consider sending a follow-up email.
```

### AI Cover Letter Feedback

The user could upload or paste a cover letter, and the app could give suggestions.

Possible feedback:

- Make it shorter
- Make it more professional
- Improve grammar
- Match it better to the job description

### AI CV and Job Match Score

The user could paste a job description and compare it with their CV.

The app could show a match score like:

```txt
Your CV matches this job 74%.
```

### Charts

Add charts for:

- Applications per month
- Status distribution
- Acceptance rate
- Interview rate

### CSV Export

Allow users to download their applications as a CSV file.

### Dark Mode

Add a dark mode switch.

### Better File Management

Allow users to remove or replace uploaded files more easily.

### Notifications

Show notifications for:

- New application added
- Application updated
- Application deleted
- Missing CV
- Follow-up reminder

---

## What I Learned

While building this project, I practiced:

- Creating a Django project
- Creating a Django app
- Working with models
- Running migrations
- Using Django admin
- Creating forms with `ModelForm`
- Creating views
- Protecting pages with `login_required`
- Using Django templates
- Passing context from views to templates
- Creating search functionality
- Creating filter functionality
- Uploading files
- Styling pages with Bootstrap
- Using Git and GitHub
- Preparing a Django app for deployment

---

## Challenges

Some challenges during development:

### Virtual Environment

Activating the virtual environment on Windows can be different between CMD and PowerShell.

CMD:

```bash
.venv\Scripts\activate.bat
```

PowerShell:

```bash
.venv\Scripts\activate
```

### Template Paths

Django templates must be saved in the correct folder.

Correct:

```txt
applications/templates/applications/dashboard.html
```

Incorrect:

```txt
applications/template/dashboard.html
```

### Static and Media Files

The app uses media files for uploaded CVs and cover letters.

During development, media files are served using Django settings.

During production, static files need `collectstatic`.

### GitHub Remote

If the remote already exists, it can be changed with:

```bash
git remote set-url origin https://github.com/halazozo/job-application-tracker.git
```

---

## Why This Project Is Useful

This project is useful because it solves a real problem.

Many students and job seekers apply to many jobs at the same time. Without a tracker, it is easy to forget:

- Where they applied
- When they applied
- Which documents they sent
- Which companies replied
- Which applications need follow-up

This application keeps everything organized in one place.

---

## Portfolio Value

This project is good for a GitHub portfolio because it shows:

- Backend development with Django
- Database design
- Authentication
- CRUD operations
- File uploads
- Search and filtering
- Frontend styling
- Deployment preparation
- Clean project structure
- Real-world use case

This makes it stronger than a simple tutorial project because it has practical features and can be used by real users.

---

## Author

Mohamad Zouzou

GitHub: [halazozo](https://github.com/halazozo)

---

## License

This project is open source and available for learning and portfolio use.