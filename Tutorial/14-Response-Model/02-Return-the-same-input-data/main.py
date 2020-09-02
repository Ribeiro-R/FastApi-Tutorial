'''
Here we are declaring a UserIn model, it will contain a plaintext password
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


# Don't do this in production!
# And we are using this model to declare our
# input and the same model to declare our output:
@app.post("/user/", response_model=UserIn)
async def create_user(user: UserIn):
    return user

'''
Now, whenever a browser is creating a user with a
password, the API will return the same password in the response.

In this case, it might not be a problem, because the user himself
is sending the password.

But if we use the same model for another path operation, we could
be sending our user's passwords to every client.

Danger

Never store the plain password of a user or send it in a response.

'''
