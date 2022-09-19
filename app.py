from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"Status": "Alive!"}


@app.get("/hello")
async def say_hello(user: str = "Anonymous"):
    return {"Message": f"Hello {user}!"}
