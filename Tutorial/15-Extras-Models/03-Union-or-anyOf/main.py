from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel
'''
You can declare a response to be the Union of two types,
that means, that the response would be any of the two.

It will be defined in OpenAPI with anyOf.

To do that, use the standard Python type hint typing.Union.

Note

When defining a Union, include the most specific type first,
followed by the less specific type. In the example below, the
more specific PlaneItem comes before CarItem in Union[PlaneItem, CarItem].
'''
app = FastAPI()


class BaseItem(BaseModel):
    description: str
    type_: str


class CarItem(BaseItem):
    type_ = "car"


class PlaneItem(BaseItem):
    type_ = "plane"
    size: int


items = {
    "item1": {
        "description": "All my friends drive a low rider",
        "type": "car"
    },
    "item2": {
        "description": "Music is my aeroplane, it's my aeroplane",
        "type": "plane",
        "size": 5
    },
}


@app.get("/items/{item_id}", response_model=Union[PlaneItem, CarItem])
async def read_item(item_id: str):
    return items[item_id]
