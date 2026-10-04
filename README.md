# Spendly — Expense Tracker

> A simple web-based expense tracker built with Python and Flask to record and manage everyday income and expenses.

[![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-3.x-000000?style=for-the-badge&logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
[![SQLite](https://img.shields.io/badge/SQLite-Database-003B57?style=for-the-badge&logo=sqlite&logoColor=white)](https://www.sqlite.org/)
[![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)](https://developer.mozilla.org/en-US/docs/Web/HTML)
[![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)](https://developer.mozilla.org/en-US/docs/Web/CSS)

---

## About the Project

**Spendly** is a web-based expense tracker built using **Python and Flask**.

I originally created this as a Python expense-tracking project and later developed it into a web application so that transactions could be managed directly through a browser.

The main goal is simple: keep track of income, expenses, and the current balance in one place.

---

## Features

- Add income and expense transactions
- View recorded transactions
- Delete transactions
- Track total income
- Track total expenses
- Calculate current balance
- Store transaction data using SQLite
- Simple browser-based interface
- Flask backend for application logic

---

## Tech Stack

| Technology | Purpose |
|---|---|
| **Python** | Application logic |
| **Flask** | Backend web framework |
| **HTML5** | Web page structure |
| **CSS3** | Styling and layout |
| **SQLite** | Database |
| **Jinja2** | Dynamic HTML templates |
| **Git** | Version control |
| **GitHub** | Source code hosting |

---

## How It Works

Spendly follows a simple flow between the browser, Flask backend, Python logic, and SQLite database.

```text
                    USER
                      │
                      ▼
                  BROWSER
                      │
                      ▼
                HTML / CSS
                      │
                      ▼
                   FLASK
                      │
                      ▼
              PYTHON LOGIC
                      │
                      ▼
              SQLITE DATABASE
                      │
                      ▼
              UPDATED WEBSITE
When a user submits a transaction, the browser sends the information to the Flask backend.

Flask receives the request, Python processes the data, and the transaction is stored in SQLite. The updated information is then displayed on the website.

Application Flow

Open Website
     │
     ▼
View Dashboard
     │
     ├──────────────────────┐
     │                      │
     ▼                      ▼
Add Transaction       View Transactions
     │                      │
     ▼                      ▼
Validate Data          Display Records
     │
     ▼
Save to Database
     │
     ▼
Update Totals
     │
     ▼
Updated Dashboard

Example

Suppose the user records:
Income   : ₹25,000
Expenses : ₹8,500

The application calculates:
Balance = Income - Expenses

Balance = ₹25,000 - ₹8,500
        = ₹16,500

Project Structure
expense-tracker/
│
├── app.py
├── requirements.txt
├── Procfile
├── README.md
│
├── templates/
│   ├── index.html
│   └── ...
│
├── static/
│   └── style.css
│
└── instance/
    └── expenses.db

Getting Started
1. Clone the Repository
git clone https://github.com/saketh21-18/expense-tracker-web.git
2. Open the Project Folder
cd expense-tracker-web
3. Create a Virtual Environment
python -m venv venv
4. Activate the Virtual Environment

Windows

venv\Scripts\activate

macOS / Linux

source venv/bin/activate
5. Install Dependencies
pip install -r requirements.txt
6. Run the Application
python app.py

Using Spendly
Add a Transaction

Enter the required transaction details and select whether it is an income or expense.

After submitting the form, Flask processes the information and stores the transaction in the database.

View Transactions

Recorded transactions can be viewed directly from the application interface.

Delete a Transaction

Transactions that are no longer required can be removed from the application.

Track Balance

The application calculates the current balance based on the income and expenses stored in the database.

Database

Spendly uses SQLite to store transaction information.

A transaction can contain details such as:

ID
Amount
Category
Type
Date
Description

SQLite was used because it is lightweight and does not require a separate database server for a project of this size.
Flask Backend

Flask handles communication between the web interface and the Python application.
HTTP Request
      │
      ▼
 Flask Route
      │
      ▼
 Python Logic
      │
      ▼
Database Operation
      │
      ▼
Template Rendering
      │
      ▼
 HTTP Response

CRUD Operations

The project uses basic CRUD concepts for handling transaction data.
| Operation  | Purpose                                       |
| ---------- | --------------------------------------------- |
| **Create** | Add a new transaction                         |
| **Read**   | Display stored transactions                   |
| **Update** | Modify transaction information when supported |
| **Delete** | Remove a transaction                          |

What I Learned

Building Spendly helped me understand how a basic Python project can be developed into a web application.

Python

Functions
Variables and data types
Conditional statements
Loops
Exception handling
Modules



Flask

Flask application structure
Routes
HTTP requests
Form handling
Template rendering
Connecting backend logic with HTML


Database

SQLite
Storing records
Reading records
Adding records
Deleting records
Basic CRUD operations


Development

Virtual environments
Installing dependencies
Debugging
Git
GitHub
Project documentation

Future Improvements

Some features I may add in future versions:

User login and registration
Monthly expense reports
More expense categories
Search and filtering
Charts and visual reports
Export transactions to CSV
Budget tracking
Mobile-friendly improvements
Cloud database
Production deployment


Why I Built This

I built Spendly to improve my understanding of Python, Flask, databases, Git, and basic web development.

The project also helped me understand how a Python-based application can be converted into something that can be accessed and used through a browser.


developer
Naga saketh sarma
BTech Student | Python | AI/ML | Software Development



