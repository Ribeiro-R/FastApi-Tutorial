'''
In Field, Path, Query, Body and others you'll see later,
you can also declare extra info for the JSON Schema by
passing any other arbitrary arguments to the function,
for example, to add an example:
'''

from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()


class Item(BaseModel):
    name: str = Field(..., example="Foo")
    description: Optional[str] = Field(None, example="A very nice Item")
    price: float = Field(..., example=35.4)
    tax: Optional[float] = Field(None, example=3.2)


@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    results = {"item_id": item_id, "item": item}
    return results

'''
Warning

Have in mind that those extra arguments passed
won't add any validation, only annotation, for
documentation purposes.
'''
