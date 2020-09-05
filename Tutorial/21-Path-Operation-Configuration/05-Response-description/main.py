'''
Response description

You can specify the response description
with the parameter response_description
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


@app.post("/items/",
          response_model=Item,
          summary="Create a Item",
          response_description="The created item")
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

'''
Info

Notice that response_description refers specifically
to the response, the description refers to the path operation in general.

Check

OpenAPI specifies that each path operation requires a response description.

So, if you don't provide one, FastAPI will automatically
generate one of "Successful response".
'''
