from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Item(BaseModel):
    item_name: str
    store_name: str
    price: float

items = []

@app.post("/api/item/add/add_item/",response_model=Item)
async def add_item(item: Item):
    items.append(item.dict())
    return item

@app.get("/api/item/get/get_item/{item_name}",response_model=Item)
async def get_item(item_name: str):
    for item in items:
        if item["item_name"]==item_name:
            return item
        else:
            return {"data not found"}
@app.get("/api/item/get/all/get_all_items/")
async def get_all_items():
    return items

@app.put("/api/item/update/update_item_name/{item_name}",response_model=Item)
async def update_item_name(item_name: str, item: Item):
    for i in range(len(items)):
        if items[i]["item_name"]==item_name:
            items[i]=item.dict()
            return item
        else:
           return {"item name does not exist"}

@app.delete("/api/item/delete/delete_item_by_name/{item_name}",response_model=dict)
async def delete_item_by_name(item_name: str):
        for i in range(len(items)):
          if items[i]["item_name"]==item_name:
            del items[i]
            return {"message": "successfully deleted"}
          else:
              return {"item not found"}
       