from fastapi import FastAPI

# Create the app
app = FastAPI()

# Define a route (endpoint)
@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI!"}

@app.get("/hello/{name}")
def say_hello(name: str):
    return {"message": f"Hello, {name}!"}

@app.post("/add")
def add_numbers(a: int, b: int):
    return {"result": a + b}
