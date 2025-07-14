# Celery Email Sender
Celery Email Sender is a full-featured Django + Celery + Vue application for sending emails via API, fully containerized with Docker and styled with Tailwind CSS.

## Tech Stack
Python 3.12.3

Django 5

Django REST Framework

Celery – asynchronous task queue

Redis – message broker

Vue 3 – SPA frontend

Tailwind CSS – styling

Docker + Docker Compose

## Features
- Send emails via REST API
- Asynchronous task processing with Celery
- Web interface for email submission
- Data validation and error handling
- Basic API tests
- Dockerized services for easy setup
- Ready for deployment

## Quick Start
- Clone the repository
```bash
git clone https://github.com/Wezzer42/celerysender.git
cd celerysender
```
- Create and configure .env
Create a .env file in the celery_email_project directory:

```ini
SECRET_KEY=your_secret_key

EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=your_email@gmail.com
EMAIL_HOST_PASSWORD=your_password
DEFAULT_FROM_EMAIL=your_email@gmail.com
```
For development or testing, you can use a dummy SECRET_KEY and local SMTP backend.

## Build and run the containers
```bash
docker-compose up --build
```
## Available Services
```Service	URL
Django API	http://localhost:8000/api/
Vue Frontend	http://localhost:8080
Flower Monitoring (if configured)	http://localhost:5555
```

## Running Tests
To run Django tests:

```bash
docker-compose run web python manage.py test
```
## Project Structure
```
.
├── celery_email_project/     # Django backend
├── vue-email-sender/         # Vue frontend
├── docker-compose.yml
└── README.md
```
## Useful Commands
Apply migrations:

```bash
docker-compose run web python manage.py migrate
```
Create a superuser:

```bash
docker-compose run web python manage.py createsuperuser
```
Build frontend assets:

```bash
cd vue-email-sender
npm install
npm run build
```
## Roadmap
- Add Flower for Celery monitoring

- Set up CI/CD

- Migrate database to PostgreSQL

- Write tests for Celery tasks

- Deploy to VPS

## Author
Azat Alibaev
GitHub
