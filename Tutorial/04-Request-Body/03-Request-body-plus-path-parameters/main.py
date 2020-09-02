'''
You can declare path parameters and body requests at the same time.

FastAPI will recognize that the function parameters that match path
parameters should be taken from the path, and that function parameters
that are declared to be Pydantic models should be taken from the request body.
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
async def create_item(item_id: int, item: Item):
    return {"item_id": item_id, **item.dict()}
