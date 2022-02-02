from fastapi import FastAPI

app = FastAPI()

BOOKS = {

}

@app.get("/")
async def first_api():
    return {"message": "Hello Eric!"}