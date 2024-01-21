# Subway Detection Assistant

## About

The AI solution for detecting individuals crossing the safety line on the subway platform has been implemented.

The project aims to create a solution to enhance the safety of citizens on subway platforms. The solution is built upon two models: the first addresses the Human Pose Estimation task, while the second focuses on segmentation.

For the segmentation architecture, I chose SegNet. The segmentation model identifies segments of the platform from its edge to the safety line. To train this model, I recorded 22 videos on various platforms of the Moscow metro, annotated 17 of them using the Roboflow tool, resulting in 640 annotated images. After augmentation (flipping images along the vertical axis), the dataset expanded to 1125 annotated images.

To test the developed solution, I created a single-page web application where users can upload subway platform videos and receive output videos detecting individuals who have crossed the safety line.

The results of this work can also be applied in processing real-time streaming video from subway surveillance cameras.

## Web App

[Design in Figma](https://www.figma.com/file/qGz5kg4ag92exxrOzW0T78/Single-page-Web-App)