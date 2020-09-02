from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel, EmailStr
'''
Continuing with the previous example, it will be common
to have more than one related model.

This is especially the case for user models, because:

    The input model needs to be able to have a password.
    The output model should not have a password.
    The database model would probably need to have a hashed password.

Danger

Never store user's plaintext passwords. Always store a
"secure hash" that you can then verify.

If you don't know, you will learn what a "password hash"
is in the security chapters
'''

'''
Here's a general idea of how the models could look like with their
password fields and the places where they are used:'''

app = FastAPI()


class UserIn(BaseModel):
    username: str
    password: str
    email: EmailStr
    full_name: Optional[str] = None


class UserOut(BaseModel):
    username: str
    email: EmailStr
    full_name: Optional[str] = None


class UserInDB(BaseModel):
    username: str
    hashed_password: str
    email: EmailStr
    full_name: Optional[str] = None


def fake_password_hasher(raw_password: str):
    return "supersecret"+raw_password


def fake_save_user(user_in: UserIn):
    hashed_password = fake_password_hasher(user_in.password)
    user_in_db = UserInDB(**user_in.dict(), hashed_password=hashed_password)
    print("User saved! ..not realy")
    return user_in_db


@app.post("/user/", response_model=UserOut)
async def create_user(user_in: UserIn):
    user_saved = fake_save_user(user_in)
    return user_saved

'''
About **user_in.dict()
Pydantic's .dict()

user_in is a Pydantic model of class UserIn.

Pydantic models have a .dict() method that
returns a dict with the model's data.

So, if we create a Pydantic object user_in like:

user_in = UserIn(username="john",
                 password="secret",
                 email="john.doe@example.com")

and then we call:

user_dict = user_in.dict()

we now have a dict with the data in the variable
user_dict (it's a dict instead of a Pydantic model object).

And if we call:

print(user_dict)

we would get a Python dict with:

{
    'username': 'john',
    'password': 'secret',
    'email': 'john.doe@example.com',
    'full_name': None,
}

Unwrapping a dict

If we take a dict like user_dict and pass it to a function (or class)
with **user_dict, Python will "unwrap" it. It will pass the keys and
values of the user_dict directly as key-value arguments.

So, continuing with the user_dict from above, writing:

UserInDB(**user_dict)

Would result in something equivalent to:

UserInDB(
    username="john",
    password="secret",
    email="john.doe@example.com",
    full_name=None,
)

Or more exactly, using user_dict directly,
with whatever contents it might have in the future:

UserInDB(
    username = user_dict["username"],
    password = user_dict["password"],
    email = user_dict["email"],
    full_name = user_dict["full_name"],
)

A Pydantic model from the contents of another

As in the example above we got user_dict from user_in.dict(), this code:

user_dict = user_in.dict()
UserInDB(**user_dict)

would be equivalent to:

UserInDB(**user_in.dict())

...because user_in.dict() is a dict, and then we make Python
"unwrap" it by passing it to UserInDB prepended with **.

So, we get a Pydantic model from the data in another Pydantic model.
Unwrapping a dict and extra keywords

And then adding the extra keyword argument hashed_password=hashed_password,
like in:

UserInDB(**user_in.dict(), hashed_password=hashed_password)

...ends up being like:

UserInDB(
    username = user_dict["username"],
    password = user_dict["password"],
    email = user_dict["email"],
    full_name = user_dict["full_name"],
    hashed_password = hashed_password,
)

Warning

The supporting additional functions are just to demo a possible flow
of the data, but they of course are not providing any real security.
'''
