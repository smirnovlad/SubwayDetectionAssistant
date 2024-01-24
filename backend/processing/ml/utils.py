import shutil

from pathlib import Path
from .segmentation.utils import segment_images
from .human_pose_estimation.utils import hpe_images
from ..folder_utils import clear_folders, copy_folder

SEGMENTED_FRAMES_FOLDER = Path("processed/segmented_frames")
HPE_FRAMES_FOLDER = Path("processed/hpe_frames")


def process_images(input_folder: Path, mode: str, output_folder: Path):
    if mode == "Fragmentation":
        copy_folder(input_folder, output_folder)
    elif mode == "Segmentation":
        clear_folders([SEGMENTED_FRAMES_FOLDER])
        segment_images(input_folder=input_folder, output_folder=SEGMENTED_FRAMES_FOLDER)
        copy_folder(SEGMENTED_FRAMES_FOLDER, output_folder)
    elif mode == "HPE":
        clear_folders([HPE_FRAMES_FOLDER])
        hpe_images(input_folder=input_folder, output_folder=HPE_FRAMES_FOLDER)
        copy_folder(HPE_FRAMES_FOLDER, output_folder)
    elif mode == "Detection":
        pass
