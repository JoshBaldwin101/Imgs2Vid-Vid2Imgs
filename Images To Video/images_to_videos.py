import os
import cv2

input_folder = 'Place your image files here'
output_folder = 'Output'

# Make sure the input and output folders exist
os.makedirs(input_folder, exist_ok=True)
os.makedirs(output_folder, exist_ok=True)

# Get the image file paths
image_files = sorted([f for f in os.listdir(input_folder)
                     if f.startswith('image') and f.endswith('.png')])

if not image_files:
    print(f'Please place image files in the "{input_folder}" folder.')
else:
    # Read the first image to get dimensions
    first_image = cv2.imread(os.path.join(input_folder, image_files[0]))
    height, width, _ = first_image.shape

    # Create the video writer
    video_out_path = os.path.join(output_folder, 'output_video.avi')
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    fps = 30
    video_writer = cv2.VideoWriter(
        video_out_path, fourcc, fps, (width, height))

    for image_file in image_files:
        image_path = os.path.join(input_folder, image_file)
        frame = cv2.imread(image_path)
        video_writer.write(frame)

    video_writer.release()
    print(f'Video saved at: {video_out_path}')
