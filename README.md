# Internal App for Business

This is an internal web application designed to streamline business processes. It integrates task management, leave tracking, and dashboards to provide a unified platform for managing internal operations efficiently.

## Features
### Task Management
- **Create, Read, Update, and Delete (CRUD)**: Manage tasks for projects and individuals.
- **User-based Access**: Ensure users see only tasks relevant to them.
- **Task Assignment**: Assign tasks to team members with due dates and priority levels.

### Leave Tracking
- **Apply for Leave**: Employees can submit leave requests for approval.
- **Approval Workflow**: Admins can approve or reject leave applications.
- **Leave Balances**: Track available leave types and balances for employees.
- **Notifications**: Get notified of new leave requests and approvals.

### Technology Stack
**Backend**: Django (Python)\
**Frontend**: HTML, CSS (with Bootstrap)\
**Database**: SQLite

### Usage
- Admin Panel: Accessible at /admin to manage users, tasks, and leave settings.
- Login: Users must log in to access their dashboard and manage tasks or leave.

### URL Structure
/projects/: Contains task management modules.\
/leaves/: Leave tracking modules.\
/: Code for user-specific dashboard views.\
/templates/: HTML templates for the frontend.\
/static/: Static files like CSS, JS, and images.