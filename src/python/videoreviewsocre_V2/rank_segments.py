# scripts/rank_segments.py

import os
import pandas as pd
from . import config

def calculate_and_rank():
    """
    Loads the combined scores, normalizes them, calculates an average,
    and ranks the segments.
    """
    allscore_path = os.path.join(config.SCORE_DIR, "allscore.txt")
    
    # Load the data
    df = pd.read_csv(allscore_path, sep=',', names=['video_no', 'segment', 'label', 'senti_score', 'g1_score', 'g2_score', 'cloud_score'])

    # Normalize scores
    df['g1_score'] = df['g1_score'] / df['g1_score'].max()
    df['g2_score'] = df['g2_score'] / df['g2_score'].max()
    df['cloud_score'] = df['cloud_score'] / df['cloud_score'].max()

    # Calculate average and rank
    df['average'] = df[['g1_score', 'g2_score', 'cloud_score']].mean(axis=1)
    df['rank'] = df['average'].rank(ascending=False)
    
    # Save the ranked data
    ranked_path = os.path.join(config.SCORE_DIR, "ranked_scores.csv")
    df.to_csv(ranked_path, index=False)
    
    print(f"Ranked scores saved to {ranked_path}")

if __name__ == '__main__':
    calculate_and_rank()