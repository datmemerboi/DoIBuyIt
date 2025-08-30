# Getting Started with Django and Uvicorn

1. **Install dependencies**:
  ```bash
  uv sync --all-groups
  ```
2. Import data
  ```bash
  python manage.py shell < main.py
  ```
3. Run the django server
  ```bash
  uv run python manage.py runserver 8080
  ```