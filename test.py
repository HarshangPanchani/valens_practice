from fastapi import FastAPI
app= FastAPI()
@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

@app.post("/showname")
def greet(name:str):
    return {"message": f"Hello, {name} , welcome to FastAPI!"}