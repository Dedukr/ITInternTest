# IT Intern Test Backend

This is a Django-based project designed to manage a `Company` model with CRUD operations.
The project uses PostgreSQL as the database and Django REST Framework for API development.
The application is containerized using Docker for easy deployment.

---

## Features

- Retrieve all companies
- Create a new company
- Retrieve, update, partially update, or delete a company by ID

## Requirements

- Docker

## Setup Instructions

### Using Docker

1. Build the Docker image:

   ```bash
   docker-compose build
   ```

2. Run the containers:

   ```bash
   docker-compose up
   ```

3. Access the API at `http://127.0.0.1:8000/api/`.

### Without Docker

1. Clone the repository:

   ```bash
   git clone https://github.com/Dedukr/ITInternTest
   ```

2. Setup virtual environment

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Apply migrations:

   ```bash
   cd backend
   python manage.py makemigrations
   python manage.py migrate
   ```

5. Run the development server:

   ```bash
   python manage.py runserver
   ```

6. Access the API at `http://127.0.0.1:8000/api/`.

## API Endpoints

### CompanyView

- `GET /api/companies/` - Retrieve all companies
- `POST /api/companies/` - Create a new company

### CompanyDetailedView

- `GET /api/companies/<id>/` - Retrieve a company by ID
- `PUT /api/companies/<id>/` - Update a company by ID
- `PATCH /api/companies/<id>/` - Partially update a company by ID
- `DELETE /api/companies/<id>/` - Delete a company by ID

## License

This project is licensed under the MIT License.
