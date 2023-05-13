import os
import cv2

input_folder = 'Place your video in here'
parent_output_folder = 'Output'

# Make sure the input and parent output folders exist
os.makedirs(input_folder, exist_ok=True)
os.makedirs(parent_output_folder, exist_ok=True)

# Get the video file path
video_files = os.listdir(input_folder)

if not video_files:
    print(f'Please place a video file in the "{input_folder}" folder.')
else:
    video_file = video_files[0]
    video_path = os.path.join(input_folder, video_file)

    # Create the output folder for the specific video
    output_folder = os.path.join(
        parent_output_folder, os.path.splitext(video_file)[0])
    os.makedirs(output_folder, exist_ok=True)

    # Open the video capture
    cap = cv2.VideoCapture(video_path)

    frame_number = 0

    while cap.isOpened():
        ret, frame = cap.read()

        if not ret:
            break

        # Save the frame as an image in the specific output folder
        output_path = os.path.join(output_folder, f'image{frame_number}.png')
        cv2.imwrite(output_path, frame)

        frame_number += 1

    cap.release()
    cv2.destroyAllWindows()
