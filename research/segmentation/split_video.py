import cv2
import os


def split_video_to_images(video_path, output_folder, fps):
    # Open the video file
    cap = cv2.VideoCapture(video_path)

    # Get video properties
    fps_original = cap.get(cv2.CAP_PROP_FPS)
    frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    # Calculate frame interval based on the desired FPS
    frame_interval = int(fps_original / fps)

    # Create output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Read and save frames
    frame_count = 0
    while True:
        ret, frame = cap.read()

        if not ret:
            break  # Break the loop if no more frames are available

        if frame_count % frame_interval == 0:
            # Save frame as an image
            image_filename = os.path.join(output_folder, f"frame_{frame_count // frame_interval}.jpg")
            cv2.imwrite(image_filename, frame)

        frame_count += 1

    # Release the video capture object
    cap.release()

    print(f"Video frames saved to {output_folder}")

video_path = "./records/2.mp4"
output_folder = "output_images"
desired_fps = 1

split_video_to_images(video_path, output_folder, desired_fps)