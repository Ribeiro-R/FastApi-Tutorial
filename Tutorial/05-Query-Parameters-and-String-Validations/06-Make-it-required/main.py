'''When we don't need to declare more validations or metadata,
we can make the q query parameter required just by not declaring
a default value, like:

q: str

instead of:

q: Optional[str] = None

But we are now declaring it with Query, for example like:

q: Optional[str] = Query(None, min_length=3)

So, when you need to declare a value as required while using Query,
you can use ... as the first argument'''
from fastapi import FastAPI, Query

app = FastAPI()


@app.get("/items/")
async def read_items(q: str = Query(..., min_length=3)):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results
'''
Info

If you hadn't seen that ... before: it is a special
single value, it is part of Python and is called "Ellipsis".

This will let FastAPI know that this parameter is required
'''
