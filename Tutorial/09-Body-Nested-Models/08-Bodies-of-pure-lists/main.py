'''If the top level value of the JSON body you expect is a JSON array
(a Python list), you can declare the type in the parameter of the
function, the same as in Pydantic models:

images: List[Image]'''

from typing import List
from fastapi import FastAPI
from pydantic import BaseModel, HttpUrl

app = FastAPI()


class Image(BaseModel):
    url: HttpUrl
    name: str


@app.post("/images/multiple/")
async def create_multiple_images(images: List[Image]):
    return images
