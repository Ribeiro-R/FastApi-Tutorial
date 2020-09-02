'''define a default list of values if none are provided'''
from typing import List
from fastapi import FastAPI, Query

app = FastAPI()


@app.get("/items/")
async def read_items(q: List[str] = Query(["foo", "bar"])):
    query_items = {"q": q}
    return query_items
'''
If you go to:

http://localhost:8000/items/

the default of q will be: ["foo", "bar"]
'''
