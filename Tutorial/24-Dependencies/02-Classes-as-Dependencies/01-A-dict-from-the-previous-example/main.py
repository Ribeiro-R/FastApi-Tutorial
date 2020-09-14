'''
Before diving deeper into the Dependency Injection system,
let's upgrade the previous example.

A dict from the previous example

In the previous example, we were returning a
dict from our dependency ("dependable")
'''

from typing import Optional
from fastapi import Depends, FastAPI

app = FastAPI()


async def common_parameters(q: Optional[str] = None,
                            skip: int = 0,
                            limit: int = 100):
    return {"q": q, "skip": skip, "limit": limit}


@app.get("/items/")
async def read_items(commons: dict = Depends(common_parameters)):
    return commons


@app.get("/users/")
async def read_users(commons: dict = Depends(common_parameters)):
    return commons

'''
But then we get a dict in the parameter commons of the path operation function.

And we know that editors can't provide a lot of support (like completion)
for dicts, because they can't know their keys and value types.

We can do better...

What makes a dependency

Up to now you have seen dependencies declared as functions.

But that's not the only way to declare dependencies
(although it would probably be the more common).

The key factor is that a dependency should be a "callable".

A "callable" in Python is anything that Python can "call" like a function.

So, if you have an object something (that might not be a function)
and you can "call" it (execute it) like:

something()

or

something(some_argument, some_keyword_argument="foo")

then it is a "callable".
'''
