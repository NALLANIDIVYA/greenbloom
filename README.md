# GreenBloom – Plant Shop Management System

## About the Project

GreenBloom is a Python and MySQL based Plant Shop Management System designed to manage plant shop operations. It helps manage plants, suppliers, customers, billing, and reports through a simple menu-driven application.

## Features

* Add, view, update, delete, and search plants
* Manage supplier information
* Manage customer information
* Generate and manage bills
* View sales and business reports
* MySQL database connectivity
* Menu-driven Python application
* Input validation and error handling

## Technologies Used

* Python
* MySQL
* MySQL Connector/Python

## Project Structure

```text
greenbloom/
│
├── billing_module.py
├── customer_module.py
├── database.sql
├── db_connection.py
├── main.py
├── plant_module.py
├── reports_module.py
├── requirements.txt
└── supplier_module.py
```

## Modules

### Plant Module

Manages plant details such as plant name, category, price, quantity, and supplier.

### Supplier Module

Manages supplier information and supplier-related operations.

### Customer Module

Manages customer details and customer records.

### Billing Module

Handles billing and sales transactions.

### Reports Module

Generates reports related to plants, customers, suppliers, and sales.

### Database Module

Connects the Python application with the MySQL database and manages database operations.

## Installation

1. Install Python.
2. Install MySQL.
3. Open the project folder in VS Code.
4. Install the required Python package:

```bash
pip install -r requirements.txt
```

5. Create the required database in MySQL.
6. Update the MySQL connection details in `db_connection.py`.

## How to Run

Run the main Python file:

```bash
python main.py
```

Follow the menu options displayed in the terminal.

## Database

The project uses MySQL to store plant, supplier, customer, billing, and other related information.

The `database.sql` file contains the SQL commands required for setting up the database.

## Purpose

The main purpose of this project is to provide a simple and efficient system for managing plant shop activities using Python and MySQL.

## Author

NALLANIDIVYA
