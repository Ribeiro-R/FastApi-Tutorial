'''But Python has a specific way to declare lists
with internal types, or "type parameters":

Import typing's List¶

First, import List from standard Python's typing module'''

from typing import List, Optional
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None
    tags: List[str] = []


@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    results = {"item_id": item_id, "item": item}
    return results

'''
Declare a List with a type parameter

To declare types that have type parameters
(internal types), like list, dict, tuple:

    * Import them from the typing module
    * Pass the internal type(s) as "type parameters"
      using square brackets: [ and ]

from typing import List

my_list: List[str]

That's all standard Python syntax for type declarations.

Use that same standard syntax for model attributes with internal types.

So, in our example, we can make tags be specifically a "list of strings"
'''
