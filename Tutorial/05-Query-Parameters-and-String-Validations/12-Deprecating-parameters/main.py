'''
Now let's say you don't like this parameter anymore.

You have to leave it there a while because there are
clients using it, but you want the docs to clearly
show it as deprecated.

Then pass the parameter deprecated=True to Query
'''
from typing import Optional
from fastapi import FastAPI, Query

app = FastAPI()


@app.get("/items/")
async def read_items(
    q: Optional[str] = Query(
        None,
        alias="item-query",
        title="Query string",
        description="Query string for the items to search in the database that have a good match",
        min_length=3,
        max_length=50,
        regex="^fixedquery$",
        deprecated=True,
    )
):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results

'''
Recap

You can declare additional validations and metadata for your parameters.

Generic validations and metadata:

    alias
    title
    description
    deprecated

Validations specific for strings:

    min_length
    max_length
    regex

In these examples you saw how to declare validations for str values.
'''
