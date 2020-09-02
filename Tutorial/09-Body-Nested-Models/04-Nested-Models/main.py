'''Each attribute of a Pydantic model has a type.

But that type can itself be another Pydantic model.

So, you can declare deeply nested JSON "objects"
with specific attribute names, types and validations.

All that, arbitrarily nested.

Define a submodel

For example, we can define an Image model'''

from typing import Optional, Set
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Image(BaseModel):
    url: str
    name: str


class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None
    tags: Set[str] = []
    # Use the submodel as a type
    # And then we can use it as the type of an attribute:
    image: Optional[Image] = None


@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    results = {"item_id": item_id, "item": item}
    return results

'''
This would mean that FastAPI would expect a body similar to:

{
    "name": "Foo",
    "description": "The pretender",
    "price": 42.0,
    "tax": 3.2,
    "tags": ["rock", "metal", "bar"],
    "image": {
        "url": "http://example.com/baz.jpg",
        "name": "The Foo live"
    }
}

Again, doing just that declaration, with FastAPI you get:

    * Editor support (completion, etc), even for nested models
    * Data conversion
    * Data validation
    * Automatic documentation
'''
