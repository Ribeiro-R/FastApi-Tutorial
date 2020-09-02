'''
There are many situations in where you need to notify an error to a client
that is using your API.

This client could be a browser with a frontend, a code from someone else,
an IoT device, etc.

You could need to tell the client that:

    * The client doesn't have enough privileges for that operation.
    * The client doesn't have access to that resource.
    * The item the client was trying to access doesn't exist.
    * etc.

In these cases, you would normally return an HTTP status code in the
range of 400 (from 400 to 499).

This is similar to the 200 HTTP status codes (from 200 to 299). Those "200"
status codes mean that somehow there was a "success" in the request.

The status codes in the 400 range mean that there was an error from the client.

To return HTTP responses with errors to the client you use HTTPException.
'''
from fastapi import FastAPI, HTTPException

app = FastAPI()

items = {"foo": "The Foo Wrestlers"}


@app.get("/items/{item_id}")
async def read_item(item_id: str):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"item": items[item_id]}

'''
Raise an HTTPException in your code

HTTPException is a normal Python exception with additional data
relevant for APIs.

Because it's a Python exception, you don't return it, you raise it.

This also means that if you are inside a utility function that you are calling
inside of your path operation function, and you raise the HTTPException from
inside of that utility function, it won't run the rest of the code in the path
operation function, it will terminate that request right away and send the
HTTP error from the HTTPException to the client.

The benefit of raising an exception over returning a value will be more
evident in the section about Dependencies and Security.

In this example, when the client request an item by an ID that doesn't exist,
raise an exception with a status code of 404.

The resulting response

If the client requests http://example.com/items/foo (an item_id "foo"),
that client will receive an HTTP status code of 200, and a JSON response of:

{
  "item": "The Foo Wrestlers"
}

But if the client requests http://example.com/items/bar (a non-existent
item_id "bar"), that client will receive an HTTP status code of 404 (the
"not found" error), and a JSON response of:

{
  "detail": "Item not found"
}

Tip

When raising an HTTPException, you can pass any value that can be converted
to JSON as the parameter detail, not only str.

You could pass a dict, a list, etc.

They are handled automatically by FastAPI and converted to JSON.
'''
