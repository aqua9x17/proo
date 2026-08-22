# Unity Infra Pumping & Site Management System

Production-ready Django web app for motor operations, attendance, site materials, reports, and admin settings.

## Tech Stack
- Python 3.12
- Django 5.1
- SQLite
- Bootstrap 5
- Chart.js
- ReportLab (PDF)
- OpenPyXL (Excel)

## Features
- Secure authentication with role-based access (`admin`, `manager`, `operator`)
- Dashboard with operations summary
- Motor start/stop workflow with runtime logs
- Site equipment CRUD with image uploads
- Employee management and attendance check-in/check-out
- Site message notice board with priorities
- PDF/Excel export for motors, attendance, and equipment
- Audit log table
- Company settings and SQLite backup/restore

## Default Login IDs
- `admin` / `admin@123`
- `manager` / `manager@123`
- `operator` / `operator@123`

## Apps
- `accounts`
- `dashboard`
- `pumping`
- `attendance`
- `equipment`
- `reports`
- `sites`
- `audit`
- `core_settings`

## Setup
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
python manage.py migrate
python manage.py seed_demo_data
python manage.py runserver
```

Open `http://127.0.0.1:8000/accounts/login/`.

## Render Deployment
- Build Command: `pip install -r requirements.txt && python manage.py collectstatic --noinput && python manage.py migrate`
- Start Command: `gunicorn config.wsgi:application --bind 0.0.0.0:$PORT`

## Reports
Use module pages to export PDF/Excel:
- Motor logs
- Attendance records
- Equipment records

## Media & Backup
- Uploaded files are stored under `media/`
- Database backup download is available at Settings
