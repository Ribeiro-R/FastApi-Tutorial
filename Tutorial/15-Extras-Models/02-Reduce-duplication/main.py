from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel, EmailStr

'''
Reduce duplication

Reducing code duplication is one of the core ideas in FastAPI.

As code duplication increments the chances of bugs, security issues,
code desynchronization issues (when you update in one place but not
in the others), etc.

And these models are all sharing a lot of the data and duplicating
attribute names and types.

We could do better.

We can declare a UserBase model that serves as a base for our other models.
And then we can make subclasses of that model that inherit its attributes
(type declarations, validation, etc).

All the data conversion, validation, documentation, etc.
will still work as normally.

That way, we can declare just the differences between the models
(with plaintext password, with hashed_password and without password)
'''
app = FastAPI()


class UserModel(BaseModel):
    username: str
    email: EmailStr
    full_name: Optional[str] = None


class UserIn(UserModel):
    password: str


class UserOut(UserModel):
    pass


class UserInDB(UserModel):
    hashed_password: str


def fake_password_hasher(raw_password: str):
    return "supersecret" + raw_password


def fake_save_user(user_in: UserIn):
    hashed_password = fake_password_hasher(user_in.password)
    user_in_db = UserInDB(**user_in.dict(), hashed_password=hashed_password)
    print("User saved! ..not really")
    return user_in_db


@app.post("/user/", response_model=UserOut)
async def create_user(user_in: UserIn):
    user_saved = fake_save_user(user_in)
    return user_saved
