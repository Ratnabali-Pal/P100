import video_processing
import ocr_processing

if __name__ == '__main__':
    # --- Configuration ---
    VIDEO_PATH = "johnson.MOV"  # Change this to the path of your video
    IMAGE_FRAMES_DIR = "image_frames"
    OUTPUT_TEXT_FILE = "extracted_text.txt"
    FRAME_INTERVAL = 10  # Extract every 10th frame

    # 1. Create a directory to store the extracted frames
    video_processing.create_output_directory(IMAGE_FRAMES_DIR)

    # 2. Extract frames from the video
    video_processing.extract_frames(VIDEO_PATH, IMAGE_FRAMES_DIR, FRAME_INTERVAL)

    # 3. Perform OCR on the extracted frames and save the text
    ocr_processing.extract_text_from_images(IMAGE_FRAMES_DIR, OUTPUT_TEXT_FILE)