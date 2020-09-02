
from fastapi import FastAPI

'''
When you declare other function parameters that are not part
of the path parameters, they are automatically interpreted as
"query" parameters.
'''

'''
The query is the set of key-value pairs that go after
the ? in a URL, separated by & characters.

For example, in the url:

http://127.0.0.1:8000/items/?skip=0&limit=10
'''

app = FastAPI()

fake_items_db = [{"item_name": "Foo"},
                 {"item_name": "Bar"},
                 {"item_name": "Baz"}]


@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):
    return fake_items_db[skip: skip + limit]

'''
...the query parameters are:

    skip: with a value of 0
    limit: with a value of 10

As they are part of the URL, they are "naturally" strings.

But when you declare them with Python types (in the example above, as int),
they are converted to that type and validated against it.

All the same process that applied for path parameters
also applies for query parameters:

    Editor support (obviously)
    Data "parsing"
    Data validation
    Automatic documentation

'''

'''
Defaults

As query parameters are not a fixed part of a path, they can be optional
and can have default values.

In the example above they have default values of skip=0 and limit=10.

So, going to the URL:

http://127.0.0.1:8000/items/

would be the same as going to:

http://127.0.0.1:8000/items/?skip=0&limit=10

But if you go to, for example:

http://127.0.0.1:8000/items/?skip=20

The parameter values in your function will be:

    skip=20: because you set it in the URL
    limit=10: because that was the default value

'''
