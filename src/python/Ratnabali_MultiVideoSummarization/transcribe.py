import os
from datetime import timedelta
import whisper

def transcribe_audio(path, model_name="base"):
    """
    Transcribes an audio file using OpenAI's Whisper model and saves the
    transcription to a text file and an SRT file.

    Args:
        path (str): The file path of the audio to be transcribed.
        model_name (str, optional): The name of the Whisper model to use.
                                     Defaults to "base".
    """
    if not os.path.exists(path):
        print(f"Error: The file '{path}' was not found.")
        return

    try:
        model = whisper.load_model(model_name)
        print("Whisper model loaded.")

        # Transcribe the audio
        result = model.transcribe(audio=path)

        # --- Save the plain text transcription ---
        output_txt_filename = os.path.splitext(path)[0] + ".txt"
        with open(output_txt_filename, 'w', encoding='utf-8') as txt_file:
            txt_file.write(result["text"])
        print(f"Transcription saved to {output_txt_filename}")

        # --- Save the transcription as an SRT file ---
        output_srt_filename = os.path.splitext(path)[0] + ".srt"
        segments = result['segments']
        with open(output_srt_filename, 'a', encoding='utf-8') as srtFile:
            for segment in segments:
                startTime = str(0) + str(timedelta(seconds=int(segment['start']))) + ',000'
                endTime = str(0) + str(timedelta(seconds=int(segment['end']))) + ',000'
                text = segment['text']
                segmentId = segment['id'] + 1
                segment_str = f"{segmentId}\n{startTime} --> {endTime}\n{text[1:] if text[0] == ' ' else text}\n\n"
                srtFile.write(segment_str)
        print(f"SRT file saved to {output_srt_filename}")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == '__main__':
    # You will need to have an audio file named '1.wav' in the same directory
    # as this script, or provide a different path.
    audio_file = "1.wav"
    transcribe_audio(audio_file)