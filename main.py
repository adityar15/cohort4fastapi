from fastapi import FastAPI
from routes.drum import router as drumRouter

app = FastAPI()

app.include_router(drumRouter)


@app.get("/")
def printHelloWorld():
    return {"message": "Hello world!"}





@app.get("/cartitems")
def returnCartItems():
    return {"data": ["item1", "item2"]}