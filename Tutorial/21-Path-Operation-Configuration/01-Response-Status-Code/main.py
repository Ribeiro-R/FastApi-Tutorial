'''
There are several parameters that you can pass to
your path operation decorator to configure it.

Warning

Notice that these parameters are passed directly to the path
operation decorator, not to your path operation function.

Response Status Code

You can define the (HTTP) status_code to be used in the
response of your path operation.

You can pass directly the int code, like 404.

But if you don't remember what each number code is for,
you can use the shortcut constants in status
'''
from typing import Optional, Set
from fastapi import FastAPI, status
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None
    tags: Set[str] = []


@app.post("/items/", response_model=Item, status_code=status.HTTP_201_CREATED)
async def create_item(item: Item):
    return item

'''
That status code will be used in the response
and will be added to the OpenAPI schema.

Technical Details

You could also use from starlette import status.

FastAPI provides the same starlette.status as fastapi.status just as a
convenience for you, the developer. But it comes directly from Starlette.
'''
