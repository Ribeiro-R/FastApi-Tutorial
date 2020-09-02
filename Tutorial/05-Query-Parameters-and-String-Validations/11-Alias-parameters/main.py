'''
Alias parameters

Imagine that you want the parameter to be item-query.

Like in:

http://127.0.0.1:8000/items/?item-query=foobaritems

But item-query is not a valid Python variable name.

The closest would be item_query.

But you still need it to be exactly item-query...

Then you can declare an alias, and that alias is
what will be used to find the parameter value
'''
from typing import Optional
from fastapi import FastAPI, Query

app = FastAPI()


@app.get("/items/")
async def read_items(q: Optional[str] = Query(None, alias="item-query")):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results
