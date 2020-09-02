'''Of course, you can also declare additional query
parameters whenever you need, additional to any
body parameters.

As, by default, singular values are interpreted
as query parameters, you don't have to explicitly
add a Query, you can just do:

q: Optional[str] = None
'''

from typing import Optional
from fastapi import Body, FastAPI
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
async def update_item(*,
                      item_id: int,
                      item: Item,
                      user: User,
                      importance: int = Body(..., gt=0),
                      q: Optional[str] = None):
    results = {"item_id": item_id,
               "item": item,
               "user": user,
               "importance": importance}
    if q:
        results.update({"q": q})
    return results

'''Body also has all the same extra validation and
metadata parameters as Query,Path and others you
will see later.'''
