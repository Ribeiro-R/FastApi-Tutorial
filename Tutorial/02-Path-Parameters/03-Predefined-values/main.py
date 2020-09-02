"""
Predefined values

If you have a path operation that receives a path parameter,
but you want the possible valid path parameter values to be
predefined, you can use a standard Python Enum.

Create an Enum class

Import Enum and create a sub-class that inherits from str and from Enum.

By inheriting from str the API docs will be able to know that the values
must be of type string and will be able to render correctly.

Then create class attributes with fixed values,
which will be the available valid values:
"""

from enum import Enum
from fastapi import FastAPI


class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"


app = FastAPI()


# Create a path parameter with a type annotation using the enum class
@app.get("/model/{model_name}")
async def get_model(model_name: ModelName):
    # The value of the path parameter will be an enumeration member.
    # Compare it with the enumeration member in your created enum ModelName.
    if model_name == ModelName.alexnet:
        return {"model_name": model_name,
                "message": "Deep Learning FTW!"}
    # Get the actual value (a str in this case) using model_name.value
    if model_name.value == "lenet":
        return {"model_name": model_name,
                "message": "LeCNN all the images"}

    return {"model_name": model_name,
            "message": "Have some residuals"}
