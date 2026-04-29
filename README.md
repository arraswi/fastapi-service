# FastAPI Service

![License](https://img.shields.io/badge/license-MIT-blue.svg) ![Version](https://img.shields.io/badge/version-1.0.0-green.svg)


Modern, production-ready API built with FastAPI and Pydantic.

## Features

- ⚡ High performance with FastAPI
- 📝 Automatic OpenAPI (Swagger) documentation
- ✅ Data validation with Pydantic v2
- 🔐 JWT Authentication ready
- 🧪 Complete test suite with pytest
- 📊 API versioning support

## Quick Start

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000
```

## API Documentation

Visit: http://localhost:8000/docs

## Endpoints

| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|---------------|
| GET | / | API info | No |
| GET | /items | List all items | No |
| POST | /items | Create item | No |
| PUT | /items/:id | Update item | No |
| DELETE | /items/:id | Delete item | No |
| POST | /login | Get JWT token | No |

## Testing

```bash
pytest -v
```

## Project Structure

```
app/
├── main.py      # FastAPI app and endpoints
├── models.py    # Pydantic models
└── __init__.py
tests/
└── test_main.py # Test suite
```

## License

MIT
