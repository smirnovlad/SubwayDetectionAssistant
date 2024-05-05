# Subway Detection Assistant 🤖

## About ❔

The AI solution for detecting individuals crossing the safety line on the subway platform has been implemented.

The project aims to create a solution to enhance the safety of citizens on subway platforms. The solution is built upon two models: the first addresses the Human Pose Estimation task, while the second focuses on segmentation. The peculiarity of the solution lies in the fact that the camera from which we receive the input video stream is not required to be in a fixed position. The neural network for segmentation is trained to detect the shoot line from various perspectives, as the training dataset consists of snapshots from different angles.

To test the developed solution, I created a single-page web application where users can upload subway platform videos and receive output videos detecting individuals who have crossed the safety line.

The results of this work can also be applied in processing real-time streaming video from subway surveillance cameras. To enhance citizen safety on the metro platform, a system of fines for crossing the safety line before the train arrives could be implemented. It would be sufficient to install several cameras along the tracks, focused on the platform, for personal identification purposes.

## Example

![Example](example/annotated/example.gif)

Website: [link](http://51.250.83.97:3000/)

Recordings from the video camera: [google drive](https://drive.google.com/drive/folders/1griTlB1BhWMGeoeSK0ap2C0pnm9OlVBg?usp=drive_link)

## Implementation details

### Human Pose Estimation 🧘🏻

#### Architecture 📐

I used a state-of-the-art model, YOLOv8, specifically the pose estimation model, to determine the positions of people on the platform. Currently, I only utilize bounding boxes around people, but I focused specifically on the pose estimation task rather than the person detection task because in the future, information about key points of the human body (such as feet) will improve the performance quality of the application. The model of this architecture didn't need to be trained. A pre-trained implementation available online shows excellent results.

Download the model: [yolov8m-pose.pt](backend/processing/ml/human_pose_estimation/yolov8m-pose.pt)

### Segmentation 🔎

#### Data collection, data annotation and architecture 💾

For the segmentation architecture, I chose SegNet. The segmentation model identifies segments of the platform from its edge to the safety line. To train this model, I recorded 22 videos on various platforms of the Moscow metro, annotated 17 of them using the Roboflow tool, resulting in 640 annotated images. After augmentation (flipping images along the vertical axis), the dataset expanded to 1125 annotated images.

Dataset of recordings: [metro-dataset](metro-dataset)

Dataset of frames on Roboflow: [link](https://app.roboflow.com/study-jzyvf/metro-detection/6)

#### Model training 🦾

I trained the model for 45 epochs, gradually decreasing the learning rate after a certain number of epochs. Training notebook: [Segmentation_1125.ipynb](research/segmentation/Segmentation_1125.ipynb)

Download the model: [segnet_bce_1125_45_epoch.pth](backend/processing/ml/segmentation/segnet_bce_1125_45_epoch.pth)

### Algorithm

The detection task is handled by the YOLOv8 model in Human Pose Estimation mode, and platform edge segmentation is done using SegNet. For classification purposes, determining whether a person is in a hazardous zone or not relies on the following idea: rectangles around detected individuals, obtained from the output of YOLOv8, are considered. Then, the proportion of edges of each rectangle lying within the segmented area is checked. If this value exceeds a predefined threshold, it is assumed that the person is on the platform edge; otherwise, they are considered to be in the safe zone.

For more precise results, algorithms for constructing convex hulls around the segmented platform area (which may be disjointed), utilizing key points of a person's legs (which may sometimes be invisible), etc., could be employed. However, compared to those alternatives, the presented solution is more efficient in terms of computational resources.

### Video stream processing 📹

The video stream input to the algorithm is first fragmented according to the specified FPS using OpenCV library tools. Next, depending on the selected operating mode of the application, the extracted frames are fed as input to either HPE models, segmentation models, or both simultaneously. The output frames obtained are then concatenated according to the AVC standard to produce the final result.

**Note.** The final video recording is created by calling the command:

    `out = cv2.VideoWriter(output_video_path.absolute().as_posix(), cv2.VideoWriter_fourcc(*'avc1'), fps, frameSize)`

However, I encountered the following issues during the development of the application:

1. When working on Windows OS, I encountered a missing dll file `openh264-1.8.0-win64.dll`, and I received the corresponding error message in the terminal.
2. Both on Windows and Linux, I faced issues with the codec:

    `[ERROR:0@2076.009] global cap_ffmpeg_impl.hpp:3130 open Could not find encoder for codec_id=27, error: Encoder not found`
    
    `[ERROR:0@2076.009] global cap_ffmpeg_impl.hpp:3208 open VIDEOIO/FFMPEG: Failed to initialize VideoWriter`

    To solve this problem, I used the OpenCV library implementation provided by the conda package manager.

### Web App 🌐

The developed interface allows the user to upload a video recording of the metro platform, select the FPS for segmenting the uploaded recording, as well as one of the video stream processing modes: fragmentation, segmentation, human pose estimation, detection. It's running on a virtual machine rented in the Yandex.Cloud.

![Modes](example/annotated/modes.png)

#### Backend 🖥

I chose FastAPI as the service for processing requests due to its ease of use. Depending on the server, computations are performed either on the CPU or on the GPU.

#### Frontend ⚛️

The frontend is implemented in React according to the following layout: [design in Figma](https://www.figma.com/file/qGz5kg4ag92exxrOzW0T78/Single-page-Web-App)

## Results 📝

The application solves the assigned task. The developed algorithm successfully detects objects on the platform and classifies them depending on whether they are in a hazardous zone or not.

As expected, the segmentation model performs an order of magnitude better on video recordings from the training dataset compared to unannotated video recordings. The problem lies in the specificity of the shoot line on each platform depending on the station. Therefore, for a stable solution at each station, preliminary labeling and further training of the neural network on new annotated data are necessary.

An example of edge segmentation of a platform on an unannotated platform:

<img src="example/unannotated/unannotated_example.png" width="256">

## TODO:

* Add tests and quality metrics for the classifier that determines whether a person crossed the line or not
* Add support for real-time streaming video processing
* Explore the possibility of resizing images (using various interpolation methods) to enhance the quality of the algorithm
* The use of morphological transformations of segmentation masks (dilation, erosion, etc.) for noise and interference removal. Skeletonization can also be used to highlight the main connected component
* To achieve more stable model training for segmentation, consider using gradient accumulation within the training loop
