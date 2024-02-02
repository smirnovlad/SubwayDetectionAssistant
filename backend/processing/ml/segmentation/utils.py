import torch
import numpy as np
from pathlib import Path
from .SegNet import SegNet
from ...folder_utils import numerical_sort
from matplotlib import pyplot as plt
from PIL import Image
import glob
import os

TRAINED_SEGNET_FILE_NAME = "./segnet_bce_1125_45_epoch.pth"


def extend_image(img, channels=None):
    height, width = img.shape[0], img.shape[1]
    delta = 768 - width
    if channels:
        padding = np.zeros((height, delta // 2, channels), np.uint8)
    else:
        padding = np.zeros((height, delta // 2), np.uint8)
    img = np.concatenate((padding, img, padding), axis=1)
    return img


def shrink_image(img, channels=None):
    height, width = img.shape[0], img.shape[1]
    delta = width - 720
    if channels:
        return img[:, delta // 2: width - delta // 2, :]
    else:
        return img[:, delta // 2: width - delta // 2]


# TODO: async
async def segment_images(input_folder: Path, output_folder: Path):
    device = "cuda" if torch.cuda.is_available() else "cpu"
    print(f"Function: {segment_images.__name__}. Device: {device}")

    model = SegNet().to(device)
    module_path = Path(__file__).resolve().parent
    model.load_state_dict(torch.load(module_path / TRAINED_SEGNET_FILE_NAME))

    images = []

    for filename in sorted(glob.glob(input_folder.absolute().as_posix() + "/frame_*.jpg"), key=numerical_sort):
        img = plt.imread(filename)
        images.append(img)

    masks = []

    model.eval()
    with torch.no_grad():
        for img in images:
            img = extend_image(img, 3)
            img = torch.FloatTensor(np.rollaxis(np.array(img)[np.newaxis, :], 3, 1)).to(device)

            result = model.forward(img)
            masks.append(torch.sigmoid(result[0][0]) > 0.5)

    for i, mask in enumerate(masks):
        mask = shrink_image(np.array(mask.cpu()))
        processed_frame = Image.fromarray(mask)
        image_filename = os.path.join(output_folder.as_posix(), f"frame_{i}.jpg")
        processed_frame.save(image_filename)
