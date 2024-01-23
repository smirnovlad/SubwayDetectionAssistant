import shutil
from fastapi import FastAPI, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware
from pathlib import Path
from io import BytesIO
from fastapi.responses import StreamingResponse

from processing.processing import process_video

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

uploads_directory = Path("uploads/")


@app.post("/upload")
async def upload(video: UploadFile = File(), fps: int = Form()):
    print("FPS: ", fps)
    input_video_path = uploads_directory / video.filename

    print("File path: ", input_video_path)

    with input_video_path.open("wb") as uploaded_file:
        shutil.copyfileobj(video.file, uploaded_file)

    processed_video_path = process_video(input_video_path, fps)
    print("Processed video path: ", processed_video_path)

    with processed_video_path.open("rb") as processed_video:
        content = processed_video.read()
        content_stream = BytesIO(content)
        return StreamingResponse(content_stream, media_type="video/mp4", headers={
            "Content-Disposition": f"filename={video.filename}"})
    # input_video_path.unlink()
    # processed_video_path.unlink()
