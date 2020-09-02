'''
You can define extra information to go in JSON Schema.

A common use case is to add an example that will be shown in the docs.

There are several ways you can declare extra JSON Schema information.

Pydantic schema_extra

You can declare an example for a Pydantic model using Config
and schema_extra, as described in Pydantic's docs: Schema customization.

'''
from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None

    class Config:
        schema_extra = {"example": {"name": "Foo",
                                    "description": "A very nice Item",
                                    "price": 35.4,
                                    "tax": 3.2,
                                    }
                        }


@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    results = {"item_id": item_id, "item": item}
    return results
# That extra info will be added as-is to the output JSON Schema.
