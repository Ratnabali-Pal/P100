import os
import cv2

def create_output_directory(directory_name='image_frames'):
    """Creates a directory to store the extracted frames."""
    if not os.path.exists(directory_name):
        os.makedirs(directory_name)
    return directory_name

def extract_frames(video_path, output_dir, frame_interval=10):
    """
    Extracts frames from a video file at a specified interval.

    Args:
        video_path (str): The path to the input video file.
        output_dir (str): The directory to save the extracted frames.
        frame_interval (int): The interval at which to extract frames (e.g., 10 means every 10th frame).
    """
    if not os.path.exists(video_path):
        print(f"Error: Video file not found at {video_path}")
        return

    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print(f"Error: Could not open video file {video_path}")
        return

    index = 0
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        if index % frame_interval == 0:
            frame_name = os.path.join(output_dir, f'frame{index}.png')
            print(f'Extracting frame.... {frame_name}')
            cv2.imwrite(frame_name, frame)

        index += 1

    cap.release()
    cv2.destroyAllWindows()
    print("Finished extracting frames.")