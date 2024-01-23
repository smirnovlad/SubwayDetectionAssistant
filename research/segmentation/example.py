import torch
from SegNet import SegNet
from matplotlib import pyplot as plt
import numpy as np
from split_video import split_video_to_images

model = SegNet()
model.load_state_dict(torch.load('./segnet_bce_1125_35_epoch.pth', map_location=torch.device('cpu')))

def extend_image(img, channels=None):
    height, width = img.shape[0], img.shape[1]
    delta = 768 - width
    if channels:
        padding = np.zeros((height, int(delta / 2), channels), np.uint8)
    else:
        padding = np.zeros((height, int(delta / 2)), np.uint8)
    img = np.concatenate((padding, img, padding), axis=1)
    return img

images = []

for i in range(47):
    images.append(plt.imread(f'./output_images/frame_{i}.jpg'))

masks = []



model.eval()
with torch.no_grad():
    for i in range(47):
        img = images[i]
        plt.imshow(img)
        plt.show()

        img = extend_image(img, 3)
        img = torch.FloatTensor(np.rollaxis(np.array(img)[np.newaxis, :], 3, 1))

        result = model.forward(img)

        plt.imshow(torch.sigmoid(result[0][0]) > 0.5, cmap='gray')
        plt.show()