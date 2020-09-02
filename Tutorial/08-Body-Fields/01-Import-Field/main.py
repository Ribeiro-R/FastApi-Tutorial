'''The same way you can declare additional validation and metadata
in path operation function parameters with Query, Path and Body, you
can declare validation and metadata inside of Pydantic models using
Pydantic's Field'''

from typing import Optional
from fastapi import Body, FastAPI
from pydantic import BaseModel, Field

app = FastAPI()


class Item(BaseModel):
    name: str
    # You can then use Field with model attributes
    description: Optional[str] = Field(None,
                                       title="The description of the item",
                                       max_length=300)
    price: float = Field(...,
                         gt=0,
                         description="The price must be greater than zero")
    tax: Optional[float] = None


@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item = Body(..., embed=True)):
    results = {"item_id": item_id, "item": item}
    return results

'''Notice that Field is imported directly from pydantic,
not from fastapi as are all the rest (Query, Path, Body, etc)

Field works the same way as Query, Path and Body,
it has all the same parameters, etc.

Technical Details

Actually, Query, Path and others you'll see next create
objects of subclasses of a common Param class, which is
itself a subclass of Pydantic's FieldInfo class.

And Pydantic's Field returns an instance of FieldInfo as well.

Body also returns objects of a subclass of FieldInfo directly.
And there are others you will see later that are subclasses of
the Body class.

Remember that when you import Query, Path, and others from fastapi,
those are actually functions that return special classes.

Tip

Notice how each model's attribute with a type, default value and
Field has the same structure as a path operation function's parameter,
with Field instead of Path, Query and Body.'''
