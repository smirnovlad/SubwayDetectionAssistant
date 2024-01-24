from ultralytics import YOLO
from pathlib import Path
import torch
import numpy as np
from ...folder_utils import numerical_sort
from matplotlib import pyplot as plt
from PIL import Image
import glob
import os
import cv2

model = YOLO('yolov8m-pose.pt')

def hpe_images(input_folder: Path, output_folder: Path):
    device = "cuda" if torch.cuda.is_available() else "cpu"
    print(f"Function: {hpe_images.__name__}. Device: {device}")

    global model
    model.to(device)

    with torch.no_grad():
        # for filename in sorted(glob.glob(input_folder.absolute().as_posix() + "/frame_*.jpg"), key=numerical_sort):
        result = model.predict(source=input_folder, save=True, project="processed", name="hpe_frames", conf=0.3, exist_ok=True)