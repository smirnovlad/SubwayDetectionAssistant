from pathlib import Path
from .video_utils import split_video_to_images, create_video_from_images
from .ml.utils import process_images

import shutil

IMAGES_FOLDER = Path("output_images")
RESULT_WITH_NO_AUDIO_PATH = Path("processed/result_with_no_audio.mp4")
PROCESSED_VIDEO_PATH = Path("processed/processed_video.mp4")


def process_video(path_to_file: Path, fps: int) -> Path:
    split_video_to_images(video_path=path_to_file, output_folder=IMAGES_FOLDER, fps=fps)
    process_images(input_folder=IMAGES_FOLDER)
    create_video_from_images(input_folder=IMAGES_FOLDER, output_video_path=PROCESSED_VIDEO_PATH, fps=fps)

    # shutil.rmtree(OUTPUT_FOLDER)

    return PROCESSED_VIDEO_PATH
