# context.txt

## Project Overview
This is a FastAPI backend application using SQLModel as the ORM. The project is designed to use SQLite for development and can be switched to PostgreSQL for production. The application is structured as a RESTful API with proper separation of concerns.

## Technology Stack
- **FastAPI**: Web framework for building APIs
- **SQLModel**: ORM for database interactions (combines SQLAlchemy and Pydantic)
- **Uvicorn**: ASGI server for running the application
- **UV**: Package manager (faster alternative to pip)
- **SQLite**: Development database
- **PostgreSQL**: Production database (optional)

## Project Structure
```
fastapi_project/
├── app/
│   ├── __init__.py
│   ├── main.py           # Main application entry point
│   ├── database.py       # Database connection and session management
│   ├── config.py         # Configuration settings
│   ├── models/           # SQLModel models (database tables)
│   │   ├── __init__.py
│   │   └── item.py       # Example Item model
│   ├── routes/           # API route handlers
│   │   ├── __init__.py
│   │   └── items.py      # Item-related endpoints
│   └── schemas/          # Pydantic schemas (if needed separately from models)
│       ├── __init__.py
│       └── item.py
├── requirements.txt      # Project dependencies
├── .env                  # Environment variables
└── run.py                # Script to run the application
```

## Key Files and Their Purpose

### app/config.py
Handles environment configuration, including database connection settings.

### app/database.py
Manages database connections, creates tables, and provides session dependency.

### app/models/item.py
Contains SQLModel models for database tables and Pydantic models for API.

### app/routes/items.py
Implements API endpoints for CRUD operations on items.

### app/main.py
Sets up the FastAPI application, includes routers, and configures middleware.

### run.py
Simple script to run the application with Uvicorn.

## Environment Configuration
The application uses a `.env` file to configure database connections:
- For SQLite: `DATABASE_URL=sqlite:///./sql_app.db`
- For PostgreSQL: `DATABASE_URL=postgresql://username:password@localhost/dbname`

## Package Management
The project uses UV as the package manager:
- Create virtual environment: `uv venv`
- Activate virtual environment: 
  - Windows: `.venv\Scripts\activate`
  - Unix/macOS: `source .venv/bin/activate`
- Install dependencies: `uv pip install -r requirements.txt`

## Database Handling
- The application is designed to work with both SQLite and PostgreSQL
- SQLite is used for development (no additional setup required)
- PostgreSQL requires the psycopg2-binary package and a PostgreSQL server
- Database switching is handled through the DATABASE_URL environment variable

## API Structure
- RESTful API with standard CRUD operations
- Automatic OpenAPI documentation at `/docs` endpoint
- JSON responses with proper status codes
- Input validation through Pydantic models

## Running the Application
- Start the server: `python run.py`
- Alternative: `uvicorn app.main:app --reload`
- Access the API at http://localhost:8000
- API documentation at http://localhost:8000/docs

## Known Issues
- psycopg2-binary installation may fail if PostgreSQL is not installed
- For development with SQLite only, PostgreSQL dependencies can be omitted

## Development Workflow
1. Make code changes
2. Server auto-reloads (if using --reload flag)
3. Test API using Swagger UI or tools like curl/Postman
4. Repeat

## Testing
The application can be tested using:
- Swagger UI for manual testing
- pytest for automated testing (not included in the initial setup)

## Deployment Considerations
- For production, consider using a proper PostgreSQL database
- Update the DATABASE_URL environment variable for production
- Consider using Docker for containerization
- Set up proper logging and monitoring