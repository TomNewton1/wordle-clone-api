# Wordle Backend

## Overview

This is the backend for a Wordle clone built using Django. It provides and API endpoint go validate a word provided by the client.

## Prerequisites

- Python 3.10+
- Virtual environment

## How to Run This Project Locally

### 1. Create and Activate a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Apply Migrations

```bash
python manage.py migrate
```

### 4. Start Development Server

```bash
python manage.py runserver
```

### 5. Run Tests

```bash
pytest
```

---
