'''
Shortcut

But you see that we are having some code repetition here,
writing CommonQueryParams twice:

commons: CommonQueryParams = Depends(CommonQueryParams)

FastAPI provides a shortcut for these cases, in where the dependency is
specifically a class that FastAPI will "call" to create an instance of
the class itself.

For those specific cases, you can do the following:

Instead of writing:

commons: CommonQueryParams = Depends(CommonQueryParams)

...you write:

commons: CommonQueryParams = Depends()

You declare the dependency as the type of the parameter, and you use Depends()
as its "default" value (that after the =) for that function's parameter,
without any parameter in Depends(), instead of having to write the full class
again inside of Depends(CommonQueryParams).

The same example would then look like:
'''
from typing import Optional

from fastapi import Depends, FastAPI

app = FastAPI()


fake_items_db = [{"item_name": "Foo"},
                 {"item_name": "Bar"},
                 {"item_name": "Baz"}]


class CommonQueryParams:
    def __init__(self,
                 q: Optional[str] = None,
                 skip: int = 0,
                 limit: int = 100):
        self.q = q
        self.skip = skip
        self.limit = limit


@app.get("/items/")
async def read_items(commons: CommonQueryParams = Depends()):
    response = {}
    if commons.q:
        response.update({"q": commons.q})
    items = fake_items_db[commons.skip: commons.skip + commons.limit]
    response.update({"items": items})
    return response

'''...and FastAPI will know what to do.'''
