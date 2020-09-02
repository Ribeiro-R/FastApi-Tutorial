'''
You can define Header parameters the same way you define Query,
Path and Cookie parameters.
'''
from typing import Optional
from fastapi import FastAPI, Header

app = FastAPI()


@app.get("/items/")
async def read_items(user_agent: Optional[str] = Header(None)):
    return {"User-Agent": user_agent}

'''
The header parameters using the same structure as with Path, Query and Cookie.

The first value is the default value, you can pass all the extra validation
or annotation parameters.

Technical Details

Header is a "sister" class of Path, Query and Cookie. It also inherits
from the same common Param class.

But remember that when you import Query, Path, Header, and others
from fastapi, those are actually functions that return special classes.

Info

To declare headers, you need to use Header, because otherwise the parameters
would be interpreted as query parameters.
'''
