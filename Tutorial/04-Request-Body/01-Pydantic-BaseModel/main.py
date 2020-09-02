'''
When you need to send data from a client (let's say, a browser)
to your API, you send it as a request body.

A request body is data sent by the client to your API. A response
body is the data your API sends to the client.

Your API almost always has to send a response body. But clients don't
necessarily need to send request bodies all the time.

To declare a request body, you use Pydantic models with all their
power and benefits.
'''
from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel


# Create your data model
# Then you declare your data model as a class that inherits from BaseModel.
class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None
# This model above declares a JSON "object" (or Python dict)


app = FastAPI()


# '''
# Declare it as a parameter
# To add it to your path operation, declare it the same way
# you declared path and query parameters:'''
@app.post("/items/")
async def create_item(item: Item):
    return item
# ...and declare its type as the model you created, Item.
