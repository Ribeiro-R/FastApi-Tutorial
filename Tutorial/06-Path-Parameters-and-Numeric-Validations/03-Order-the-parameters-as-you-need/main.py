'''
If you want to declare the q query parameter without a Query nor any default
value, and the path parameter item_id using Path, and have them in a different
order, Python has a little special syntax for that.

Pass *, as the first parameter of the function.

Python won't do anything with that *, but it will know that all the following
parameters should be called as keyword arguments (key-value pairs), also known
as kwargs. Even if they don't have a default value.
'''
from fastapi import FastAPI, Path

app = FastAPI()


@app.get("/items/{item_id}")
async def read_items(
    *, item_id: int = Path(..., title="The ID of the item to get"), q: str
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results
