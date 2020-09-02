'''
Multiple path and query parameters

You can declare multiple path parameters and query parameters at the same time,
FastAPI knows which is which.

And you don't have to declare them in any specific order.

They will be detected by name.
'''
from typing import Optional
from fastapi import FastAPI

app = FastAPI()


@app.get("/users/{user_id}/items/{item_id}")
async def read_user_item(user_id: int,
                         item_id: str,
                         q: Optional[str] = None,
                         short: bool = False):
    item = {"item_id": item_id, "owner_id": user_id}
    if q:
        item.update({"q": q})
    if not short:
        text = "This is an amazing item that has a long description"
        item.update(
            {"description": text}
        )
    return item
