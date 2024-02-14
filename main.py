from fastapi import FastAPI, Body
from pydantic import BaseModel, EmailStr

app = FastAPI()

class CreateUser(BaseModel):
    email: EmailStr


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/hello/")
def hello(name:str = "World!"):
    name = name.strip().title()
    return {"message": f"Hello {name}"}

@app.post("/users/")
def create_user(user: CreateUser):
    return {
        "message":"success",
        "email":user.email,
    }
@app.post("/calc/add/")
def add(a:int, b:int):
    return {
        "a": a,
        "b": b,
        "result": a+b,
    }

@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}

@app.get("/items/")
async def list_items(has_spa: bool = None):
    return [
        "Items 1",
        "Items 2",
        "Items 3",
    ]

@app.get("/items/latest/")
async def get_latest_item(id:int, name:str):
    return {
        "item":{
            "id":id,
            "name":name,
        },

    }

@app.get("/items/{item_id}")
async def get_item_by_id(item_id: int):
    return {
        "item":{
            "id":item_id,
        },
    }
