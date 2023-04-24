from fastapi import FastAPI
from routes.drum import router as drumRouter

from database.connection import engine
from database import models

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(drumRouter)


@app.get("/")
def printHelloWorld():
    return {"message": "Hello world!"}





@app.get("/cartitems")
def returnCartItems():
    return {"data": ["item1", "item2"]}