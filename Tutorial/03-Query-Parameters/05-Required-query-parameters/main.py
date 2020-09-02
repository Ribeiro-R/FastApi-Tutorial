'''
Required query parameters

When you declare a default value for non-path parameters
(for now, we have only seen query parameters), then it is not required.

If you don't want to add a specific value but just make it optional,
set the default as None.

But when you want to make a query parameter required, you can just not
declare any default value.
'''
from fastapi import FastAPI

app = FastAPI()


@app.get("/items/{item_id}")
async def read_user_item(item_id: str, needy: str):
    item = {"item_id": item_id, "needy": needy}
    return item

'''
Here the query parameter needy is a required query parameter of type str.

If you open in your browser a URL like:

http://127.0.0.1:8000/items/foo-item

...without adding the required parameter needy, you will see an error

As needy is a required parameter, you would need to set it in the URL:

http://127.0.0.1:8000/items/foo-item?needy=sooooneedy

...this would work

And of course, you can define some parameters as required,
some as having a default value, and some entirely optional:

from typing import Optional

from fastapi import FastAPI

app = FastAPI()


@app.get("/items/{item_id}")
async def read_user_item(
    item_id: str, needy: str, skip: int = 0, limit: Optional[int] = None
):
    item = {"item_id": item_id, "needy": needy, "skip": skip, "limit": limit}
    return item

In this case, there are 3 query parameters:

    needy, a required str.
    skip, an int with a default value of 0.
    limit, an optional int.

Tip

You could also use Enums the same way as with Path Parameters
'''
