'''
In some cases you don't really need the return value of a
dependency inside your path operation function.

Or the dependency doesn't return a value.

But you still need it to be executed/solved.

For those cases, instead of declaring a path operation function
parameter with Depends, you can add a list of dependencies to the
path operation decorator.

Add dependencies to the path operation decorator

The path operation decorator receives an optional argument dependencies.

It should be a list of Depends()
'''
from fastapi import Depends, FastAPI, Header, HTTPException

app = FastAPI()


async def verify_token(x_token: str = Header(...)):
    if x_token != "fake-super-secret-token":
        raise HTTPException(status_code=400, detail="X-Token header invalid")


async def verify_key(x_key: str = Header(...)):
    if x_key != "fake-super-secret-key":
        raise HTTPException(status_code=400, detail="X-Key header invalid")
    return x_key


@app.get("/items/", dependencies=[Depends(verify_token), Depends(verify_key)])
async def read_items():
    return [{"item": "Foo"}, {"item": "Bar"}]

'''
These dependencies will be executed/solved the same way normal dependencies.
But their value (if they return any) won't be passed to your path operation
function.

Tip

Some editors check for unused function parameters, and show them as errors.

Using these dependencies in the path operation decorator you can make sure
they are executed while avoiding editor/tooling errors.

It might also help avoid confusion for new developers that see an
unused parameter in your code and could think it's unnecessary.

Dependencies errors and return values

You can use the same dependency functions you use normally.

Dependency requirements

They can declare request requirements (like headers) or other sub-dependencies:

async def verify_token(x_token: str = Header(...)):
async def verify_key(x_key: str = Header(...)):

Raise exceptions¶

These dependencies can raise exceptions, the same as normal dependencies:

raise HTTPException(status_code=400, detail="X-Token header invalid")
raise HTTPException(status_code=400, detail="X-Key header invalid")

Return values

And they can return values or not, the values won't be used.

So, you can re-use a normal dependency (that returns a value)
you already use somewhere else, and even though the value won't
be used, the dependency will be executed.

Dependencies for a group of path operations

Later, when reading about how to structure bigger applications
(Bigger Applications - Multiple Files), possibly with multiple files,
you will learn how to declare a single dependencies parameter for a
group of path operations.
'''
