import os
from os import listdir
from os.path import isfile, join
from sentiment_analyzer import analyze_sentiment
from keyword_extractor import extract_and_score_keywords

def main():
    """
    Main function to run the sentiment analysis and keyword extraction pipeline.
    """
    dataset = "AppleWatch8"
    text_path = f"text/{dataset}"
    sentiment_output_path = "sentiment"
    keyword_output_path = f"keyword/{dataset}"

    # Create output directories if they don't exist
    if not os.path.exists(sentiment_output_path):
        os.makedirs(sentiment_output_path)
    if not os.path.exists(keyword_output_path):
        os.makedirs(keyword_output_path)

    # Get the list of text files
    text_files = [f for f in listdir(text_path) if isfile(join(text_path, f))]

    # --- 1. Perform Sentiment Analysis ---
    print("Starting sentiment analysis...")
    analyze_sentiment(text_files, text_path, sentiment_output_path)
    print("Sentiment analysis complete.")

    # --- 2. Perform Keyword Extraction and Scoring ---
    print("\nStarting keyword extraction and scoring...")
    extract_and_score_keywords(text_files, text_path, keyword_output_path)
    print("Keyword extraction and scoring complete.")

if __name__ == "__main__":
    main()