"""
Order matters

When creating path operations, you can find situations
where you have a fixed path.

Like /users/me, let's say that it's to get data about the current user.

And then you can also have a path /users/{user_id} to get data about a
specific user by some user ID.

Because path operations are evaluated in order, you need to make sure
that the path for /users/me is declared before the one for /users/{user_id}:
"""

from fastapi import FastAPI

app = FastAPI()


@app.get("/users/me")
async def read_user_me():
    return {"user_id": "the current user"}


@app.get("/users/{user_id}")
async def read_user(user_id: str):
    return {"user_id": user_id}

# Otherwise, the path for /users/{user_id} would match also for /users/me,
# "thinking" that it's receiving a parameter user_id with a value of "me".
