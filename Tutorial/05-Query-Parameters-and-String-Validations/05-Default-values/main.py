'''
The same way that you can pass None as the first argument to be
used as the default value, you can pass other values.

Let's say that you want to declare the q query parameter to have
a min_length of 3, and to have a default value of "fixedquery"
'''
from fastapi import FastAPI, Query

app = FastAPI()


@app.get("/items/")
async def read_items(q: str = Query("fixedquery", min_length=3)):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results

'''
Note

Having a default value also makes the parameter optional.
'''
