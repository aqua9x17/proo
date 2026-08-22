# proo
Build a 100% complete, production-ready Unity Infra Pumping & Site Management System using Python 3.12 + Django + SQLite + Bootstrap 5 + JavaScript + Chart.js + ReportLab + OpenPyXL. It must be a fully working web application (not a demo or prototype), with a professional responsive UI for desktop and mobile.

Login & User Roles

Create secure authentication with password hashing and role-based access.

Default Login IDs

- Admin → "admin" / "admin@123"
- Manager → "manager" / "manager@123"
- Operator → "operator" / "operator@123"

Roles must have different permissions, logout, change password, reset password, and session security.

Dashboard

Modern dashboard with live date/time and summary cards:

- Total Motors
- Running Motors
- Stopped Motors
- Today's Running Hours
- Employees Present Today
- Extra Equipment Count
- Important Site Messages

Include charts for daily/monthly motor usage and attendance.

Motor/Pumping Module

Manage 4 motors (future-ready for unlimited motors).
Each motor must have:

- Start Motor / Stop Motor buttons.
- Running/Stopped/Maintenance status.
- Start Time, Stop Time.
- Live running timer while ON.
- Automatic runtime calculation (hours/minutes/seconds).
- Prevent duplicate START or STOP.
- Save operator name and timestamp.

Motor History & Reports

Store every motor session with filters:

- Date, Date Range, Motor, Site, Operator.
  Generate:
- Daily Report.
- Monthly Report.
- Custom Date Report.
  Export to PDF and Excel with Unity Infra logo and company details.

Site Equipment Module

Separate menu for extra materials lying on site (as requested by client).
Categories:

- Extra Motor
- Light
- Pipe
- Cable
- Starter
- Valve
- Pump
- Tools
- Other Material

Fields:

- Item Name
- Quantity
- Site
- Location
- Condition
- Status
- Remarks
- Photo Upload

Full CRUD, search, filter, PDF & Excel export.

Attendance System

Separate Attendance menu with:

- Employee Management.
- Check In / Check Out.
- Working Hours calculation.
- Present / Absent / Leave / Half Day.
- Daily & Monthly Attendance Reports.
- PDF & Excel export.

Site Messages / Notice Board

Create notice board for Unity Infra.
Fields:

- Title
- Message
- Site
- Priority (Normal, Important, Urgent)
- Expiry Date
- Created By

Important messages should appear on Dashboard.

Admin Panel

Admin can:

- Add/Edit/Delete Users.
- Manage Employees.
- Manage Motors.
- Manage Equipment.
- View Audit Logs.
- Backup & Restore SQLite Database.
- Company Settings (Logo, Address, Contact, Report Footer).

Database

Use normalized SQLite tables:
Users, Sites, Motors, MotorLogs, Employees, Attendance, Equipment, SiteMessages, AuditLogs, CompanySettings.

UI Design

- Blue + White + Orange industrial theme.
- Left sidebar navigation.
- Top navbar with profile.
- Responsive Bootstrap tables.
- Search, Filters, Pagination.
- Toast notifications and confirmation dialogs.

Project Structure

Create a complete Django project with apps:
"accounts", "dashboard", "pumping", "attendance", "equipment", "reports", "sites", "audit", "settings".

Include:

- "requirements.txt"
- ".env.example"
- "README.md"
- Seed demo data command.
- Migrations.
- Static files.
- Media upload support.

Final Requirement

Generate the entire working project with all Python files, Django models, views, URLs, templates, CSS, JavaScript, database migrations, authentication, PDF/Excel reports, backup system, and installation instructions. No placeholders, no TODOs, and every button/function must work completely.