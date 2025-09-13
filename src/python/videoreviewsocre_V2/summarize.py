# scripts/summarize.py

import os
import pandas as pd
from . import config
from .utils import jaccard_similarity

def generate_summary():
    """
    Generates the final summary by selecting top-ranked, non-redundant segments.
    """
    ranked_scores_path = os.path.join(config.SCORE_DIR, "ranked_scores.csv")
    segment_text_path = os.path.join(config.SCORE_DIR, "segment.txt")
    
    # Load ranked scores and segment sentences
    df_ranked = pd.read_csv(ranked_scores_path)
    df_segments = pd.read_csv(segment_text_path, sep=',', names=['video_no', 'segment', 'segment_sentence'])
    
    # Merge the dataframes
    df_final = pd.merge(df_ranked, df_segments, on=['video_no', 'segment'])
    
    # Clean up the segment sentences
    df_final['segment_sentence'] = df_final['segment_sentence'].str.replace('\\W', ' ', regex=True)
    df_final['segment_sentence'] = df_final['segment_sentence'].str.replace('\\d+', '', regex=True)
    
    # Sort by rank
    df_final.sort_values(by='rank', ascending=True, inplace=True)
    df_final.reset_index(drop=True, inplace=True)

    # Generate summary using Jaccard similarity to avoid redundancy
    final_indices = []
    summarized_text = ""
    
    if not df_final.empty:
        final_indices.append(0)
        summarized_text = df_final['segment_sentence'].iloc[0]

        for i in range(1, len(df_final)):
            is_redundant = False
            for j in final_indices:
                score = jaccard_similarity(
                    df_final['segment_sentence'][i].split(),
                    df_final['segment_sentence'][j].split()
                )
                if score > config.JACCARD_THRESHOLD:
                    is_redundant = True
                    break
            
            if not is_redundant:
                final_indices.append(i)
                summarized_text += " " + df_final['segment_sentence'].iloc[i]
            
            if len(final_indices) == config.SUMMARY_LENGTH:
                break
    
    # Save the summary to a file
    summary_path = os.path.join(config.SCORE_DIR, "summarized.txt")
    with open(summary_path, "w+") as f:
        f.write(summarized_text)
        
    print(f"Summary saved to {summary_path}")
    print("\nFinal Summary:")
    print(summarized_text)

if __name__ == '__main__':
    generate_summary()