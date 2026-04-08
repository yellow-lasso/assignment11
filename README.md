# Congressional Trade Disclosure Analysis Tool (Web Application – Assignment 11)

## Overview

This project extends the Congressional Trade Disclosure Analysis Tool by implementing full CRUD (Create, Read, Update, Delete) functionality using Flask and SQLAlchemy.

In this version, users can not only create and view trade records, but also update existing records and delete them. This completes the core set of operations required for managing data in a web application and represents a key milestone in backend development.

---

## Features

### 1. Create (Already Implemented)

- Users can add new trade records through a web form.
- Submitted data is stored in a SQLite database using SQLAlchemy.

---

### 2. Read (Already Implemented)

- All stored trade records are retrieved from the database.
- Data is displayed dynamically on the homepage using Jinja2.

---

### 3. Update (New Feature)

- Users can edit an existing trade record.
- Each trade includes an **Edit** link that routes to:
