# 🚀 FastAPI JWT Authentication Practice

A hands-on practice repository demonstrating how to implement a secure, standard **User Authentication and Authorization system** using FastAPI, SQLAlchemy, and JWT (JSON Web Tokens).

## 🛠️ Tech Stack & Dependencies

This project explores backend security fundamentals using the following specific libraries:

* **`fastapi[standard]`**: The modern, fast web framework for building APIs with Python, including standard production tools like `uvicorn`.
* **`SQLAlchemy`**: The SQL Toolkit and Object-Relational Mapper (ORM) to interact with the database.
* **`python-jose[cryptography]`**: Used to generate, decode, and verify JWT tokens securely.
* **`bcrypt`**: Used for secure password hashing and verification.
* **`python-multipart`**: Enables FastAPI to accept form data (required for the OAuth2 login flow).
* **`pydantic-settings`**: Handles loading and strict type-validation of environment variables.

---

## 🏗️ Architecture & Flow

1. **Registration (`POST /auth/`):** User creates an account. The plain-text password is encrypted using a unique salt via `bcrypt` and saved securely into the SQLite database via `SQLAlchemy`.
2. **Authentication (`POST /auth/token`):** User submits credentials via the OAuth2 standard form data. The server locates the user, verifies the password hash, and returns a signed, UTC-timestamped Access Token (JWT).
3. **Authorization & Guarding (`GET /`):** The client includes the JWT in the `Authorization: Bearer <token>` header. An internal FastAPI dependency (`get_current_user`) decodes the token, extracts user claims, and enforces route security.

---

## 📁 Project Layout

Ensure your repository is organized cleanly at the root level without nested duplicates:

```text
├── .env             # Application secrets (Local only, Git-ignored)
├── .gitignore       # Prevents pushing caches, DB files, and secrets to Git
├── auth.py          # Authentication router, password hashing & JWT handlers
├── config.py        # Pydantic Settings management to securely ingest .env
├── main.py          # App initialization, router injection & protected endpoints
├── models.py        # SQLAlchemy engine, session maker, and DB schemas
├── mydatabase.db    # Local SQLite database file (Auto-generated)
├── README.md        # Project documentation
└── requirements.txt # Project dependency list
