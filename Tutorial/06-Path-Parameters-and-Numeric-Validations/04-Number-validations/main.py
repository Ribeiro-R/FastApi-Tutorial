from fastapi import FastAPI, Path

app = FastAPI()


'''
Greater than or equal

With Query and Path (and other's you'll see later)
you can declare string constraints, but also number constraints.

Here, with ge=1, item_id will need to be an
integer number "greater than or equal" to 1.
'''


@app.get("/items/{item_id}")
async def read_items(*,
                     item_id: int = Path(...,
                                         title="The ID of the item to get",
                                         ge=1),
                     q: str):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results

'''
Greater than and less than or equal

The same applies for:

    gt: greater than
    le: less than or equal

'''


@app.get("/items/{item_id}")
async def read_items(
    *,
    item_id: int = Path(..., title="The ID of the item to get", gt=0, le=1000),
    q: str,
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results

'''
Floats, greater than and less than

Number validations also work for float values.

Here's where it becomes important to be able to
declare gt and not just ge. As with it you can
require, for example, that a value must be greater
than 0, even if it is less than 1.

So, 0.5 would be a valid value. But 0.0 or 0 would not.

And the same for lt
'''


@app.get("/items/{item_id}")
async def read_items(
    *,
    item_id: int = Path(..., title="The ID of the item to get", ge=0, le=1000),
    q: str,
    size: float = Query(..., gt=0, lt=10.5)
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results

'''
Recap

With Query, Path (and others you haven't seen yet)
you can declare metadata and string validations in
the same ways as with Query Parameters and String Validations.

And you can also declare numeric validations:

    gt: greater than
    ge: greater than or equal
    lt: less than
    le: less than or equal

'''
