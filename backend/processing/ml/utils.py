from pathlib import Path
from .segmentation.utils import segment_images
from .human_pose_estimation.utils import hpe_images, project_hpe_onto
from ..folder_utils import clear_folders, copy_folder
import asyncio

SEGMENTED_FRAMES_FOLDER = Path("processed/segmented_frames")
HPE_FRAMES_FOLDER = Path("processed/hpe_frames")
HPE_SEG_FRAMES_FOLDER = Path("processed/hpe_seg_frames")
DETECTION_FRAMES_FOLDER = Path("processed/detection_frames")


# TODO: async
async def process_images(input_folder: Path, mode: str, output_folder: Path):
    if mode == "Fragmentation":
        copy_folder(input_folder, output_folder)
    elif mode == "Segmentation":
        clear_folders([SEGMENTED_FRAMES_FOLDER])
        await segment_images(input_folder=input_folder, output_folder=SEGMENTED_FRAMES_FOLDER)
        copy_folder(SEGMENTED_FRAMES_FOLDER, output_folder)
    elif mode == "HPE":
        clear_folders([HPE_FRAMES_FOLDER])
        _ = hpe_images(input_folder=input_folder, output_folder=HPE_FRAMES_FOLDER)
        copy_folder(HPE_FRAMES_FOLDER, output_folder)
    else:
        clear_folders([SEGMENTED_FRAMES_FOLDER, HPE_FRAMES_FOLDER, HPE_SEG_FRAMES_FOLDER, DETECTION_FRAMES_FOLDER])
        segment_task = asyncio.create_task(segment_images(input_folder=input_folder, output_folder=SEGMENTED_FRAMES_FOLDER))
        hpe_task = asyncio.create_task(hpe_images(input_folder=input_folder, output_folder=HPE_FRAMES_FOLDER))
        await asyncio.gather(segment_task, hpe_task)
        hpe_results = hpe_task.result()
        if mode == "HPE, SEG":
            project_hpe_onto(hpe_results=hpe_results, segmented_folder=SEGMENTED_FRAMES_FOLDER, project_onto_folder=SEGMENTED_FRAMES_FOLDER, output_folder=HPE_SEG_FRAMES_FOLDER)
            copy_folder(HPE_SEG_FRAMES_FOLDER, output_folder)
        elif mode == "Detection":
            project_hpe_onto(hpe_results=hpe_results, segmented_folder=SEGMENTED_FRAMES_FOLDER, project_onto_folder=input_folder, output_folder=DETECTION_FRAMES_FOLDER)
            copy_folder(DETECTION_FRAMES_FOLDER, output_folder)
