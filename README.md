# Expense Tracker API

A simple RESTful API for tracking income and expenses with user authentication, built with Django REST Framework and JWT.

---

## Features

- User registration and JWT authentication (login, token refresh)
- CRUD operations for Expense/Income transactions
- Transactions linked to authenticated users
- Tax calculation with flat or percentage tax types
- Pagination on list endpoints
- Admin users can access all transactions
- Custom success messages on update and delete

---

## Tech Stack

- Python 3.x
- Django 4.x
- Django REST Framework
- djangorestframework-simplejwt (JWT Authentication)
- SQLite (default DB, can be replaced)

---

## Getting Started

### Prerequisites

- Python 3.8+
- pip
- virtualenv (recommended)

### Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/expense-tracker-api.git
cd expense-tracker-api

## Installation & Setup

If you clone this repository, please be sure to:

- **Create and activate a Python virtual environment:**

  ```bash
  python -m venv venv
  source venv/bin/activate      # macOS/Linux
  venv\Scripts\activate         # Windows
  pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver

    Usage
Register a user by sending a POST request to /api/auth/register/

Login with credentials at /api/auth/login/ to get JWT tokens

Include the access token in the header:

makefile
Copy
Edit
Authorization: Bearer <token>
to access protected endpoints like /api/transactions/

API Endpoints
Authentication
Endpoint	Method	Description
/api/auth/register/	POST	Register a new user
/api/auth/login/	POST	Obtain JWT token
/api/auth/token/refresh/	POST	Refresh JWT token

Transactions
Endpoint	Method	Description
/api/transactions/	GET	List user's transactions
/api/transactions/	POST	Create a new transaction
/api/transactions/{id}/	GET	Retrieve transaction details
/api/transactions/{id}/	PUT	Update a transaction
/api/transactions/{id}/	DELETE	Delete a transaction

Pagination
List endpoints return 10 records per page by default.

Use the ?page= query parameter to access other pages, e.g., /api/transactions/?page=2

Models
ExpenseIncome
Field	Type	Description
user	ForeignKey	Owner of the transaction
title	CharField	Transaction title
description	TextField	Optional description
amount	DecimalField	Amount of money
transaction_type	CharField	'credit' or 'debit'
tax	DecimalField	Tax amount
tax_type	CharField	'flat' or 'percentage'
created_at	DateTimeField	Creation timestamp
updated_at	DateTimeField	Last update timestamp

Notes for Users Cloning This Repository
When cloning this repository, you should:

Create and activate a Python virtual environment

Install dependencies from requirements.txt

Run makemigrations and migrate to set up the database schema

(Optional) Create a superuser for admin access

Start the development server using runserver


