'''You can also declare a body as a dict with
keys of some type and values of other type.

Without having to know beforehand what are
the valid field/attribute names (as would
be the case with Pydantic models).

This would be useful if you want to receive
keys that you don't already know.

-------------------------------------------

Other useful case is when you want to have
keys of other type, e.g. int.

That's what we are going to see here.

In this case, you would accept any dict as
long as it has int keys with float values:
'''

from typing import Dict
from fastapi import FastAPI

app = FastAPI()


@app.post("/index-weights/")
async def create_index_weights(weights: Dict[int, float]):
    return weights

'''
Tip

Have in mind that JSON only supports str as keys.

But Pydantic has automatic data conversion.

This means that, even though your API clients can only
send strings as keys, as long as those strings contain
pure integers, Pydantic will convert them and validate them.

And the dict you receive as weights will actually have int keys
and float values.
'''
