from typing import Dict
from fastapi import FastAPI
'''
You can also declare a response using a plain arbitrary dict,
declaring just the type of the keys and values, without using
a Pydantic model.

This is useful if you don't know the valid field/attribute names
(that would be needed for a Pydantic model) beforehand.

In this case, you can use typing.Dict
'''
app = FastAPI()


@app.get("/keyword-weights/", response_model=Dict[str, float])
async def read_keyword_weights():
    return {"foo": 2.3, "bar": 3.4}
