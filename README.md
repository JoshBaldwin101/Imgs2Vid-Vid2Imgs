# Images and Videos Conversion

This repository contains two Python scripts for converting images to video and video to images.

## Video to Images

The `video_to_images.py` script extracts the frames from a video and saves them as images.

#### Usage:

1. Place your video file inside the folder "Place your video in here".
2. Run the `video_to_images.py` script, e.g., by double-clicking the `run_video_to_images.bat` file on Windows.
3. The extracted images will be saved in a separate folder named after the video file inside the "Output" folder.

## Images to Video

The `images_to_video.py` script creates a video from a sequence of images.

#### Usage:

1. Place your image files inside the folder "Place your image files here". Make sure the image files are named like "image0", "image1", "image23", etc., sequentially without any gaps.
2. Run the `images_to_video.py` script, e.g., by double-clicking the `run_images_to_video.bat` file on Windows (you'll have to create the batch file as described below).
3. The output video will be saved as "output_video.avi" inside the "Output" folder.

## Windows Batch Files

For Windows users, there's a Launch.bat file for executing each program.

## Dependencies

These scripts use the OpenCV library. Install it using pip:
pip install opencv-python