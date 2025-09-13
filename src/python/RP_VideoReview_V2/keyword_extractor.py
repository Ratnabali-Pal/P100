from keybert import KeyBERT

def get_all_text(text_files, text_path):
    """
    Aggregates all text from a list of files into a single string.

    Args:
        text_files (list): A list of filenames to process.
        text_path (str): The path to the directory containing the text files.

    Returns:
        str: A single string containing all the text from the files.
    """
    all_text = ""
    for t in text_files:
        with open(f"{text_path}/{t}") as f:
            lines = f.readlines()
        
        text_content = str(lines[0])
        text_segments = text_content.split("@")
        
        for segment_data in text_segments:
            all_text += " " + str(segment_data)
    return all_text

def extract_and_score_keywords(text_files, text_path, keyword_output_path):
    """
    Extracts keywords and keyphrases from the text, calculates scores for each
    text segment, and saves the results.

    Args:
        text_files (list): A list of filenames to process.
        text_path (str): The path to the directory containing the text files.
        keyword_output_path (str): The path to the directory to save keyword scores.
    """
    all_text = get_all_text(text_files, text_path)
    
    kw_model = KeyBERT()
    
    # Extract single keywords
    keywords_single = kw_model.extract_keywords(all_text, top_n=20)
    print("Top 20 Single Keywords:", keywords_single)

    # Extract keyphrases
    keywords_phrases = kw_model.extract_keywords(all_text, keyphrase_ngram_range=(1, 2), stop_words='english', top_n=20)
    print("Top 20 Keyphrases:", keywords_phrases)
    
    output_file_path = f"{keyword_output_path}/keyword_scores.txt"
    with open(output_file_path, "w+") as fh:
        for t in text_files:
            with open(f"{text_path}/{t}") as f:
                lines = f.readlines()

            text_content = str(lines[0])
            text_segments = text_content.split("@")
            
            segment_number = 1
            for segment_data in text_segments:
                if segment_data.strip():
                    g1_score = 0
                    g2_score = 0
                    
                    # Calculate score based on single keywords
                    for kw, score in keywords_single:
                        count = segment_data.count(kw)
                        g1_score += count * score
                    
                    # Calculate score based on keyphrases
                    for kw, score in keywords_phrases:
                        count = segment_data.count(kw)
                        g2_score += count * score
                        
                    fh.write(f"{t.split('.')[0]},{segment_number},{g1_score},{g2_score}\n")
                    segment_number += 1
            print(f"Calculated keyword scores for: {t}")