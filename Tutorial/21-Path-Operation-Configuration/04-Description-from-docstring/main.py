'''
Description from docstring

As descriptions tend to be long and cover multiple lines,
you can declare the path operation description in the function
docstring and FastAPI will read it from there.

You can write Markdown in the docstring, it will be interpreted
and displayed correctly (taking into account docstring indentation)
'''
from typing import Optional, Set
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None
    tags: Set[str] = []


@app.post("/items/", response_model=Item, summary="Create an item")
async def create_item(item: Item):
    """
    Create an item with all the information:

    - **name**: each item must have a name
    - **description**: a long description
    - **price**: required
    - **tax**: if the item doesn't have tax, you can omit this
    - **tags**: a set of unique tag strings for this item
    """
    return item
