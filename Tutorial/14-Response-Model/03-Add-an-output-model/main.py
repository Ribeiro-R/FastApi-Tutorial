'''
We can instead create an input model with the plaintext password
and an output model without it
'''
from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel, EmailStr

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


@app.post("/user/", response_model=UserOut)
async def create_user(user: UserIn):
    return user
'''
Here, even though our path operation
function is returning the same input
user that contains the password

we declared the response_model to be
our model UserOut, that doesn't include
the password

So, FastAPI will take care of filtering
out all the data that is not declared in
the output model (using Pydantic).
'''
