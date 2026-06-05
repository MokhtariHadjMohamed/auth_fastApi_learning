# 🚀 FastAPI JWT Authentication Practice

A hands-on practice repository demonstrating how to implement a secure, standard User Authentication and Authorization system using FastAPI, SQLAlchemy, and JWT (JSON Web Tokens).

# 🛠️ Tech Stack & Dependencies
This project explores backend security fundamentals using the following specific libraries:
- fastapi[standard]: The modern, fast web framework for building APIs with Python, including standard production tools like uvicorn.
- SQLAlchemy: The SQL Toolkit and Object-Relational Mapper (ORM) to interact with the database.
- python-jose[cryptography]: Used to generate, decode, and verify JWT tokens securely.
- bcrypt: Used for secure password hashing and verification.
- python-multipart: Enables FastAPI to accept form data (required for the OAuth2 login flow).

# 🏗️ Architecture & Flow
[ Client ] ---> ( Form Data: Username/Password ) ---> [ /token Endpoint ]
    ^                                                        |
    |                                                 Validates & Issues
    |                                                        v
[ Protected Route ] <--- ( Header: Bearer <JWT> ) <--- [ Signed JWT Token ]

- Registration: User creates an account; the password is encrypted using bcrypt and stored in the database via SQLAlchemy.
- Authentication: User logs in via the OAuth2 standard form. The server verifies the credentials and returns a signed Access Token (JWT).
- Authorization: The client includes the JWT in the Authorization: Bearer <token> header to access restricted endpoints.