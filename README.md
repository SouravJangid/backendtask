# Django RBAC Project

This project demonstrates Role-Based Access Control (RBAC) using Django and Django Rest Framework.

## Prerequisites

- Python 3.x
- Pip (Python package manager)
- Virtualenv (Optional but recommended)

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/rbac_project.git
   cd rbac_project

2. **Create a Virtual Environment (Optional but recommended):**
    python -m venv env
source env/bin/activate  # On Windows, use `env\Scripts\activate`

3. **Install Dependencies:**
    pip install -r requirements.txt

4. **Run Migrations:**
    python manage.py migrate

5. **Create a Superuser:**
    python manage.py createsuperuser

6. **Run the Development Server:**
    python manage.py runserver


7. **usage**
    http://127.0.0.1:8000/admin/
    
    http://127.0.0.1:8000/api/articles
