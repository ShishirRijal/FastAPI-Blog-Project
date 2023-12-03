# FastAPI Blog Project

## Overview

Welcome to the FastAPI Blog project! This project is a simple blogging application built using FastAPI and PostgreSQL. It distinguishes itself by opting not to use an Object-Relational Mapping (ORM) system, providing a straightforward and raw interaction with the database.

## Features

- Retrieve a list of all blog posts
- Retrieve details of a specific blog post
- Create a new blog post
- Update an existing blog post
- Delete a blog post

## Prerequisites

Before running the application, make sure you have the following installed:

- [Python](https://www.python.org/) (>= 3.7)
- [PostgreSQL](https://www.postgresql.org/)

## Setup

1. **Clone the repository:**

   ```bash
   git clone https://github.com/your-username/fastapi-blog.git

   # Navigate to project directory
   cd fastapi-blog

   # Open project in your favorite IDE
   code . # Open in VSCODE
  
2. **Create a virtual environment**
   ```bash
   python -m venv .venv
   
3. **Activate the virtual environment**
    ```bash
   # For windows
   .venv\Scripts\activate

    # For Mac and Linux
    source .venv/bin/activate

4. **Install Requirements**
    ```bash
    pip install -r requirements.txt

5. **Set up the PostgreSQL database**
  Create a database and update the .env file with your database connection string.
    ```bash
    DATABASE_URL="dbname=xxxx user=xxxx password=xxxx host=xxxx port=xxxx"

6. **Run the FastAPI application**
   ```bash
     uvicorn app.main:app --reload

The application will be accessible at http://localhost:8000.

## API Endpoints
- GET /posts: Retrieve a list of all blog posts.
- GET /posts/{id}: Retrieve details of a specific blog post.
- POST /posts: Create a new blog post.
- PUT /posts/{id}: Update an existing blog post.
- DELETE /posts/{id}: Delete a blog post.

## API Documentation

Explore the API documentation to understand and interact with the available endpoints:

- **Swagger UI (Interactive):** [http://localhost:8000/docs](http://localhost:8000/docs)

- **ReDoc (Alternative UI):** [http://localhost:8000/redoc](http://localhost:8000/redoc)

## Snapshots
- Swagger API documentation
  <img width="1512" alt="Screenshot 2023-12-03 at 9 14 03 PM" src="https://github.com/ShishirRijal/FastAPI-Blog-Project/assets/63596895/ce9eefeb-70d7-4796-919c-37fe0a9a6724">

