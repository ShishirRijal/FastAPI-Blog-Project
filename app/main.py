import time
from typing import Optional, Union
from fastapi import FastAPI, HTTPException, Response, status
from pydantic import BaseModel
import psycopg2
from psycopg2.extras import RealDictCursor
import os
from dotenv import load_dotenv


# load environment variables
load_dotenv()

# Create the fastAPI app
app = FastAPI()


# Connect to the database
while True:
    try:
        database_url = os.environ.get("DATABASE_URL")
        conn = psycopg2.connect(database_url,
                                cursor_factory=RealDictCursor)
        # Open a cursor to perform database operations
        cur = conn.cursor()
        print("Database connection established successfully.")
        break  # If connection is successful, break out of the loop
    except (Exception, psycopg2.DatabaseError) as error:
        print("Error connecting to the database.")
        print("Error: ", error)
        # If connection is not successful, retry after 5 seconds
        time.sleep(5)


class Post(BaseModel):
    title: str
    content: str
    published: bool = True


@app.get("/")
def home():
    return {"message": "Welcome to my website!"}


@app.get("/posts")
def get_posts():
    cur.execute("SELECT * FROM posts")
    posts = cur.fetchall()
    print(posts)
    return {"data": posts}


@app.get("/posts/{id}")
def read_post(id: int):
    # find the post with the id passed in
    cur.execute("SELECT * FROM posts WHERE id = %s", (id,))
    post = cur.fetchone()
    return {"data": post}


@app.post("/posts", status_code=status.HTTP_201_CREATED)
def create_item(post: Post):
    print(post)
    cur.execute("INSERT INTO posts (title, content, published) VALUES (%s, %s, %s) RETURNING *",
                (post.title, post.content, post.published))
    new_post = cur.fetchone()  # fetch the post that was just created
    conn.commit()  # commit the changes to the database
    return {"message": "Post has been created successfully", "data": new_post}


@app.put("/posts/{id}")
def update_post(id: int, post: Post, response: Response):
    # Find the index of the post with the specified id
    cur.execute("UPDATE posts SET title = %s, content = %s, published = %s WHERE id = %s RETURNING *",
                (post.title, post.content, post.published, id))
    updated_post = cur.fetchone()
    if updated_post:  # If the post with the id exists
        conn.commit()  # commit the changes to the database
        return {"message": "Post has been updated successfully", "data": post}
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Post with id {id} not found")


@app.delete("/posts/{id}")
def delete_post(id: int, response: Response):
    cur.execute("DELETE FROM posts WHERE id = %s RETURNING *", (id,))
    post = cur.fetchone()
    conn.commit()
    if not post:  # Post not found
        raise HTTPException(
            status_code=404, detail=f"Post with id {id} not found")
    return Response(status_code=status.HTTP_204_NO_CONTENT)
