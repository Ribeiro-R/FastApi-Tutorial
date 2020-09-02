'''
The same way you can declare more validations and metadata
for query parameters with Query, you can declare the same
type of validations and metadata for path parameters with Path

Import Path¶

First, import Path from fastapi
'''
from typing import Optional
from fastapi import FastAPI, Path, Query

app = FastAPI()

'''
Declare metadata

You can declare all the same parameters as for Query.

For example, to declare a title metadata value for the
path parameter item_id
'''


@app.get("/items/{item_id}")
async def read_items(item_id: int = Path(...,
                                         title="The ID of the item to get"),
                     q: Optional[str] = Query(None, alias="item-query"),):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results

'''


Note

A path parameter is always required as it has to be part of the path.

So, you should declare it with ... to mark it as required.

Nevertheless, even if you declared it with None or set a default value,
it would not affect anything, it would still be always required.
'''
