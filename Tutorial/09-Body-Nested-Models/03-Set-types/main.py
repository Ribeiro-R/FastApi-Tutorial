'''But then we think about it, and realize that tags
shouldn't repeat, they would probably be unique strings.

And Python has a special data type for sets of unique items, the set.

Then we can import Set and declare tags as a set of str'''

from typing import Optional, Set
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None
    tags: Set[str] = set()


@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    results = {"item_id": item_id, "item": item}
    return results

'''With this, even if you receive a request with duplicate data,
it will be converted to a set of unique items.

And whenever you output that data, even if the source had duplicates,
it will be output as a set of unique items.

And it will be annotated / documented accordingly too.'''
