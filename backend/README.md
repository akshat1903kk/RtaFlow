RtaFlow Backend

This directory contains the backend server for ṚtaFlow, a privacy-first journaling and task management app.

The server is built using FastAPI and uses SQLite as its database, ensuring that all data remains local and private to the user.

✨ Features

FastAPI: A modern, high-performance Python web framework for building APIs.

SQLite: A C-language library that implements a small, fast, self-contained, high-reliability, full-featured, SQL database engine.

Local-First: All data is stored and managed on your local machine.

Pydantic: Used for data validation and settings management.

🚀 Getting Started

Follow these instructions to get the backend server up and running on your local machine for development and testing.

Prerequisites

Python 3.8+

pip (Python package installer)

1. Set Up a Virtual Environment

It's highly recommended to use a virtual environment to manage project dependencies.

# Navigate to the backend directory
cd backend

# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# On macOS/Linux:
source venv/bin/activate
# On Windows:
.\venv\Scripts\activate


2. Install Dependencies

Install all the required Python packages from requirements.txt.

# Ensure your virtual environment is activated
pip install -r requirements.txt


(Note: If a requirements.txt file is not present, you may need to manually install fastapi, uvicorn, and sqlalchemy.)

3. Run the Server

The server is run using uvicorn, an ASGI server.

# Run the server
# Replace 'main:app' with the correct path to your FastAPI app instance
# (e.g., 'app.main:app' if your main file is 'app/main.py')
uvicorn main:app --reload


main:app refers to the app object in the main.py file.

--reload enables auto-reload, so the server restarts after code changes.

The server will be running at http://127.0.0.1:8000.

📚 API Documentation

Once the server is running, you can access the interactive API documentation provided by FastAPI:

Swagger UI: http://127.0.0.1:8000/docs

ReDoc: http://127.0.0.1:8000/redoc

🗄️ Database

This backend uses SQLite for its database.

The database file (e.g., rtaflow.db) will be created in the root of the backend directory when the server is first run.

Database models and schema are likely managed using SQLAlchemy (a common companion to FastAPI).

⚙️ Project Structure (Assumed)

A typical FastAPI project structure might look like this:

backend/
├── venv/                     # Virtual environment
├── app/                      # Main application module
│   ├── __init__.py
│   ├── main.py               # FastAPI app instance
│   ├── dependencies.py       # Dependency injection
│   ├── models.py             # SQLAlchemy models
│   ├── schemas.py            # Pydantic schemas
│   └── routers/              # API endpoint routers
│       ├── __init__.py
│       └── entries.py
├── tests/                    # Unit and integration tests
├── .gitignore
├── requirements.txt          # Project dependencies
└── README.md                 # This file
