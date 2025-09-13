import os
import PIL.Image
import pytesseract

def extract_text_from_images(image_dir, output_file='read.txt'):
    """
    Performs OCR on all images in a directory and saves the text to a file.

    Args:
        image_dir (str): The directory containing the image frames.
        output_file (str): The file to save the extracted text to.
    """
    if not os.path.exists(image_dir):
        print(f"Error: Image directory not found at {image_dir}")
        return

    with open(output_file, 'w') as f:
        for image_file in os.listdir(image_dir):
            if image_file.endswith(('.png', '.jpg', '.jpeg')):
                print(f"Processing {image_file}...")
                image_path = os.path.join(image_dir, image_file)
                try:
                    text = pytesseract.image_to_string(PIL.Image.open(image_path), lang='eng')
                    f.write(text + '\n')
                except Exception as e:
                    print(f"Could not process {image_file}: {e}")
    print(f"Text extraction complete. Results saved in {output_file}")