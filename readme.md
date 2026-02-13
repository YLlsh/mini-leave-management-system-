
#  Mini Leave Management System

##  Project Overview

The Mini Leave Management System is a simple web-based application built using Python Django REST Framework (DRF).

It allows users to apply for leave and managers to review, approve, or reject leave requests.

This project demonstrates backend API development, authentication, and frontend integration using JavaScript.

---

##  Features

### User Features
- Login securely
- Apply for leave
- Select leave type (Sick, Casual, Annual)
- Choose start and end date
- Provide reason for leave
- View leave status (Pending / Approved / Rejected)

###  Manager Features
- Login securely
- View all leave requests
- Approve leave requests
- Reject leave requests
- Add remarks while updating leave status

---

##  Technologies Used

### Backend
- Python
- Django
- Django REST Framework (DRF)

### Frontend( used AI tools to design and structure the UI )
- HTML
- CSS
- JavaScript (Fetch API)


### Database
- PostgreSQL

### Authentication
- JWT Token-Based Authentication

---

##  Login Credentials

Note:
after Databse Confrigration in settings.py use this for create Credentials 
---

##  Create Manager Account

Run the following code inside the Django shell:

```python
from django.contrib.auth.models import User, Group

manager = User(username='manager')
manager.set_password('m123')   
manager.save()

manager_group, created = Group.objects.get_or_create(name='manager')

manager.groups.add(manager_group)
manager.save()

##  Create Manager Normal User Account

from django.contrib.auth.models import User

user1 = User(username='user1')
user1.set_password('123')
user1.save()

user2 = User(username='user2')
user2.set_password('123')
user2.save()


Username: manager  
Password: m123  


Username: user1  
Password: 123  

Username: user2  
Password: 123  

---

