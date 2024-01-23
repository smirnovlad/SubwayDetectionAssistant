import shutil
from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse, FileResponse
from pathlib import Path
from io import BytesIO

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

import time

# uploads_directory = Path("uploads/")


@app.post("/upload")
def upload(video: UploadFile = File()):
    content = video.file.read()

    content_stream = BytesIO(content)
    # Дополнительные действия с контентом, если необходимо

    return StreamingResponse(content_stream, media_type=video.headers['content-type'], headers={
        "Content-Disposition": f"filename={video.filename}"})