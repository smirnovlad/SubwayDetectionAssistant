import shutil
from fastapi import FastAPI, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware
from pathlib import Path
from io import BytesIO
from fastapi.responses import StreamingResponse
import asyncio

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

UPLOADED_VIDEO_FOLDER = Path("uploads/")


@app.post("/upload")
async def upload(video: UploadFile = File(), mode: str = Form(), fps: int = Form()):
    print(f"Mode: {mode}, FPS: {fps}")
    uploaded_video_path = UPLOADED_VIDEO_FOLDER / video.filename

    print("File path: ", uploaded_video_path)

    with uploaded_video_path.open("wb") as uploaded_file:
        shutil.copyfileobj(video.file, uploaded_file)

    process_video_task = asyncio.create_task(process_video(path_to_file=uploaded_video_path, mode=mode, fps=fps))
    await process_video_task
    processed_video_path = process_video_task.result()
    print("Processed video path: ", processed_video_path)

    with processed_video_path.open("rb") as processed_video:
        content = processed_video.read()
        content_stream = BytesIO(content)
        return StreamingResponse(content_stream, media_type="video/mp4", headers={
            "Content-Disposition": f"filename={video.filename}"})
