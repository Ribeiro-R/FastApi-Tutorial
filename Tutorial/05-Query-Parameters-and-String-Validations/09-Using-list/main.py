'''You can also use list directly instead of List[str]'''
from fastapi import FastAPI, Query

app = FastAPI()


@app.get("/items/")
async def read_items(q: list = Query([])):
    query_items = {"q": q}
    return query_items

'''
Note

Have in mind that in this case,
FastAPI won't check the contents of the list.

For example, List[int] would check (and document)
that the contents of the list are integers. But list alone wouldn't.
'''
