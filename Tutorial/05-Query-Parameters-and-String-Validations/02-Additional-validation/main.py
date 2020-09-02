'''
We are going to enforce that even though q is optional,
whenever it is provided, it doesn't exceed a length of
50 characters.

Import Query

To achieve that, first import Query from fastapi
'''
from typing import Optional
from fastapi import FastAPI, Query

app = FastAPI()


# Use Query as the default value
# And now use it as the default value of your parameter,
# setting the parameter max_length to 50
@app.get("/items/")
async def read_items(q: Optional[str] = Query(None, max_length=50)):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results

'''
As we have to replace the default value None with Query(None),
the first parameter to Query serves the same purpose of defining
that default value.

So:

q: Optional[str] = Query(None)

...makes the parameter optional, the same as:

q: Optional[str] = None

But it declares it explicitly as being a query parameter.

Info

Have in mind that FastAPI cares about the part:

= None

or the:

= Query(None)

and will use that None to detect that the query parameter is not required.

The Optional part is only to allow your editor to provide better support.

Then, we can pass more parameters to Query. In this case,
the max_length parameter that applies to strings:

q: str = Query(None, max_length=50)

This will validate the data, show a clear error when the data is not valid,
and document the parameter in the OpenAPI schema path operation.
'''
