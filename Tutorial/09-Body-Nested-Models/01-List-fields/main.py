'''With FastAPI, you can define, validate, document,
and use arbitrarily deeply nested models (thanks to Pydantic).

You can define an attribute to be a subtype. For example, a Python list:
'''

from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None
    tags: list = []


@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    results = {"item_id": item_id, "item": item}
    return results

'''This will make tags be a list of items. Although it
doesn't declare the type of each of the items.'''
