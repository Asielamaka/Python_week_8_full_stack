# Building a FastAPI application with python

from fastapi import FastAPI

app = FastAPI() # Define a route for the root URL
@app.get("/")
def home():
    return {"message": "Welcome to the FastAPI application!"}

@app.get("/about")
def about():
    return {
        "course": "Python Full Stack developer", 
        "instructor": "Josh"
    }