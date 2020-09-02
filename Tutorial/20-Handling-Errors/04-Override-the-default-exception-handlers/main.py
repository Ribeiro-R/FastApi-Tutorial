'''
FastAPI has some default exception handlers.

These handlers are in charge of returning the default JSON responses when you
raise an HTTPException and when the request has invalid data.

You can override these exception handlers with your own.

Override request validation exceptions

When a request contains invalid data, FastAPI internally raises a
RequestValidationError.

And it also includes a default exception handler for it.

To override it, import the RequestValidationError and use it with
@app.exception_handler(RequestValidationError) to decorate the
exception handler.

The exception handler will receive a Request and the exception.
'''
from fastapi import FastAPI, HTTPException
from fastapi.exceptions import RequestValidationError
from fastapi.responses import PlainTextResponse
from starlette.exceptions import HTTPException as StarletteHTTPException

app = FastAPI()


@app.exception_handler(StarletteHTTPException)
async def http_exception_handler(request, exc):
    return PlainTextResponse(str(exc.detail), status_code=exc.status_code)


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
    return PlainTextResponse(str(exc), status_code=400)


@app.get("/items/{item_id}")
async def read_item(item_id: int):
    if item_id == 3:
        raise HTTPException(status_code=418, detail="Nope! I don't like 3.")
    return {"item_id": item_id}

'''
Now, if you go to /items/foo, instead of getting the default JSON error with:

{
    "detail": [
        {
            "loc": [
                "path",
                "item_id"
            ],
            "msg": "value is not a valid integer",
            "type": "type_error.integer"
        }
    ]
}

you will get a text version, with:

1 validation error
path -> item_id
  value is not a valid integer (type=type_error.integer)

RequestValidationError vs ValidationError

Warning

These are technical details that you might skip if it's
not important for you now.

RequestValidationError is a sub-class of Pydantic's ValidationError.

FastAPI uses it so that, if you use a Pydantic model in response_model,
and your data has an error, you will see the error in your log.

But the client/user will not see it. Instead, the client will receive an
"Internal Server Error" with a HTTP status code 500.

It should be this way because if you have a Pydantic ValidationError in your
response or anywhere in your code (not in the client's request), it's actually
a bug in your code.

And while you fix it, your clients/users shouldn't have access to internal
information about the error, as that could expose a security vulnerability.
'''
'''
Override the HTTPException error handler

The same way, you can override the HTTPException handler.

For example, you could want to return a plain text response instead of
JSON for these errors.

Technical Details

You could also use from starlette.responses import PlainTextResponse.

FastAPI provides the same starlette.responses as fastapi.responses just as a
convenience for you, the developer. But most of the available responses come
directly from Starlette.
'''
