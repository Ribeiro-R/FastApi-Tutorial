# FastAPI is a Python class that provides all the functionality for your API.
from fastapi import FastAPI

#  create a FastAPI "instance"
app = FastAPI()
# Here the app variable will be an "instance" of the class FastAPI.
# This will be the main point of interaction to create all your API.
# This app is the same one referred by uvicorn in the command:


@app.get("/")
async def root():
    return {"message": "Hello World"}

'''
Note

The command uvicorn main:app refers to:

    * main: the file main.py (the Python "module").
    * app: the object created inside of main.py with the line app = FastAPI().
    * --reload: make the server restart after code changes.
      Only use for development.

INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)

Interactive API docs

Now go to http://127.0.0.1:8000/docs.

You will see the automatic interactive API documentation
(provided by Swagger UI).

Alternative API docs

And now, go to http://127.0.0.1:8000/redoc.

You will see the alternative automatic documentation (provided by ReDoc).

'''

'''
Path

"Path" here refers to the last part of the URL starting from the first /.

So, in a URL like:

https://example.com/items/foo

...the path would be:

/items/foo

While building an API, the "path" is the main way to separate "concerns"
and "resources".
Operation

"Operation" here refers to one of the HTTP "methods".

One of:

    POST
    GET
    PUT
    DELETE

...and the more exotic ones:

    OPTIONS
    HEAD
    PATCH
    TRACE

In the HTTP protocol, you can communicate to each path using one
(or more) of these "methods".

When building APIs, you normally use these specific HTTP methods
to perform a specific action.

Normally you use:

    POST: to create data.
    GET: to read data.
    PUT: to update data.
    DELETE: to delete data.

So, in OpenAPI, each of the HTTP methods is called an "operation".

We are going to call them "operations" too.
Define a path operation decorator

@app.get("/")
async def root():
    return {"message": "Hello World"}

The @app.get("/") tells FastAPI that the function right below is
in charge of handling requests that go to:

    the path /
    using a get operation

A "decorator" takes the function below and does something with it.

In our case, this decorator tells FastAPI that the function below
corresponds to the path / with an operation get.

It is the "path operation decorator".

You can also use the other operations:

    @app.post()
    @app.put()
    @app.delete()

And the more exotic ones:

    @app.options()
    @app.head()
    @app.patch()
    @app.trace()

Path operation function

This is our "path operation function":

    path: is /.
    operation: is get.
    function: is the function below the "decorator" (below @app.get("/")).

@app.get("/")
async def root():
    return {"message": "Hello World"}

This is a Python function.

It will be called by FastAPI whenever it receives a request to the URL "/"
using a GET operation.

In this case, it is an async function.

You could also define it as a normal function instead of async def:

@app.get("/")
def root():
    return {"message": "Hello World"}

Return the content

@app.get("/")
async def root():
    return {"message": "Hello World"}

You can return a dict, list, singular values as str, int, etc.

You can also return Pydantic models

'''
