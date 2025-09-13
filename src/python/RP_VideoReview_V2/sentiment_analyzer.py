from transformers import pipeline

def analyze_sentiment(text_files, text_path, sentiment_output_path):
    """
    Performs sentiment analysis on text segments from files and saves the results.

    Args:
        text_files (list): A list of filenames to process.
        text_path (str): The path to the directory containing the text files.
        sentiment_output_path (str): The path to the directory to save sentiment results.
    """
    sentiment_pipeline = pipeline("sentiment-analysis")

    for t in text_files:
        output_file_path = f"{sentiment_output_path}/{t}"
        with open(output_file_path, "w+") as fh:
            with open(f"{text_path}/{t}") as f:
                lines = f.readlines()
            
            text_content = str(lines[0])
            text_segments = text_content.split("@")
            
            segment_number = 1
            for segment_data in text_segments:
                if segment_data.strip():  # Ensure the segment is not empty
                    result = sentiment_pipeline(segment_data)[0]
                    fh.write(f"{t.split('.')[0]},{segment_number},{result['label']},{result['score']}\n")
                    segment_number += 1
        print(f"Processed sentiment for: {t}")