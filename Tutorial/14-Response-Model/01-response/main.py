'''
You can declare the model used for the response with
the parameter response_model in any of the path operations:

    @app.get()
    @app.post()
    @app.put()
    @app.delete()
    etc.
'''
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


@app.post("/items/", response_model=Item)
async def create_item(item: Item):
    return item

'''
Note

Notice that response_model is a parameter of the "decorator"
method (get, post, etc). Not of your path operation function,
like all the parameters and body.

It receives the same type you would declare for a Pydantic model attribute,
so, it can be a Pydantic model, but it can also be, e.g. a list of Pydantic
models, like List[Item].

FastAPI will use this response_model to:

    Convert the output data to its type declaration.
    Validate the data.
    Add a JSON Schema for the response, in the OpenAPI path operation.
    Will be used by the automatic documentation systems.

But most importantly:

    Will limit the output data to that of the model.
    We'll see how that's important below.

Technical Details

The response model is declared in this parameter instead of as a function
return type annotation, because the path function may not actually return
that response model but rather return a dict, database object or some other
model, and then use the response_model to perform the field limiting and
serialization.

'''
