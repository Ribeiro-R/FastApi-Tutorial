'''
FastAPI allows you to declare additional
information and validation for your parameters.
'''
from typing import Optional
from fastapi import FastAPI

app = FastAPI()


@app.get("/items/")
async def read_items(q: Optional[str] = None):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results

'''The query parameter q is of type Optional[str], that means that
 it's of type str but could also be None, and indeed, the default
 value is None, so FastAPI will know it's not required.'''

'''
FastAPI will know that the value of q is not required because
of the default value = None.

The Optional in Optional[str] is not used by FastAPI, but will
allow your editor to give you better support and detect errors.
'''
