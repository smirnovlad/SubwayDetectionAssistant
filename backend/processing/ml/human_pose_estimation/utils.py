from ultralytics import YOLO
from pathlib import Path
import torch
from ultralytics.utils.plotting import Annotator
import cv2

model = YOLO('yolov8m-pose.pt')

# TODO: async
async def hpe_images(input_folder: Path, output_folder: Path):
    device = "cuda" if torch.cuda.is_available() else "cpu"
    print(f"Function: {hpe_images.__name__}. Device: {device}")

    global model
    model.to(device)

    with torch.no_grad():
        results = model.predict(source=input_folder, save=True, project="processed", name="hpe_frames", conf=0.3, exist_ok=True)

    return results


def check_danger(img_path, box):
    # box coordinates in (left, bottom, right, top) format
    in_danger = True
    img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
    left, bottom, right, top = tuple(map(int, box))
    width = right - left
    height = top - bottom

    bottom_white_count, top_white_count = 0, 0
    for x in range(left - 1, right):
        bottom_white_count += img[bottom - 1][x] > 128
        top_white_count += img[top - 1][x] > 128

    in_danger = bottom_white_count / width >= 0.25 or top_white_count / width >= 0.25

    if not in_danger:
        left_white_count, right_white_count = 0, 0
        for y in range(bottom - 1, top):
            left_white_count += img[y][left - 1] > 128
            right_white_count += img[y][right - 1] > 128

        in_danger = left_white_count / height >= 0.25 or right_white_count / height >= 0.25

    return in_danger


def project_hpe_onto(hpe_results, segmented_folder: Path, project_onto_folder: Path, output_folder: Path):
    for i, result in enumerate(hpe_results):
        img_path = project_onto_folder.absolute().as_posix() + "/" + Path(result.path).name
        img = cv2.imread(img_path)
        annotator = Annotator(img)

        segmented_img_path = segmented_folder.absolute().as_posix() + "/" + Path(result.path).name

        boxes = result.boxes
        for box in boxes:
            b = box.xyxy[0]  # get box coordinates in (left, bottom, right, top) format
            in_danger = check_danger(segmented_img_path, b)
            # label = "in danger" if in_danger else "in safety"
            label = ""
            color = (0, 0, 255) if in_danger else (0, 128, 0)
            annotator.box_label(b, label, color=color)

        result_img = annotator.result()
        result_filename = output_folder.absolute().as_posix() + "/" + Path(result.path).name
        cv2.imwrite(result_filename, result_img)
