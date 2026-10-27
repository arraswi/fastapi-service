# FastAPI Service

![License](https://img.shields.io/badge/license-MIT-blue.svg) ![Version](https://img.shields.io/badge/version-1.0.0-green.svg)


API example built with FastAPI and Pydantic. Authentication is incomplete;
this service is not ready for production deployment.

## Features

- ⚡ High performance with FastAPI
- 📝 Automatic OpenAPI (Swagger) documentation
- ✅ Data validation with Pydantic v2
- 🔐 JWT token generation example (authentication incomplete)
- 🧪 Complete test suite with pytest
- 📊 API versioning support

## Quick Start

```bash
pip install -r requirements.txt
```

Copy `.env.example` to `.env`. Generate a unique signing key with:

```bash
python -c "import secrets; print(secrets.token_hex(32))"
```

Set `SECRET_KEY` in `.env` to the generated value, then start the API:

```bash
uvicorn app.main:app --env-file .env --reload --port 8000
```

`--env-file` explicitly loads configuration for the application. Alternatively,
inject `SECRET_KEY` through the process environment. Startup fails if the key
is missing, blank, a known placeholder, or shorter than 32 bytes after trimming
whitespace. Length validation does not guarantee randomness: always generate
the key. Never commit real keys. Use `--reload` only for local development.

### Storage and authentication limitations

Items and users are stored in memory and lost on restart. PostgreSQL is not
integrated, and there is no `DATABASE_URL` setting. This is a FastAPI service;
`FLASK_ENV` is not used.

`/login` does not validate credentials and issues tokens without expiration.
Its parameters are currently query parameters, so do not send real passwords.
No route applies `verify_token`; generating a token does not protect the API.
A secure signing key does not resolve these authentication limitations.

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
python -m pytest -v
```

The test configuration generates a separate ephemeral signing key and resets
in-memory state between API tests. It does not require a developer's `.env`.

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
