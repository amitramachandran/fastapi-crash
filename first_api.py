from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get('/')
def root():
    return "hello world"

class Item(BaseModel):
    id : int
    name : str
    description : str | None 
    price : float
    available : bool

@app.post('/item/')
def create_item(item : Item):
    return item

@app.get('/item/{item_id}')
def items(item_id: int):
    return {"Item": item_id}