from fastapi import FastAPI
from pydantic import BaseModel

# create the FastAPI application instance
app = FastAPI(title="FastAPI Intro", version="0.1.0")


# simple health / hello endpoint (GET)
@app.get("/")
def read_root():
    return {"message": "Hello, World!"}


# query parameter example (GET)
@app.get("/hello")
def hello(name: str = "friend"):
    return {"message": f"Hello, {name}!"}


# path parameter example (GET)
@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "query": q}


class NameRequest(BaseModel):
    name: str


# request body example (POST)
@app.post("/showname")
def greet(payload: NameRequest):
    return {"message": f"Hello, {payload.name}, welcome to FastAPI!"}