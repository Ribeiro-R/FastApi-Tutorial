'''
Summary and description¶

You can add a summary and description
'''

from typing import Optional, Set
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    description: Optional[str] = None
    prince: float
    tax: Optional[float] = None
    tags: Set[str] = []


@app.post("/items/", response_model=Item,
          summary="Create a item",
          description="Create an item with all the information, name,\
              description, price, tax and a set of unique tags")
async def create_item(item: Item):
    return item
