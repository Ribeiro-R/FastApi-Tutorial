'''
It's possible to upload several files at the same time.

They would be associated to the same "form field" sent using "form data".

To use that, declare a List of bytes or UploadFile.
'''
from typing import List
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import HTMLResponse

app = FastAPI()


@app.post("/files/")
async def create_files(files: List[bytes] = File(...)):
    return {"file_sizes": [len(file) for file in files]}


@app.post("/uploadfiles/")
async def create_upload_files(files: List[UploadFile] = File(...)):
    return {"filenames": [file.filename for file in files]}


@app.get("/")
async def main():
    content = """
<body>
<form action="/files/" enctype="multipart/form-data" method="post">
<input name="files" type="file" multiple>
<input type="submit">
</form>
<form action="/uploadfiles/" enctype="multipart/form-data" method="post">
<input name="files" type="file" multiple>
<input type="submit">
</form>
</body>
    """
    return HTMLResponse(content=content)

'''
You will receive, as declared, a list of bytes or UploadFiles.

Technical Details

You could also use from starlette.responses import HTMLResponse.

FastAPI provides the same starlette.responses as fastapi.responses just as
a convenience for you, the developer. But most of the available responses
come directly from Starlette.
'''
