from typing import List
from fastapi import FastAPI
from pydantic import BaseModel
'''
The same way, you can declare responses of lists of objects.

For that, use the standard Python typing.List.
'''
app = FastAPI()


class Item(BaseModel):
    name: str
    description: str


items = [
    {"name": "Foo", "description": "There comes my hero"},
    {"name": "Red", "description": "It's my aeroplane"},
]


@app.get("/items/", response_model=List[Item])
async def read_items():
    return items
