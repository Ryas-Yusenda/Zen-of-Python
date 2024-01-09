from pydub import AudioSegment
import os

# Check all mp3 files in the current directory
for file in os.listdir("."):
    if file.endswith(".mp3"):
        # Get the file name full path
        file_name = os.path.realpath(file)

        audio = AudioSegment.from_mp3(file_name)

        # Create a 5-second silent audio segment
        silence_segment = AudioSegment.silent(
            duration=5000
        )  # Duration is in milliseconds (5 seconds)

        # Concatenate the silent segment to the original audio
        output_audio = silence_segment + audio

        # Export the result to a new MP3 file
        output_name_file = file_name + "_silence.mp3"
        output_audio.export(output_name_file, format="mp3")
