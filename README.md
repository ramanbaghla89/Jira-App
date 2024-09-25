# Jira APP Project Management Platform

This project is a Jira-APP project management platform built with Django 3.2 and Django Rest Framework (DRF). It provides REST APIs for user authentication, project management, task handling, and comment management.

## Features

- **Authentication**: Register, login, and update user profiles.
- **Projects**: Create, update, delete, and list projects.
- **Tasks**: Create, update, delete, and list tasks within projects.
- **Comments**: Add, edit, delete, and list comments on tasks.

## Requirements

- Python 3.8 or later
- Django 3.2
- Django Rest Framework
- PostgreSQL (optional, for database)

## Create a Virtual Environment
- python -m venv venv
- source venv/bin/activate 

## Install Dependencies
- requrement.txt

## Configure the Database
- Update DATABASES in settings.py if using PostgreSQL or another database.

## Apply Migrations
- python manage.py migrate
- python manage.py createsuperuser # for admin page

## Run the Development Server
- Run the Development Server
- http://127.0.0.1:8000


# API Endpoints
## Django Admin 
-   http://127.0.0.1:8000/admin/

## Authentication
- Register: POST /register/
- Logout: POST /logout/
- Login: POST /login/
## User Profile
- Get Profile: GET /profile/
- Update Profile: PUT|PATCH /profile/ 
## Projects
- Create Project: POST api/projects/
- Get Projects: GET api/projects/
- Get Project Details: GET api/projects/{id}/
- Update Project: PUT|PATCH api/projects/{id}/
- Delete Project: DELETE api/projects/{id}/
## Tasks
- Create Task: POST api/tasks/
- Get Tasks: GET api/tasks/
- Get Task Details: GET api/tasks/{id}/
- Update Task: PUT|PATCH api/tasks/{id}/
- Delete Task: DELETE api/tasks/{id}/
## Comments
- Add Comment: POST api/comments/
- Get Comments: GET api/comments/
- Get Comment Details: GET api/comments/{id}/
- Update Comment: PUT|PATCH api/comments/{id}/
- Delete Comment: DELETE api/comments/{id}/

### NOTE: To access all the Api you need to register first on register Api then use that JWT token
