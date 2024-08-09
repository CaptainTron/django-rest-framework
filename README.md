# Covid Vaccination Booking

This project is a web application for covid vaccination booking. It is implemented with a basic user interface.

## Type of Users
- User
- Admin

### User Use Cases
- Login: Users can log in to their accounts.
- Sign up: New users can create an account.
- Searching for Vaccination center and working hours: Users can search for vaccination centers and view their working hours.
- Apply for a vaccination slot: Users can apply for a vaccination slot. Only 10 candidates are allowed per day.
- Logout: Users can log out of their accounts.

### Admin Use Cases
- Login: Admins have a separate login.
- Add Vaccination Centres: Admins can add new vaccination centers.
- Get dosage details: Admins can view dosage details grouped by centers.
- Remove vaccination centers: Admins can remove vaccination centers. 

### DB schema
![image](https://github.com/user-attachments/assets/1cc5060f-7c19-46f6-8b65-141038ac30ba)

### Project Structure
```
.
├── README.md
├── covid_vaccination_booking
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── __init__.cpython-310.pyc
│   │   ├── settings.cpython-310.pyc
│   │   ├── urls.cpython-310.pyc
│   │   └── wsgi.cpython-310.pyc
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── db.sqlite3
├── image.png
├── manage.py
├── requirement.txt
└── vaccination
    ├── __init__.py
    ├── __pycache__
    │   ├── __init__.cpython-310.pyc
    │   ├── admin.cpython-310.pyc
    │   ├── apps.cpython-310.pyc
    │   ├── models.cpython-310.pyc
    │   ├── urls.cpython-310.pyc
    │   └── views.cpython-310.pyc
    ├── admin.py
    ├── apps.py
    ├── migrations
    │   ├── 0001_initial.py
    │   ├── __init__.py
    │   └── __pycache__
    │       ├── 0001_initial.cpython-310.pyc
    │       └── __init__.cpython-310.pyc
    ├── models.py
    ├── templates
    │   ├── add_center.html
    │   ├── admin_dashboard.html
    │   ├── base.html
    │   ├── dosage_details.html
    │   ├── login.html
    │   ├── signup.html
    │   └── user_dashboard.html
    ├── tests.py
    ├── urls.py
    └── views.py
```
