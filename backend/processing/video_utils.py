import cv2
import os
from pathlib import Path
import glob
import re


def split_video_to_images(video_path: Path, output_folder: Path, fps: int):
    # Open the video file
    cap = cv2.VideoCapture(video_path.as_posix())

    # Get video properties
    fps_original = cap.get(cv2.CAP_PROP_FPS)
    frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    print(f"Video properties. Frame width: {frame_width}, frame height: {frame_height}")

    # Calculate frame interval based on the desired FPS
    frame_interval = int(fps_original / fps) if fps < fps_original else 1

    # Create output folder if it doesn't exist
    if not os.path.exists(output_folder.as_posix()):
        os.makedirs(output_folder.as_posix())

    # Read and save frames
    frame_count = 0
    while True:
        ret, frame = cap.read()

        if not ret:
            break  # Break the loop if no more frames are available

        if frame_count % frame_interval == 0:
            # Save frame as an image
            image_filename = os.path.join(output_folder.as_posix(), f"frame_{frame_count // frame_interval}.jpg")
            cv2.imwrite(image_filename, frame)

        frame_count += 1

    # Release the video capture object
    cap.release()

    print(f"Video frames saved to {output_folder.as_posix()}")


numbers = re.compile(r"(\d+)")


def numericalSort(value):
    parts = numbers.split(value)
    parts[1::2] = map(int, parts[1::2])
    return parts


def create_video_from_images(input_folder: Path, output_video_path: Path, fps: int):
    frameSize = (720, 1280)  # must be equal to input size!!!

    print("Output video path: ", output_video_path.absolute().as_posix())

    out = cv2.VideoWriter(output_video_path.absolute().as_posix(), cv2.VideoWriter_fourcc(*'avc1'), fps, frameSize)

    for filename in sorted(glob.glob(input_folder.absolute().as_posix() + "/frame_*.jpg"), key=numericalSort):
        img = cv2.imread(filename)
        out.write(img)

    out.release()
