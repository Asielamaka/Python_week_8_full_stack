# Building a FastAPI application with python

from fastapi import FastAPI

app = FastAPI() # Define a route for the root URL
@app.get("/")
def home():
    return {"message": "Welcome to the FastAPI application!",
            "swagger ui": "/docs",
            "status": "success",
            "endpoints": ["/about", "/csv"]
            }

@app.get("/about")
def about():
    return {
        "course": "Python Full Stack developer", 
        "instructor": "Josh",
        "description": "Learn Python programming from scratch to building full-stack applications"
    }


@app.get("/csv")
def csv():
    csv_content = "name,age,city\nAlice,30,New York\nBob,25,Los Angeles\nCharles,35,Chicago"
    return {"csv_data": csv_content}


