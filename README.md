# Mini Bookstore API

A simple REST API for a mini bookstore built with FastAPI, SQLAlchemy, and Docker. This project serves as a clean and simple example of a modern web application.

---

### Features
-   **User Authentication**: Secure user registration and login using JWT.
-   **Book Management**: CRUD operations (Create, Read, Update, Delete) for books, including soft-delete.
-   **Order System**: Users can create and view their own book orders.
-   **Containerized**: Fully containerized with Docker for easy setup and deployment.

### Tech Stack
-   **Backend**: FastAPI
-   **Database**: PostgreSQL with SQLAlchemy (Sync)
-   **Authentication**: `python-jose` for JWT and `passlib` for hashing
-   **Validation**: Pydantic
-   **Infrastructure**: Docker & Docker Compose

---

## How to Run

1.  **Configure:**
    Create a `.env` file from the example and set your secret key.
    ```sh
    # On Windows (PowerShell), Linux, or macOS
    cp .env.example .env
    ```
    You must open the new `.env` file and add a unique `SECRET_KEY`.

2.  **Build & Run:**
    Use Docker Compose to build and run the application.
    ```sh
    docker-compose up --build
    ```

3.  **Explore the API:**
    Once the application is running, the interactive API documentation is available at:
    [**http://localhost:8000/docs**](http://localhost:8000/docs)

    You can use this page to test all API endpoints directly from your browser.

---

<details>
<summary>Click to see API Usage Examples with cURL</summary>

### 1. Register a new user

```sh
curl -X 'POST' \
  'http://localhost:8000/users/register' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "email": "testuser@example.com",
  "password": "strongpassword"
}'
```

### 2. Log in to get a JWT Token

```sh
curl -X 'POST' \
  'http://localhost:8000/users/login' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -d 'username=testuser@example.com&password=strongpassword'
```

Copy the `access_token` from the response. We will refer to it as `YOUR_TOKEN` below.

### 3. Create a new book (Protected)

```sh
TOKEN="YOUR_TOKEN" # Paste your token here

curl -X 'POST' \
  "http://localhost:8000/books/" \
  -H "accept: application/json" \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
  "title": "The Hitchhiker''s Guide to the Galaxy",
  "author": "Douglas Adams",
  "price": 42.0
}'
```

### 4. Create an order (Protected)

Let's assume the book we created has an `id` of `1`.

```sh
TOKEN="YOUR_TOKEN" # Paste your token here

curl -X 'POST' \
  'http://localhost:8000/orders/' \
  -H 'accept: application/json' \
  -H "Authorization: Bearer $TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{
  "book_ids": [1]
}'
```
</details> 