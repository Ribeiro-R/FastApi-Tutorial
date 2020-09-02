'''
The RequestValidationError contains the body it received with invalid data.

You could use it while developing your app to log the body and debug it,
return it to the user, etc.
'''
from fastapi import FastAPI, Request, status
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from pydantic import BaseModel

app = FastAPI()


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request,
                                       exc: RequestValidationError):
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content=jsonable_encoder({"detail": exc.errors(), "body": exc.body}),
    )


class Item(BaseModel):
    title: str
    size: int


@app.post("/items/")
async def create_item(item: Item):
    return item

'''
Now try sending an invalid item like:

{
  "title": "towel",
  "size": "XL"
}

You will receive a response telling you that the data is invalid
containing the received body:

{
  "detail": [
    {
      "loc": [
        "body",
        "size"
      ],
      "msg": "value is not a valid integer",
      "type": "type_error.integer"
    }
  ],
  "body": {
    "title": "towel",
    "size": "XL"
  }
}
'''
'''
FastAPI's HTTPException vs Starlette's HTTPException

FastAPI has its own HTTPException.

And FastAPI's HTTPException error class inherits from Starlette's
HTTPException error class.

The only difference, is that FastAPI's HTTPException allows you to add headers
to be included in the response.

This is needed/used internally for OAuth 2.0 and some security utilities.

So, you can keep raising FastAPI's HTTPException as normally in your code.

But when you register an exception handler, you should register it for
Starlette's HTTPException.

This way, if any part of Starlette's internal code, or a Starlette extension
or plug-in, raises a Starlette HTTPException, your handler will be able to
catch and handle it.

In this example, to be able to have both HTTPExceptions in the same code,
Starlette's exceptions is renamed to StarletteHTTPException:

from starlette.exceptions import HTTPException as StarletteHTTPException
'''
