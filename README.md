# Subway Detection Assistant 🤖

## About ❔

The AI solution for detecting individuals crossing the safety line on the subway platform has been implemented.

The project aims to create a solution to enhance the safety of citizens on subway platforms. The solution is built upon two models: the first addresses the Human Pose Estimation task, while the second focuses on segmentation.

To test the developed solution, I created a single-page web application where users can upload subway platform videos and receive output videos detecting individuals who have crossed the safety line.

The results of this work can also be applied in processing real-time streaming video from subway surveillance cameras. To enhance citizen safety on the metro platform, a system of fines for crossing the safety line before the train arrives could be implemented. It would be sufficient to install several cameras along the tracks, focused on the platform, for personal identification purposes.

## Example

Coming soon.

Website: [link](http://51.250.83.97:3000/)

Recordings from the video camera: [link](https://drive.google.com/drive/folders/1griTlB1BhWMGeoeSK0ap2C0pnm9OlVBg?usp=drive_link)

## Implementation details

### Human Pose Estimation 🧘🏻

#### Architecture 📐

I used a state-of-the-art model, YOLOv8, specifically the pose estimation model, to determine the positions of people on the platform. Currently, I only utilize bounding boxes around people, but I focused specifically on the pose estimation task rather than the person detection task because in the future, information about key points of the human body (such as feet) will improve the performance quality of the application. The model of this architecture didn't need to be trained. A pre-trained implementation available online shows excellent results.

Download the model: [link](backend/processing/ml/human_pose_estimation/yolov8m-pose.pt)

### Segmentation 🔎

#### Data collection, data annotation and architecture 💾

For the segmentation architecture, I chose SegNet. The segmentation model identifies segments of the platform from its edge to the safety line. To train this model, I recorded 22 videos on various platforms of the Moscow metro, annotated 17 of them using the Roboflow tool, resulting in 640 annotated images. After augmentation (flipping images along the vertical axis), the dataset expanded to 1125 annotated images.

Dataset on Roboflow: [link](https://app.roboflow.com/study-jzyvf/metro-detection/6)

#### Model training 🦾

I trained the model for 45 epochs, gradually decreasing the learning rate after a certain number of epochs. Training notebook: [link](research/segmentation/Segmentation_1125.ipynb)

Download the model: [link](backend/processing/ml/segmentation/segnet_bce_1125_45_epoch.pth)

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

#### Backend

I chose FastAPI as the service for processing requests due to its ease of use.

#### Frontend

The frontend is implemented in React according to the following layout: [design in Figma](https://www.figma.com/file/qGz5kg4ag92exxrOzW0T78/Single-page-Web-App)


## TODO:

* Add tests and quality metrics for the classifier that determines whether a person crossed the line or not
* Add support for real-time streaming video processing