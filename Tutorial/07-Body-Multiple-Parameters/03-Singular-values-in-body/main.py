'''The same way there is a Query and Path to define extra
data for query and path parameters, FastAPI provides an
equivalent Body.

For example, extending the previous model, you could decide
that you want to have another key importance in the same body,
besides the item and user.

If you declare it as is, because it is a singular value,
FastAPI will assume that it is a query parameter.

But you can instruct FastAPI to treat it
as another body key using Body.'''

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
async def update_item(item_id: int,
                      item: Item,
                      user: User,
                      importance: int = Body(...)):
    results = {"item_id": item_id,
               "item": item,
               "user": user,
               "importance": importance}
    return results
