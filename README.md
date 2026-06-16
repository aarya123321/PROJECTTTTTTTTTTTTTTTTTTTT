Personal Finance - Expense Tracking & Budget Management System

Quickstart

1. Create a virtualenv and install:

```bash
python -m venv .venv
.venv\\Scripts\\activate
pip install -r requirements.txt
```

2. Run the app:

```bash
uvicorn personal_finance.main:app --reload
```

Open http://127.0.0.1:8000/docs
