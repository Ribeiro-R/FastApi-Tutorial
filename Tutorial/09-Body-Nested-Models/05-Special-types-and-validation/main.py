'''Apart from normal singular types like str, int, float, etc.
You can use more complex singular types that inherit from str.

To see all the options you have, checkout the docs for
Pydantic's exotic types. You will see some examples in
the next chapter.

For example, as in the Image model we have a url field,
we can declare it to be instead of a str, a Pydantic's HttpUrl'''

from typing import Optional, Set
from fastapi import FastAPI
from pydantic import BaseModel, HttpUrl

app = FastAPI()


class Image(BaseModel):
    url: HttpUrl
    name: str


class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None
    tags: Set[str] = []
    image: Optional[Image] = None


@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    results = {"item_id": item_id, "item": item}
    return results

'''The string will be checked to be a valid URL,
and documented in JSON Schema / OpenAPI as such.'''
