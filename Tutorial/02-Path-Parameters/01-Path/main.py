from fastapi import FastAPI

app = FastAPI()

# You can declare path "parameters" or "variables"
# with the same syntax used by Python format strings:

# The value of the path parameter item_id will be passed to
# your function as the argument item_id

# So, if you run this example and go to http://127.0.0.1:8000/items/foo,
# you will see a response of: {"item_id":"foo"}


# @app.get("/items/{item_id}")
# async def read_item(item_id):
#     return {"item_id": item_id}


# Path parameters with types
# You can declare the type of a path parameter in the function,
# using standard Python type annotations:

# In this case, item_id is declared to be an int.
#  Example 1 http://127.0.0.1:8000/items/3
#  Example 2 http://127.0.0.1:8000/items/foo
@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}
