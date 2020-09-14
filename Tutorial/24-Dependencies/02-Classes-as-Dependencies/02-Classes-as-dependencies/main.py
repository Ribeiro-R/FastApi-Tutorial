'''
You might notice that to create an instance of a Python class,
you use that same syntax.

For example:

class Cat:
    def __init__(self, name: str):
        self.name = name


fluffy = Cat(name="Mr Fluffy")

In this case, fluffy is an instance of the class Cat.

And to create fluffy, you are "calling" Cat.

So, a Python class is also a callable.

Then, in FastAPI, you could use a Python class as a dependency.

What FastAPI actually checks is that it is a "callable" (function,
class or anything else) and the parameters defined.

If you pass a "callable" as a dependency in FastAPI, it will analyze
the parameters for that "callable", and process them in the same way
as the parameters for a path operation function. Including sub-dependencies.

That also applies to callables with no parameters at all. The same as it would
be for path operation functions with no parameters.

Then, we can change the dependency "dependable" common_parameters from above
to the class CommonQueryParams
'''
from typing import Optional
from fastapi import FastAPI, Depends

app = FastAPI()

fake_items_db = [
    {"item_name": "Foo"},
    {"item_name": "Bar"},
    {"item_name": "Baz"}
]


class CommonQuerryParams:
    def __init__(self,
                 q: Optional[str] = None,
                 skip: int = 0,
                 limit: int = 100):
        self.q = q
        self.skip = skip
        self.limit = limit


@app.get("/items/")
async def read_items(
    commons: CommonQuerryParams = Depends(CommonQuerryParams)
):
    response = {}
    if commons.q:
        response.update({"q": commons.q})
    items = fake_items_db[commons.skip: commons.skip + commons.limit]
    response.update({"items": items})
    return response
'''
Pay attention to the __init__ method used to create the instance of the class.

...it has the same parameters as our previous common_parameters

Those parameters are what FastAPI will use to "solve" the dependency.

In both cases, it will have:

    * an optional q query parameter.
    * a skip query parameter, with a default of 0.
    * a limit query parameter, with a default of 100.

In both cases the data will be converted, validated,
documented on the OpenAPI schema, etc.

Use it

Now you can declare your dependency using this class.

FastAPI calls the CommonQueryParams class. This creates an "instance"
of that class and the instance will be passed as the parameter commons
to your function.

Type annotation vs Depends

Notice how we write CommonQueryParams twice in the above code:

commons: CommonQueryParams = Depends(CommonQueryParams)

The last CommonQueryParams, in:

... = Depends(CommonQueryParams)

...is what FastAPI will actually use to know what is the dependency.

From it is that FastAPI will extract the declared parameters and that is
what FastAPI will actually call.

In this case, the first CommonQueryParams, in:

commons: CommonQueryParams ...

...doesn't have any special meaning for FastAPI.
FastAPI won't use it fordata conversion, validation, etc.
(as it is using the = Depends(CommonQueryParams) for that).

You could actually write just:

commons = Depends(CommonQueryParams)

..as in:

from typing import Optional

from fastapi import Depends, FastAPI

app = FastAPI()


fake_items_db = [{"item_name": "Foo"},
                 {"item_name": "Bar"},
                 {"item_name": "Baz"}]


class CommonQueryParams:
    def __init__(self,
    q: Optional[str] = None,
    skip: int = 0,
    limit: int = 100
):
        self.q = q
        self.skip = skip
        self.limit = limit


@app.get("/items/")
async def read_items(commons=Depends(CommonQueryParams)):
    response = {}
    if commons.q:
        response.update({"q": commons.q})
    items = fake_items_db[commons.skip : commons.skip + commons.limit]
    response.update({"items": items})
    return response

But declaring the type is encouraged as that way your editor will know what
will be passed as the parameter commons, and then it can help you with code
completion, type checks, etc.
'''
