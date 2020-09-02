'''
You can also declare body, path and query parameters, all at the same time.

FastAPI will recognize each of them and take the data from the correct place.
'''
from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel


class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None


app = FastAPI()


@app.put("/items/{item_id}")
async def create_item(item_id: int, item: Item, q: Optional[str] = None):
    result = {"item_id": item_id, **item.dict()}
    if q:
        result.update({"q": q})
    return result

'''
The function parameters will be recognized as follows:

    If the parameter is also declared in the path,
    it will be used as a path parameter.

    If the parameter is of a singular type
    (like int, float, str, bool, etc) it will be
    interpreted as a query parameter.

    If the parameter is declared to be of the type
    of a Pydantic model, it will be interpreted as a request body.

Note

FastAPI will know that the value of q is not
required because of the default value = None.

The Optional in Optional[str] is not used by FastAPI,
but will allow your editor to give you better support and detect errors.

'''
