from pydub import AudioSegment
import math
import speech_recognition as sr
from os import path

class SplitWavAudioMubin():
    def __init__(self, folder, filename):
        self.folder = folder
        self.filename = filename
        self.filepath = path.join(folder, filename)
        self.audio = AudioSegment.from_wav(self.filepath)

    def get_duration(self):
        """
        Returns the duration of the audio in seconds.
        """
        return self.audio.duration_seconds

    def single_split(self, from_min, to_min, split_filename):
        """
        Splits the audio file into a smaller chunk.
        """
        t1 = from_min * 60 * 1000
        t2 = to_min * 60 * 1000
        split_audio = self.audio[t1:t2]
        split_audio.export(path.join(self.folder, split_filename), format="wav")

    def multiple_split(self, min_per_split):
        """
        Splits the audio file into multiple chunks and performs speech recognition on each.
        """
        # Open a file to store the recognized text
        text_output_path = self.filename.split('.')[0] + ".txt"
        fh = open(text_output_path, "w+")
        total_mins = math.ceil(self.get_duration() / 60)
        
        # Create a speech recognition object
        r = sr.Recognizer()

        for i in range(0, total_mins, min_per_split):
            split_fn = str(i) + '_' + self.filename
            self.single_split(i, i + min_per_split, split_fn)
            file = path.join(self.folder, split_fn)
            
            # Recognize the chunk
            with sr.AudioFile(file) as source:
                audio_listened = r.listen(source)

            try:
                # Try converting audio to text
                rec = r.recognize_google(audio_listened)
                # Write the output to the file with a timestamp marker
                fh.write(rec + "@" + str(i) + "#")

            # Handle errors
            except sr.UnknownValueError:
                print("Could not understand audio")
            except sr.RequestError as e:
                print(f"Could not request results; {e}")

        print(f"All splits for {self.filename} processed successfully.")
        fh.close()