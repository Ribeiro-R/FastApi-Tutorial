'''
Let's say that you want to declare the query parameter q as a required str.

And you don't need to declare anything else for that parameter,
so you don't really need to use Query.

But you still need to use Path for the item_id path parameter.

Python will complain if you put a value with a "default"
before a value that doesn't have a "default".

But you can re-order them, and have the value without a
default (the query parameter q) first.

It doesn't matter for FastAPI. It will detect the parameters
by their names, types and default declarations (Query, Path, etc),
it doesn't care about the order
'''
from fastapi import FastAPI, Path

app = FastAPI()


@app.get("/items/{item_id}")
async def read_items(
    q: str, item_id: int = Path(..., title="The ID of the item to get")
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results
