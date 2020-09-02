'''
201 is the status code for "Created".

But you don't have to memorize what each of these codes mean.

You can use the convenience variables from fastapi.status.
'''
from fastapi import FastAPI, status

app = FastAPI()


@app.post("/items/", status_code=status.HTTP_201_CREATED)
async def create_item(name: str):
    return {"name": name}

'''
Technical Details

You could also use from starlette import status.

FastAPI provides the same starlette.status as fastapi.status
just as a convenience for you, the developer. But it comes
directly from Starlette.
'''
