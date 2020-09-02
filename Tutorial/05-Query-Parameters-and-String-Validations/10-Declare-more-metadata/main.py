'''
You can add more information about the parameter.

That information will be included in the generated
OpenAPI and used by the documentation user interfaces
and external tools.

Note
Have in mind that different tools might have
different levels of OpenAPI support.
Some of them might not show all the extra
information declared yet, although in most
of the cases, the missing feature is already
planned for development.
'''
# You can add a title and a description
from typing import Optional
from fastapi import FastAPI, Query

app = FastAPI()


@app.get("/items/")
async def read_items(q: Optional[str] = Query(None,
                                              title="Query string",
                                              description="Query string for the items to search in the database that have a good match",
                                              min_length=3,)):
    results = {"items": [{"item_id": "Foo"},
                         {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results
