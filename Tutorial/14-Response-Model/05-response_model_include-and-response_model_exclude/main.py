'''
You can also use the path operation decorator parameters
response_model_include
and
response_model_exclude.

They take a set of str with the name of the attributes to
include (omitting the rest)
or to
exclude (including the rest).

This can be used as a quick shortcut if you have only one
Pydantic model and want to remove some data from the output.

Tip

But it is still recommended to use the ideas above,
using multiple classes, instead of these parameters.

This is because the JSON Schema generated in your app's
OpenAPI (and the docs) will still be the one for the
complete model, even if you use response_model_include
or response_model_exclude to omit some attributes.

This also applies to response_model_by_alias that works similarly.
'''
from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: float = 10.5


items = {
    "foo": {"name": "Foo", "price": 50.2},
    "bar": {"name": "Bar",
            "description": "The Bar fighters",
            "price": 62, "tax": 20.2},
    "baz": {
        "name": "Baz",
        "description": "There goes my baz",
        "price": 50.2,
        "tax": 10.5,
    },
}


@app.get(
    "/items/{item_id}/name",
    response_model=Item,
    response_model_include={"name", "description"},
)
async def read_item_name(item_id: str):
    return items[item_id]


@app.get("/items/{item_id}/public",
         response_model=Item,
         response_model_exclude={"tax"})
async def read_item_public_data(item_id: str):
    return items[item_id]

'''
Tip

The syntax {"name", "description"} creates a set with those two values.

It is equivalent to set(["name", "description"]).
'''
