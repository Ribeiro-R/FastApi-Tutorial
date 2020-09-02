'''
The same way you can pass extra info to Field, you can do the
same with Path, Query, Body, etc.

For example, you can pass an example for a body request to Body'''

from typing import Optional
from fastapi import Body, FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None


@app.put("/items/{item_id}")
async def update_item(item_id: int,
                      item: Item = Body(...,
                                        example={"name": "Foo",
                                                 "description": "A nice Item",
                                                 "price": 35.4,
                                                 "tax": 3.2,
                                                 },
                                        ),
                      ):
    results = {"item_id": item_id, "item": item}
    return results

# That extra info will be added as-is to the output JSON Schema.

'''
Technical Details

About example vs examples...

JSON Schema defines a field examples in the most recent versions,
but OpenAPI is based on an older version of JSON Schema that
didn't have examples.

So, OpenAPI defined its own example for the same purpose
(as example, not examples), and that's what is used by
the docs UI (using Swagger UI).

So, although example is not part of JSON Schema, it
is part of OpenAPI, and that's what will be used
by the docs UI.
'''
