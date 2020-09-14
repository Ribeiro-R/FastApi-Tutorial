'''
Update replacing with PUT

To update an item you can use the HTTP PUT operation.

You can use the jsonable_encoder to convert the input
data to data that can be stored as JSON (e.g. with a
NoSQL database). For example, converting datetime to
str.
'''
from typing import List, Optional
from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = None
    tax: float = 10.5
    tags: List[str] = []


items = {
    "foo": {"name": "Foo",
            "price": 50.2},
    "bar": {"name": "Bar",
            "description": "The bartenders",
            "price": 62.0,
            "tax": 20.2},
    "baz": {"name": "Baz",
            "description": None,
            "price": 50.2,
            "tax": 10.5,
            "tags": []},
}


@app.get("/items/{item_id}", response_model=Item)
async def read_item(item_id: str):
    return items[item_id]


@app.put("/items/{item_id}", response_model=Item)
async def update_item(item_id: str, item: Item):
    update_item_encoded = jsonable_encoder(item)
    items[item_id] = update_item_encoded
    return update_item_encoded


'''
PUT is used to receive data that should replace the existing data.

Warning about replacing

That means that if you want to update the item bar using
PUT with a body containing:

{
  "name": "Barz",
  "description": null,
  "price": 3.0,
  "tags": []
}

{
  "name": "Barz",
  "description": null,
  "price": 3,
  "tax": 10.5,
  "tags": []
}

because it doesn't include the already stored attribute "tax": 20.2,
the input model would take the default value of "tax": 10.5.

And the data would be saved with that "new" tax of 10.5.
'''
