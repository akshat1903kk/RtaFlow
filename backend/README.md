# ṚtaFlow Backend

> *FastAPI-powered backend for privacy-first journaling and task management*

[![FastAPI](https://img.shields.io/badge/FastAPI-0.115+-009688.svg)](https://fastapi.tiangolo.com/)
[![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)](https://www.python.org/)
[![SQLite](https://img.shields.io/badge/SQLite-3-003B57.svg)](https://www.sqlite.org/)

This is the backend API server for ṚtaFlow, built with FastAPI and SQLite. It provides a RESTful API for managing journal entries, tasks, and user data with a focus on performance, simplicity, and local-first architecture.

---

## 🏗️ Architecture

The backend follows a clean, modular architecture based on FastAPI best practices:

```
backend/
├── app/
│   ├── __init__.py
│   ├── main.py              # FastAPI application entry point
│   ├── core/                # Core configurations
│   │   ├── config.py        # Environment & app configuration
│   │   ├── security.py      # Authentication & security utilities
│   │   └── database.py      # Database connection & session management
│   ├── models/              # SQLAlchemy ORM models
│   │   ├── user.py          # User model
│   │   ├── journal.py       # Journal entry model
│   │   └── task.py          # Task model
│   ├── schemas/             # Pydantic models for request/response
│   │   ├── user.py          # User schemas
│   │   ├── journal.py       # Journal schemas
│   │   └── task.py          # Task schemas
│   ├── routers/             # API route handlers
│   │   ├── auth.py          # Authentication endpoints
│   │   ├── journals.py      # Journal CRUD endpoints
│   │   └── tasks.py         # Task management endpoints
│   ├── services/            # Business logic layer
│   │   ├── auth_service.py  # Authentication logic
│   │   ├── journal_service.py
│   │   └── task_service.py
│   └── dependencies.py      # Shared dependencies (DB sessions, auth)
├── tests/                   # Test suite
│   ├── test_auth.py
│   ├── test_journals.py
│   └── test_tasks.py
├── alembic/                 # Database migrations
├── .env.example             # Environment variables template
├── requirements.txt         # Python dependencies
└── README.md               # This file
```

### Design Patterns

- **Model-Service-Controller (MSC)**: Clear separation of concerns
- **Dependency Injection**: FastAPI's DI system for database sessions and auth
- **Repository Pattern**: Data access abstraction through SQLAlchemy models
- **Schema Validation**: Pydantic models for type-safe request/response handling

---

## 🚀 Getting Started

### Prerequisites

- **Python 3.11+** (recommended: 3.12)
- **pip** or **poetry** for dependency management
- **SQLite** (included with Python)

### Installation

1. **Navigate to the backend directory**
   ```bash
   cd backend
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   
   # Activate on Linux/Mac
   source venv/bin/activate
   
   # Activate on Windows
   venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   ```bash
   cp .env.example .env
   # Edit .env with your configuration
   ```

5. **Initialize the database**
   ```bash
   # Run migrations
   alembic upgrade head
   ```

### Running the Development Server

```bash
# Standard way
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

# Or using FastAPI CLI (recommended)
fastapi dev app/main.py
```

The API will be available at:
- **API Server**: http://localhost:8000
- **Interactive Docs (Swagger UI)**: http://localhost:8000/docs
- **Alternative Docs (ReDoc)**: http://localhost:8000/redoc

---

## 📚 API Documentation

### Authentication Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/v1/auth/register` | Register new user |
| POST | `/api/v1/auth/login` | User login |
| POST | `/api/v1/auth/refresh` | Refresh access token |
| POST | `/api/v1/auth/logout` | User logout |

### Journal Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/v1/journals` | List all journal entries |
| GET | `/api/v1/journals/{id}` | Get specific entry |
| POST | `/api/v1/journals` | Create new entry |
| PUT | `/api/v1/journals/{id}` | Update entry |
| DELETE | `/api/v1/journals/{id}` | Delete entry |

### Task Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/v1/tasks` | List all tasks |
| GET | `/api/v1/tasks/{id}` | Get specific task |
| POST | `/api/v1/tasks` | Create new task |
| PUT | `/api/v1/tasks/{id}` | Update task |
| PATCH | `/api/v1/tasks/{id}/complete` | Mark task complete |
| DELETE | `/api/v1/tasks/{id}` | Delete task |

For detailed API documentation with request/response examples, visit `/docs` when the server is running.

---

## 🧪 Testing

### Running Tests

```bash
# Run all tests
pytest

# Run with coverage report
pytest --cov=app --cov-report=html

# Run specific test file
pytest tests/test_journals.py

# Run with verbose output
pytest -v
```

### Test Structure

Tests are organized to mirror the application structure:

```
tests/
├── conftest.py          # Pytest fixtures and configuration
├── test_auth.py         # Authentication tests
├── test_journals.py     # Journal endpoint tests
├── test_tasks.py        # Task endpoint tests
└── test_services.py     # Business logic tests
```

---

## 🗄️ Database

### SQLite Database

The backend uses SQLite for local-first data storage:

- **Development DB**: `./rtaflow_dev.db`
- **Test DB**: `./test_db.sqlite`
- **Production DB**: Configured via environment variable

### Migrations

Database migrations are managed with Alembic:

```bash
# Create a new migration
alembic revision --autogenerate -m "Description of changes"

# Apply migrations
alembic upgrade head

# Rollback one migration
alembic downgrade -1

# View migration history
alembic history
```

### Models

**User Model**
- `id`: Primary key
- `email`: Unique email address
- `username`: Unique username
- `hashed_password`: Bcrypt hashed password
- `created_at`: Timestamp
- `is_active`: Boolean flag

**Journal Entry Model**
- `id`: Primary key
- `user_id`: Foreign key to User
- `title`: Entry title
- `content`: Markdown content
- `created_at`: Timestamp
- `updated_at`: Timestamp
- `tags`: Many-to-many relationship

**Task Model**
- `id`: Primary key
- `user_id`: Foreign key to User
- `title`: Task title
- `description`: Optional description
- `completed`: Boolean status
- `due_date`: Optional due date
- `priority`: Enum (low, medium, high)
- `created_at`: Timestamp

---

## 🔒 Security

### Authentication

- **JWT Tokens**: Used for stateless authentication
- **Bcrypt**: Password hashing with salt rounds
- **Token Expiry**: Access tokens expire in 15 minutes, refresh tokens in 7 days

### Best Practices

- Passwords are never stored in plain text
- SQL injection prevention through SQLAlchemy ORM
- CORS configuration for frontend integration
- Rate limiting on authentication endpoints (planned)
- Input validation with Pydantic schemas

---

## ⚙️ Configuration

### Environment Variables

Create a `.env` file based on `.env.example`:

```env
# Application
APP_NAME=RtaFlow
DEBUG=True
VERSION=0.1.0

# Database
DATABASE_URL=sqlite:///./rtaflow_dev.db

# Security
SECRET_KEY=your-secret-key-here-change-in-production
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=15
REFRESH_TOKEN_EXPIRE_DAYS=7

# CORS (for frontend)
CORS_ORIGINS=http://localhost:3000,http://localhost:5173

# Server
HOST=0.0.0.0
PORT=8000
```

---

## 📦 Dependencies

### Core Dependencies

- **FastAPI**: Modern web framework for building APIs
- **Uvicorn**: ASGI server
- **SQLAlchemy**: SQL ORM toolkit
- **Pydantic**: Data validation using Python type hints
- **Alembic**: Database migration tool
- **python-jose**: JWT token handling
- **passlib**: Password hashing
- **python-multipart**: Form data parsing

### Development Dependencies

- **pytest**: Testing framework
- **pytest-cov**: Code coverage
- **httpx**: Async HTTP client for testing
- **black**: Code formatter
- **flake8**: Linting
- **mypy**: Static type checking

---

## 🚦 Development Guidelines

### Code Style

```bash
# Format code with Black
black app/

# Run linter
flake8 app/

# Type checking
mypy app/
```

### Adding New Endpoints

1. **Create/update model** in `app/models/`
2. **Define schemas** in `app/schemas/`
3. **Implement service logic** in `app/services/`
4. **Create router** in `app/routers/`
5. **Write tests** in `tests/`
6. **Update documentation**

### Async vs Sync

- Use `async def` for I/O-bound operations (database queries, external APIs)
- Use regular `def` for CPU-bound operations
- Database operations should be async using `asyncpg` or similar

---

## 📈 Performance Considerations

### Optimization Strategies

- **Connection Pooling**: SQLAlchemy connection pool for database efficiency
- **Lazy Loading**: Strategic use of lazy vs eager loading for relationships
- **Caching**: Planned Redis integration for frequently accessed data
- **Pagination**: All list endpoints support pagination
- **Query Optimization**: Indexes on frequently queried fields

### Monitoring

- **Logging**: Structured logging with JSON format
- **Metrics**: Planned Prometheus integration
- **Health Check**: `/health` endpoint for monitoring

---

## 🗺️ Roadmap

### Phase 1: Core Features (Current)
- [x] FastAPI project setup
- [x] SQLite database integration
- [x] Basic project structure
- [ ] User authentication (JWT)
- [ ] Journal CRUD operations
- [ ] Task management endpoints
- [ ] Unit tests (80%+ coverage)

### Phase 2: Enhanced Features
- [ ] Full-text search for journals
- [ ] Tag management
- [ ] File attachments
- [ ] Data export (JSON, Markdown)
- [ ] Backup/restore functionality

### Phase 3: Advanced Features
- [ ] End-to-end encryption
- [ ] Optional cloud sync
- [ ] Real-time updates (WebSockets)
- [ ] Bulk operations
- [ ] API rate limiting
- [ ] Comprehensive audit logs

### Phase 4: Optimization
- [ ] Database query optimization
- [ ] Redis caching layer
- [ ] PostgreSQL support
- [ ] Docker containerization
- [ ] CI/CD pipeline
- [ ] Performance benchmarking

---

## 🤝 Contributing

We welcome contributions to the backend! Here's how to get started:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Write/update tests
5. Ensure all tests pass (`pytest`)
6. Format code (`black app/`)
7. Commit changes (`git commit -m 'Add amazing feature'`)
8. Push to branch (`git push origin feature/amazing-feature`)
9. Open a Pull Request

### Contribution Guidelines

- Follow PEP 8 style guidelines
- Write docstrings for all functions/classes
- Maintain test coverage above 80%
- Update documentation for API changes
- Use type hints consistently

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](../LICENSE) file for details.

---

## 🔗 Related Documentation

- [Main Project README](../README.md)
- [Frontend Documentation](../frontend/README.md) *(Coming Soon)*
- [Deployment Guide](../docs/deployment.md) *(Coming Soon)*
- [API Reference](http://localhost:8000/docs) *(When server is running)*

---

## 📞 Support

For backend-specific questions or issues:
- Open an issue on GitHub
- Check the [FastAPI documentation](https://fastapi.tiangolo.com/)
- Review the [SQLAlchemy documentation](https://docs.sqlalchemy.org/)

---

<div align="center">
  <sub>Built with FastAPI ⚡ • Powered by Python 🐍</sub>
</div>
