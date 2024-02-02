from pathlib import Path
from .video_utils import fragment_video, create_video_from_images
from .ml.utils import process_images
from .folder_utils import clear_folders

IMAGES_FOLDER = Path("uploads/frames")
PROCESSED_FRAMES_FOLDER = Path("processed/result_frames")
PROCESSED_VIDEO_PATH = Path("processed/processed_video.mp4")


async def process_video(path_to_file: Path, mode: str, fps: int) -> Path:
    clear_folders([IMAGES_FOLDER, PROCESSED_FRAMES_FOLDER])
    fragment_video(video_path=path_to_file, output_folder=IMAGES_FOLDER, fps=fps)
    await process_images(input_folder=IMAGES_FOLDER, mode=mode, output_folder=PROCESSED_FRAMES_FOLDER)
    create_video_from_images(input_folder=PROCESSED_FRAMES_FOLDER, output_video_path=PROCESSED_VIDEO_PATH, fps=fps)

    return PROCESSED_VIDEO_PATH
