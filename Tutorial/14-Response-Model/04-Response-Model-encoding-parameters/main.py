'''
Your response model could have default values, like
description: Optional[str] = None
tax: float = 10.5
tags: List[str] = []
'''
from typing import List, Optional
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: float = 10.5
    tags: List[str] = []


items = {"foo": {"name": "Foo",
                 "price": 50.2},
         "bar": {"name": "Bar",
                 "description": "The bartenders",
                 "price": 62,
                 "tax": 20.2},
         "baz": {"name": "Baz",
                 "description": None,
                 "price": 50.2,
                 "tax": 10.5,
                 "tags": []},
         }


@app.get("/items/{item_id}",
         response_model=Item,
         response_model_exclude_unset=True)
async def read_item(item_id: str):
    return items[item_id]

'''
description: Optional[str] = None has a default of None.
tax: float = 10.5 has a default of 10.5.
tags: List[str] = [] as a default of an empty list: [].

but you might want to omit them from the result if they
were not actually stored.

For example, if you have models with many optional attributes
in a NoSQL database, but you don't want to send very long JSON
responses full of default values.
'''
'''
Use the response_model_exclude_unset parameter

You can set the path operation decorator parameter
response_model_exclude_unset=True and those default
values won't be included in the response, only the
values actually set.

So, if you send a request to that path operation for
the item with ID foo, the response (not including
default values) will be:

{
    "name": "Foo",
    "price": 50.2
}

Info

FastAPI uses Pydantic model's .dict() with its exclude_unset
parameter to achieve this.

Info

You can also use:

    response_model_exclude_defaults=True
    response_model_exclude_none=True

as described in the Pydantic docs for exclude_defaults and exclude_none.
'''
'''
Data with values for fields with defaults

But if your data has values for the model's
fields with default values, like the item
with ID bar:

{
    "name": "Bar",
    "description": "The bartenders",
    "price": 62,
    "tax": 20.2
}

they will be included in the response.
'''
'''
Data with the same values as the defaults

If the data has the same values as the default ones,
like the item with ID baz:

{
    "name": "Baz",
    "description": None,
    "price": 50.2,
    "tax": 10.5,
    "tags": []
}

FastAPI is smart enough (actually, Pydantic is smart enough) to realize
that, even though description, tax, and tags have the same values as the
defaults, they were set explicitly (instead of taken from the defaults).

So, they will be included in the JSON response.

Tip

Notice that the default values can be anything, not only None.

They can be a list ([]), a float of 10.5, etc.
'''
