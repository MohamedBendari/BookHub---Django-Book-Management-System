# BookHub - Book Management API
<img width="1358" height="714" alt="Screenshot 2025-08-09 155540" src="https://github.com/user-attachments/assets/22aa9044-9523-47a4-8495-81a8943b67a8" />


A Django REST API for managing book collections with full CRUD functionality.

## Features
- Create, read, update, and delete books
- RESTful API design
- JSON serialization
- Error handling

## Installation
1. Clone the repository
2. Create virtual environment: `python -m venv venv`
3. Activate environment: `venv\Scripts\activate` (Windows)
4. Install dependencies: `pip install -r requirements.txt`
5. Run migrations: `python manage.py migrate`
6. Start server: `python manage.py runserver`

## API Documentation
Endpoints available at:
- `GET/POST /api/books/`
- `GET/PUT/DELETE /api/books/<id>/`

## Testing
Use Postman to test all endpoints with various HTTP methods.
