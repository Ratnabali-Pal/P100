# main.py

from scripts import preprocess, rank_segments, summarize

def main():
    """
    Main function to run the entire video review summarization pipeline.
    """
    print("Step 1: Combining score files...")
    preprocess.combine_scores()
    
    print("\nStep 2: Calculating and ranking segments...")
    rank_segments.calculate_and_rank()
    
    print("\nStep 3: Generating the final summary...")
    summarize.generate_summary()
    
    print("\nPipeline finished successfully!")

if __name__ == "__main__":
    main()