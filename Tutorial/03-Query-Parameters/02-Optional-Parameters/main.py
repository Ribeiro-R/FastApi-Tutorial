from typing import Optional
from fastapi import FastAPI

app = FastAPI()

'''
The same way, you can declare optional query parameters,
by setting their default to None.
'''


@app.get("/items/{item_id}")
async def read_item(item_id: str, q: Optional[str] = None):
    if q:
        return {"item_id": item_id, "q": q}
    return {"item_id": item_id}

'''In this case, the function parameter q will be optional,
and will be None by default.

Also notice that FastAPI is smart enough to notice that the path
parameter item_id is a path parameter and q is not, so, it's a query parameter.

FastAPI will know that q is optional because of the = None.

The Optional in Optional[str] is not used by FastAPI
(FastAPI will only use the str part), but the Optional[str]
will let your editor help you finding errors in your code.
'''
