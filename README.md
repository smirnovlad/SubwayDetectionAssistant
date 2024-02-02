# Subway Detection Assistant

## About

The AI solution for detecting individuals crossing the safety line on the subway platform has been implemented.

The project aims to create a solution to enhance the safety of citizens on subway platforms. The solution is built upon two models: the first addresses the Human Pose Estimation task, while the second focuses on segmentation.

To test the developed solution, I created a single-page web application where users can upload subway platform videos and receive output videos detecting individuals who have crossed the safety line.

The results of this work can also be applied in processing real-time streaming video from subway surveillance cameras.

## Implementation details

### Human Pose Estimation

#### Architecture

I used a state-of-the-art model, YOLOv8, specifically the pose estimation model, to determine the positions of people on the platform. Currently, I only utilize bounding boxes around people, but I focused specifically on the pose estimation task rather than the person detection task because in the future, information about key points of the human body (such as feet) will improve the performance quality of the application. The model of this architecture didn't need to be trained. A pre-trained implementation available online shows excellent results.

Download the model: [link](https://github.com/ultralytics/assets/releases/download/v8.1.0/yolov8m-pose.pt)

### Segmentation

#### Data collection, data annotation and architecture

For the segmentation architecture, I chose SegNet. The segmentation model identifies segments of the platform from its edge to the safety line. To train this model, I recorded 22 videos on various platforms of the Moscow metro, annotated 17 of them using the Roboflow tool, resulting in 640 annotated images. After augmentation (flipping images along the vertical axis), the dataset expanded to 1125 annotated images.

#### Model training

I trained the model for 45 epochs, gradually decreasing the learning rate after a certain number of epochs. Training notebook: [link](research/segmentation/Segmentation_1125.ipynb)

### Web App

#### Backend

I chose FastAPI as the service for processing requests due to its ease of use.

#### Frontend

The frontend is implemented in React according to the following layout: [design in Figma](https://www.figma.com/file/qGz5kg4ag92exxrOzW0T78/Single-page-Web-App)



## TODO:

* Add tests and quality metrics for the classifier that determines whether a person crossed the line or not
* Add support for real-time streaming video processing