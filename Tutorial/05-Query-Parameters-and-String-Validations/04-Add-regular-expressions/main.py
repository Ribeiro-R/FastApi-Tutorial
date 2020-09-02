'''You can define a regular expression that the parameter should match'''
from typing import Optional
from fastapi import FastAPI, Query

app = FastAPI()


@app.get("/items/")
async def read_items(q: Optional[str] = Query(None,
                                              min_length=3,
                                              max_length=50,
                                              regex="^fixedquery$")):
    results = {"items": [{"item_id": "Foo"},
                         {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results

'''
This specific regular expression checks that the received parameter value:

    ^: starts with the following characters, doesn't have characters before.
    fixedquery: has the exact value fixedquery.
    $: ends there, doesn't have any more characters after fixedquery.

If you feel lost with all these "regular expression" ideas, don't worry.
They are a hard topic for many people. You can still do a lot of stuff
without needing regular expressions yet.

But whenever you need them and go and learn them,
know that you can already use them directly in FastAPI.
'''
