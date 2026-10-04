# **EXPENSE TRACKER**

> A simple and intuitive web-based expense tracker designed to help users record, manage, and understand their income and expenses in one place.

Expense Tracker is a web-based financial management application built around a simple idea:

**What if tracking your daily expenses was as simple as adding a transaction and immediately seeing where your money goes?**

The application provides a structured way to add transactions, view transaction history, delete records, track income and expenses, and understand spending through category-based expense distribution.

---

## 🌐 Live Demo

[**Visit Expense Tracker →**](https://expense-tracker-web-lemon.vercel.app/)

---

## **Overview**

Expense Tracker brings basic personal finance management into one centralized interface.

Users can:

- Add income transactions
- Add expense transactions
- View complete transaction history
- Delete transactions
- Categorize expenses
- Track total income
- Track total expenses
- View the current financial summary
- Analyze expense distribution by category
- Access transaction summary through an API
- Check application availability through a health-check endpoint

The application uses **Flask and SQLite** for its backend and database functionality, with a responsive web interface for interacting with the system.

---

## **Why Expense Tracker?**

Managing everyday expenses can become difficult when transactions are spread across:

- Notes
- Messages
- Spreadsheets
- Bank statements
- Memory
- Different applications

Expense Tracker explores a simpler approach.

Instead of manually calculating spending, users can enter transactions into one interface and immediately see a summarized view of their financial activity.

The idea is simple:

> **Add → Track → Analyze → Manage**

---

# **Features**

### **01 — Add Transactions**

Users can add new financial transactions by specifying:

- Transaction type
- Title
- Amount
- Category
- Date
- Optional note

The application supports two transaction types:

**INCOME**

and

**EXPENSE**

Example:

```text
Type        → Expense
Title       → Lunch
Amount      → ₹250
Category    → Food
Date        → 2026-10-03
Note        → College lunch

### **02 — Transaction History**

The application provides a centralized transaction history section.

Each transaction displays relevant information such as:

* Transaction title
* Transaction type
* Amount
* Category
* Date
* Note

Transactions are ordered by date so users can easily review their recent financial activity.

This makes it easier to understand:

> **Where did my money go?**

---

### **03 — Delete Transactions**

Users can remove transactions that are incorrect, outdated, or no longer required.

The delete action removes the selected transaction from the database.

The workflow is:

**Select Transaction**

↓

**Delete**

↓

**Database Updated**

↓

**Transaction Removed from History**

This keeps the transaction list clean and manageable.

---

### **04 — Income & Expense Tracking**

The application separates transactions into:

* **Income**
* **Expenses**

The dashboard calculates the total amount for each type.

The financial summary provides:

| Metric                | Description                     |
| --------------------- | ------------------------------- |
| **Income**            | Total recorded income           |
| **Expense**           | Total recorded expenses         |
| **Transaction Count** | Number of recorded transactions |

This gives users a quick overview of their financial activity.

---

### **05 — Expense Categories**

Expenses can be organized into predefined categories.

Available categories include:

* Food
* Transport
* Shopping
* Bills
* Education
* Entertainment
* Health
* Other

Categorization makes it easier to understand which areas contribute most to overall spending.

---

### **06 — Financial Summary**

The application automatically calculates a financial summary from stored transactions.

The backend calculates:

```text
Total Income
Total Expenses
Total Transactions
```

This information is displayed directly on the dashboard.

The summary updates whenever transactions are added or deleted.

---

### **07 — Expense Distribution**

Expense Tracker provides a category-based view of spending.

The application groups expenses according to their categories and calculates the total amount spent in each category.

Example:

```text
Food            ₹4,500
Transport       ₹2,000
Shopping        ₹3,200
Education       ₹1,500
Entertainment   ₹1,000
```

This allows users to identify their major spending categories.

The application retrieves this information through the summary API and uses it to create the expense distribution view.

Conceptually:

**Transactions**

↓

**Filter Expenses**

↓

**Group by Category**

↓

**Calculate Category Totals**

↓

**Display Expense Distribution**

---

### **08 — Summary API**

The application includes a backend API endpoint that provides expense distribution data.

### **Endpoint**

```text
GET /api/summary
```

The endpoint returns category-based expense information.

Example response:

```json
{
  "labels": [
    "Food",
    "Transport",
    "Shopping"
  ],
  "values": [
    4500,
    2000,
    3200
  ]
}
```

The API separates the category names from their corresponding expense totals, making the data easy to consume from the frontend.

This also demonstrates how a Flask application can expose structured JSON data for frontend components.

---

### **09 — Application Health Check**

The application includes a dedicated health-check endpoint.

### **Endpoint**

```text
GET /health
```

Example response:

```json
{
  "status": "ok"
}
```

The endpoint can be used to quickly verify whether the Flask application is running successfully.

This is especially useful for deployment monitoring and basic application diagnostics.

---

### **10 — Persistent Data Storage**

The application uses **SQLite** to store transaction records.

Each transaction contains information such as:

```text
ID
Transaction Type
Title
Amount
Category
Date
Note
```

The database structure allows transactions to remain available between normal application requests.

---

# **Tech Stack**

### **Frontend**

* **HTML5** — application structure and page layout
* **CSS3** — responsive styling and visual presentation
* **JavaScript** — frontend interactions and dynamic functionality

### **Backend**

* **Python** — core application programming language
* **Flask** — web framework and routing
* **Jinja2** — server-side HTML templating

### **Database**

* **SQLite** — lightweight relational database for transaction storage

### **API**

* **Flask JSON API** — provides expense summary data

### **Deployment**

* **Vercel**

### **Version Control**

* **Git**
* **GitHub**

---

# **Project Architecture**

```text
                         EXPENSE TRACKER
                               │
                               ▼
                    ┌─────────────────────┐
                    │    Web Interface    │
                    │    HTML / CSS / JS  │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │       Flask         │
                    │   Backend Server    │
                    └──────────┬──────────┘
                               │
              ┌────────────────┼────────────────┐
              │                │                │
              ▼                ▼                ▼
       ┌────────────┐   ┌────────────┐   ┌────────────┐
       │ Transactions│   │ Summary API│   │ Health API │
       │   Routes    │   │ /api/summary│  │  /health   │
       └──────┬─────┘   └────────────┘   └────────────┘
              │
              ▼
       ┌─────────────────────┐
       │       SQLite        │
       │      Database       │
       └─────────────────────┘
```

---

## **Project Structure**

```text
expense-tracker-web/
│
├── static/
│   ├── css/
│   │   └── style.css
│   └── js/
│       └── script.js
│
├── templates/
│   └── index.html
│
├── database/
│   └── expenses.db
│
├── app.py
├── requirements.txt
├── Procfile
├── .gitignore
└── README.md
```

---

### **Core Files**

| File                   | Purpose                                                               |
| ---------------------- | --------------------------------------------------------------------- |
| `app.py`               | Main Flask application, routes, database operations and API endpoints |
| `templates/index.html` | Main application interface                                            |
| `static/`              | Frontend styling and JavaScript assets                                |
| `database/expenses.db` | SQLite transaction database                                           |
| `requirements.txt`     | Python dependencies required by the application                       |
| `Procfile`             | Deployment/start command configuration                                |
| `.gitignore`           | Prevents unnecessary files from being committed                       |
| `README.md`            | Project documentation                                                 |

---

# **How the Application Works**

### **Step 1 — Open the Application**

The user opens the Expense Tracker web application.

The Flask backend renders the main dashboard.

---

### **Step 2 — Add a Transaction**

The user enters transaction details such as:

```text
Type
Title
Amount
Category
Date
Note
```

The form sends the information to the Flask backend.

---

### **Step 3 — Validate the Data**

The backend validates important transaction fields.

For example:

* Transaction type must be valid
* Title cannot be empty
* Amount must be greater than zero
* Transaction details must be present

Invalid data is rejected and the user receives an appropriate message.

---

### **Step 4 — Store the Transaction**

After validation, Flask inserts the transaction into the SQLite database.

Conceptually:

```text
User Input
    ↓
HTML Form
    ↓
Flask Route
    ↓
Validation
    ↓
SQLite Database
```

---

### **Step 5 — Display Transaction History**

The application retrieves stored transactions from the database.

Transactions are displayed in the transaction history section.

The user can review:

**What → How Much → Category → When**

---

### **Step 6 — Calculate Financial Summary**

The backend calculates:

```text
Total Income
Total Expenses
Transaction Count
```

The results are passed to the frontend and displayed on the dashboard.

---

### **Step 7 — Calculate Expense Distribution**

The backend filters only expense transactions.

Then it groups them by category.

```text
All Transactions
       ↓
Expense Transactions
       ↓
Group by Category
       ↓
SUM(amount)
       ↓
Expense Distribution
```

The result is then used by the application to represent spending across categories.

---

### **Step 8 — Delete a Transaction**

When the user deletes a transaction:

```text
Delete Button
     ↓
Flask Delete Route
     ↓
Transaction ID
     ↓
SQLite DELETE
     ↓
Database Updated
     ↓
Updated Transaction History
```

---

### **Step 9 — Access the Summary API**

The frontend or another client can request:

```text
GET /api/summary
```

The Flask backend calculates category-wise expenses and returns the result as JSON.

---

### **Step 10 — Check Application Health**

The application can be checked using:

```text
GET /health
```

A successful response:

```json
{
  "status": "ok"
}
```

confirms that the application is responding.

---

# **Application Data Flow**

```text
                 USER
                  │
                  ▼
          ┌───────────────┐
          │ Web Interface │
          └───────┬───────┘
                  │
                  ▼
             Flask App
                  │
        ┌─────────┼─────────┐
        │         │         │
        ▼         ▼         ▼
      Add      Delete    Summary
   Transaction Transaction   API
        │         │         │
        └─────────┼─────────┘
                  ▼
            SQLite DB
                  │
                  ▼
          Updated Dashboard
```

---

# **Database Design**

The application uses a `transactions` table.

### **Transaction Schema**

| Field              | Type    | Description               |
| ------------------ | ------- | ------------------------- |
| `id`               | INTEGER | Unique transaction ID     |
| `kind`             | TEXT    | Income or expense         |
| `title`            | TEXT    | Transaction title         |
| `amount`           | REAL    | Transaction amount        |
| `category`         | TEXT    | Expense/income category   |
| `transaction_date` | TEXT    | Date of transaction       |
| `note`             | TEXT    | Optional transaction note |

---

### **Example Database Record**

```text
ID: 1
Kind: expense
Title: Lunch
Amount: 250
Category: Food
Date: 2026-10-03
Note: College lunch
```

---

# **Application Routes**

| Method | Route          | Purpose                                   |
| ------ | -------------- | ----------------------------------------- |
| `GET`  | `/`            | Display dashboard and transaction history |
| `POST` | `/add`         | Add a new transaction                     |
| `POST` | `/delete/<id>` | Delete a transaction                      |
| `GET`  | `/api/summary` | Return category-based expense data        |
| `GET`  | `/health`      | Check application health                  |

---

# **API**

## **Expense Summary API**

### Request

```text
GET /api/summary
```

### Response

```json
{
  "labels": [
    "Food",
    "Transport",
    "Shopping"
  ],
  "values": [
    4500,
    2000,
    3200
  ]
}
```

The API calculates the total expense for each category and returns the result in JSON format.

---

## **Application Health API**

### Request

```text
GET /health
```

### Response

```json
{
  "status": "ok"
}
```

This endpoint provides a simple way to verify that the application is running.

---

# **UI & Design**

Expense Tracker focuses on keeping financial information simple and easy to understand.

### **Design Principles**

* Clean interface
* Simple navigation
* Clear financial information
* Easy transaction entry
* Organized transaction history
* Category-based expense visibility
* Responsive layout
* Clear action buttons
* Minimal unnecessary complexity

The interface is designed around the idea that users should be able to add or review a transaction without navigating through complicated screens.

---

# **User Experience**

The application follows a simple workflow:

```text
OPEN APPLICATION
       ↓
VIEW SUMMARY
       ↓
ADD TRANSACTION
       ↓
VIEW TRANSACTION HISTORY
       ↓
ANALYZE EXPENSE DISTRIBUTION
       ↓
DELETE / MANAGE TRANSACTIONS
```

The goal is to keep the complete process inside a single application.

---

# **Interaction Flow**

### **Add Transaction**

```text
User
 ↓
Transaction Form
 ↓
Validation
 ↓
Flask Backend
 ↓
SQLite
 ↓
Dashboard Updated
```

### **Delete Transaction**

```text
User
 ↓
Delete Transaction
 ↓
Flask Backend
 ↓
SQLite DELETE
 ↓
Updated History
```

### **Expense Distribution**

```text
SQLite
 ↓
Expense Transactions
 ↓
Category Grouping
 ↓
Total per Category
 ↓
Summary API
 ↓
Frontend Visualization
```

---

# **Current Limitations**

The current version is designed as a student portfolio project, so several production-level features are not implemented yet.

* No user authentication
* No individual user accounts
* No cloud database
* No recurring transaction system
* No budget management
* No bank account integration
* No advanced financial analytics
* No export to PDF or Excel
* No email notifications
* Limited transaction filtering
* No multi-user financial separation
* SQLite is suitable for lightweight use but not ideal for large-scale production workloads
* The Vercel deployment uses a temporary serverless filesystem approach, so persistent production database storage would require a managed database

These limitations provide clear directions for future development.

---

# **Future Scope**

### **User Authentication**

Introduce secure user accounts with:

* Sign up
* Login
* Logout
* Password protection
* User profiles

This would allow every user to maintain a separate financial record.

---

### **Cloud Database**

Move from local SQLite storage to a managed database such as:

```text
PostgreSQL
Supabase
Neon
```

Possible architecture:

```text
Frontend
    ↓
Flask Backend
    ↓
REST API
    ↓
Cloud Database
```

---

### **Budget Management**

Users could create budgets for categories such as:

```text
Food          ₹5,000
Transport     ₹3,000
Shopping      ₹4,000
Entertainment ₹2,000
```

The application could then warn users when spending approaches or exceeds a budget.

---

### **Advanced Analytics**

Future versions could provide:

* Monthly spending
* Weekly spending
* Category comparison
* Income vs expense trends
* Highest spending category
* Average daily spending
* Savings estimation
* Monthly financial reports

---

### **Transaction Search & Filtering**

Users could search and filter transactions by:

* Date
* Category
* Transaction type
* Amount
* Keyword

This would make managing large transaction histories easier.

---

### **Export Functionality**

Users could export their financial records as:

* CSV
* Excel
* PDF

This would make the application more useful for personal financial reporting.

---

### **Recurring Transactions**

Support could be added for recurring expenses such as:

* Rent
* Subscriptions
* Internet bills
* Tuition
* Monthly services

---

### **Financial Insights**

A future version could generate automated insights such as:

> "Food expenses increased by 18% compared to last month."

or:

> "Transport is currently your second-highest expense category."

This could make the application more useful for financial decision-making.

---

# **Local Development**

### **1. Clone the Repository**

```bash
git clone https://github.com/saketh21-18/expense-tracker-web.git
```

### **2. Enter the Project**

```bash
cd expense-tracker-web
```

### **3. Create a Virtual Environment**

Windows:

```bash
python -m venv venv
```

Activate it:

```bash
venv\Scripts\activate
```

---

### **4. Install Dependencies**

```bash
pip install -r requirements.txt
```

---

### **5. Run the Application**

```bash
python app.py
```

The application will start locally.

Open:

```text
http://127.0.0.1:5000
```

---

# **Local Development Flow**

```text
Clone Repository
       ↓
Create Virtual Environment
       ↓
Install Dependencies
       ↓
Run Flask Application
       ↓
Open Localhost
       ↓
Add Transactions
       ↓
Test Features
```

---

# **Deployment**

The application is deployed using **Vercel**.

The project contains deployment configuration required to run the Flask application in a serverless environment.

### **Deployment Flow**

```text
Local Project
     ↓
Git
     ↓
GitHub
     ↓
Vercel
     ↓
Production Deployment
```

The source code is maintained on GitHub and the deployed application is accessible through the Vercel live demo.

---

# **Project Status**

**Active Development**

Expense Tracker is a working web application focused on demonstrating:

> **TRANSACTIONS → DATABASE → SUMMARY → ANALYSIS**

The current version provides the core functionality required for basic expense management.

Future iterations can expand the project into a more complete personal finance platform.

---

# **Screenshots**

Screenshots can be added here as the interface continues to evolve.

Suggested project showcase:

1. Dashboard
2. Add transaction form
3. Transaction history
4. Income and expense summary
5. Expense distribution
6. Delete transaction workflow
7. Responsive mobile interface
8. API response examples

Example Markdown:

```markdown
![Expense Tracker Dashboard](screenshots/dashboard.png)
```

---

# **What I Learned**

Building this project helped me understand practical concepts including:

* Python application development
* Flask web development
* HTML templates
* CSS-based UI development
* JavaScript interactions
* HTTP routes
* GET and POST requests
* SQLite databases
* SQL queries
* CRUD operations
* Form handling
* JSON APIs
* Backend validation
* Data aggregation
* Category-based analysis
* Application health checks
* Git and GitHub
* Vercel deployment

The project also helped bridge the gap between writing standalone Python programs and building a complete web application.

---

# **About the Developer**

### **Naga Saketh Sarma R**

**B.Tech AIML @ PES University**

I'm a B.Tech AIML student interested in software development, artificial intelligence, problem-solving, and building practical projects that strengthen my programming and development skills.

I enjoy turning ideas into functional applications while continuously improving my understanding of Python, web development, databases, and computer science fundamentals.

Expense Tracker is one of my projects built to explore how Python can be used beyond standalone programs to create a complete web-based application.

### **Connect**

* **GitHub:** [https://github.com/saketh21-18](https://github.com/saketh21-18)
* **LinkedIn:** [https://www.linkedin.com/in/naga-saketh-sarma-r-116b10387/](https://www.linkedin.com/in/naga-saketh-sarma-r-116b10387/)

---

# **Acknowledgement**

Expense Tracker was built as an independent student project to explore:

* Python development
* Flask web development
* Backend programming
* Database management
* CRUD operations
* REST-style API development
* Data aggregation
* Frontend and backend integration
* Git and GitHub
* Web application deployment

---

## **Project Links**

* **Live Demo:** [https://expense-tracker-web-lemon.vercel.app/](https://expense-tracker-web-lemon.vercel.app/)
* **GitHub Repository:** [https://github.com/saketh21-18/expense-tracker-web](https://github.com/saketh21-18/expense-tracker-web)
* **LinkedIn:** [https://www.linkedin.com/in/naga-saketh-sarma-r-116b10387/](https://www.linkedin.com/in/naga-saketh-sarma-r-116b10387/)

---

## **Built With**

**Python · Flask · HTML · CSS · JavaScript · SQLite · Git · GitHub · Vercel**

---

<p align="center">
  <strong>EXPENSE TRACKER.</strong><br>
  Track it. Understand it. Manage it.
</p>
```
