# Subtract Cloud API! [Subtract Manufacturing](https://subtractmanufacturing.com/wp-content/uploads/2025/05/subtract_logo_01_social-small-red.png)

A modern, high-performance backend API built with FastAPI and SQLModel, designed to handle connection to the Subtract Application Interface.

![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![SQLModel](https://img.shields.io/badge/SQLModel-FF4154?style=for-the-badge&logo=sqlite&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)

## 📋 Features

- RESTful API with automatic OpenAPI documentation
- Flexible data models for shipments and inventory items
- Database abstraction layer supporting both SQLite (development) and PostgreSQL (production)
- Comprehensive validation and error handling
- CORS middleware for frontend integration
- Easily extensible architecture

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- UV package manager (recommended) or pip

### Setting Up Development Environment

1. **Clone the repository**

```bash
git clone https://github.com/yourusername/subtract-cloud.git
cd subtract-cloud/backend
```

2. **Create and activate a virtual environment**

Using UV (recommended):

```bash
uv venv
```

Activate the virtual environment:

On Windows:

```bash
.venv\Scripts\activate
```

On macOS/Linux:

```bash
source .venv/bin/activate
```

3. **Install dependencies**

```bash
uv pip install -r requirements.txt
```

4. **Set up environment variables**

Create a `.env` file in the project root:

```
DATABASE_URL=sqlite:///./sql_app.db
```

5. **Run the application**

```bash
python run.py
```

The API will be available at [http://localhost:8000](http://localhost:8000).

API documentation can be accessed at:

- Swagger UI: [http://localhost:8000/docs](http://localhost:8000/docs)
- ReDoc: [http://localhost:8000/redoc](http://localhost:8000/redoc)

## 🏗️ Project Structure

```
backend/
├── app/
│   ├── __init__.py
│   ├── main.py           # Main application entry point
│   ├── database.py       # Database connection and session management
│   ├── config.py         # Configuration settings
│   ├── models/           # SQLModel models (database tables)
│   │   ├── __init__.py
│   │   ├── item.py       # Item model
│   │   └── shipment.py   # Shipment model
│   └── routes/           # API route handlers
│       ├── __init__.py
│       ├── items.py      # Item-related endpoints
│       └── shipments.py  # Shipment-related endpoints
├── requirements.txt      # Project dependencies
├── .env                  # Environment variables (create this file)
├── .gitignore            # Git ignore rules
└── run.py                # Script to run the application
```


## 📚 Documentation

For more detailed information about the API, refer to the Swagger documentation at [http://localhost:8000/docs](http://localhost:8000/docs) when the server is running.

## 🔐 Environment Variables

| Variable     | Description                | Default                |
| ------------ | -------------------------- | ---------------------- |
| DATABASE_URL | Database connection string | sqlite:///./sql_app.db |

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project currently is not assigned a license

## 📧 Contact

Jacob Munoz - [jacob@subtractmanufacturing.com](mailto:jacob@subtractmanufacturing.com)

---

<p align="center">Made with ❤️ using FastAPI and SQLModel</p>
