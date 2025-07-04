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
