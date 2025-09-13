from os import listdir
from os.path import isfile, join
from audio_splitter import SplitWavAudioMubin

if __name__ == '__main__':
    # --- Configuration ---
    dataset_name = "AppleWatch8"
    audio_folder = join("audio", dataset_name)
    # The text files will be saved in the same directory as the audio files.
    
    # --- Processing ---
    # Get all audio file names from the directory
    audio_files = [f for f in listdir(audio_folder) if isfile(join(audio_folder, f)) and f.endswith('.wav')]
    
    # Process each audio file
    for audio_file in audio_files:
        print(f"Processing {audio_file}...")
        split_wav = SplitWavAudioMubin(audio_folder, audio_file)
        split_wav.multiple_split(min_per_split=1)
    
    print("--- All files processed. ---")