'''In the previous example, the path operations
would expect a JSON body with the attributes
of an Item, like:

{
    "name": "Foo",
    "description": "The pretender",
    "price": 42.0,
    "tax": 3.2
}
But you can also declare multiple body parameters, e.g. item and user.
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


class User(BaseModel):
    username: str
    full_name: Optional[str] = None


@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item, user: User):
    results = {"item_id": item_id, "item": item, "user": user}
    return results

'''In this case, FastAPI will notice that thereare more than one body
parameters in the function (two parameters that are Pydantic models).'''

'''Notice that even though the item was declared the same way as before,
it is now expected to be inside of the body with a key item.'''

'''FastAPI will do the automatic conversion from the request,
so that the parameter item receives it's specific content
and the same for user.

It will perform the validation of the compound data,
and will document it like that for the OpenAPI schema
and automatic docs.'''
