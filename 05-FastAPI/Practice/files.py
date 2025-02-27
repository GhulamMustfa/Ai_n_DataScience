# poetry add python-multipart
from fastapi import FastAPI, File, UploadFile # type: ignore
from fastapi.staticfiles import StaticFiles # type: ignore

import shutil
import os

UPLOAD_FOLDER = "05-FastAPI\Practice"  # Define the folder to store uploaded files

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

app = FastAPI()

# Mount the uploads folder to serve static files
app.mount("/static", StaticFiles(directory=UPLOAD_FOLDER), name="static")

@app.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    file_path = os.path.join(UPLOAD_FOLDER, file.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Return the public URL to access the file
    file_url = f"/static/{file.filename}"

    return {"filename": file.filename, "file_url": file_url}
