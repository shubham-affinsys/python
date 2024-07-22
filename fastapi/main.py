from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel
app=FastAPI()

class Item(BaseModel):
    name:str
    price:float
    is_offer : Union[bool,None] = None 

@app.get("/")
async def read_root():
    return {"hello":"world"}
    # return "hello world"

@app.get("/items/{item_id}")
async def read_item(item_id:int,q:Union[str,None]=None):
    return {"item_id":item_id,"q":q}  #http://127.0.0.1:8000/items/5?q=myquery

@app.put("/items/{item_id}")
def update_item(item_id:int,item:Item):
    return {"item_name":item.name, "item_id":item_id}

