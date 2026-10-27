# Changelog

## [Unreleased]

### Added
- Environment configuration template with no default signing key.
- Explicit dependencies for JWT, dotenv loading, and API tests.
- Regression tests for signing-key configuration and JWT signing.

### Changed
- Load the JWT signing key from SECRET_KEY and reject missing or unsafe values.
- Document local configuration, in-memory storage, and authentication limitations.
- Ignore environment files while retaining .env.example.
- Isolate in-memory application state between API tests.
