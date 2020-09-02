'''
There are some situations in where it's useful to be able to add custom
headers to the HTTP error. For example, for some types of security.

You probably won't need to use it directly in your code.

But in case you needed it for an advanced scenario, you can add
custom headers.
'''
from fastapi import FastAPI, HTTPException

app = FastAPI()

items = {"foo": "The Foo Wrestlers"}


@app.get("/items-header/{item_id}")
async def read_item_header(item_id: str):
    if item_id not in items:
        raise HTTPException(status_code=404,
                            detail="Item not found",
                            headers={"X-Error": "There goes my error"})
    return {"item": items[item_id]}
