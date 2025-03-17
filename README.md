# Wordle Backend

## Overview

This is the backend for a Wordle clone built using Django. It provides and API endpoint go validate a word provided by the client.

This API should be run with the following React Frontend: [https://github.com/TomNewton1/wordle-clone](https://github.com/TomNewton1/wordle-clone)

- You can add more words to the API by modifying the `words.txt` file.
- Change the word of the day by deleting the `word_of_the_day.txt` file.

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
