'''
When you define a query parameter explicitly with Query you can also
declare it to receive a list of values, or said in other way, to receive
multiple values.

For example, to declare a query parameter q that can appear
multiple times in the URL, you can write
'''
from typing import List, Optional
from fastapi import FastAPI, Query

app = FastAPI()


@app.get("/items/")
async def read_items(q: Optional[List[str]] = Query(None)):
    query_items = {"q": q}
    return query_items
'''
Then, with a URL like:

http://localhost:8000/items/?q=foo&q=bar

you would receive the multiple q query parameters' values
(foo and bar) in a Python list inside your path operation
function, in the function parameter q

Tip

To declare a query parameter with a type of list,
like in the example above, you need to explicitly
use Query, otherwise it would be interpreted as a request body.
'''
