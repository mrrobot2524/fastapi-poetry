from fastapi import FastAPI, Path
from pydantic import BaseModel, EmailStr
from items_ciews import router as items_router
from users.views import router as users_router


app = FastAPI()
app.include_router(items_router)
app.include_router(users_router)



@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/hello/")
def hello(name:str = "World!"):
    name = name.strip().title()
    return {"message": f"Hello {name}"}


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
