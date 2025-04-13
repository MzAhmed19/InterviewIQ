from moviepy import VideoFileClip
from pydub import AudioSegment
import os

# Step 1: Extract audio from video
video_path = 'testinterview1.mp4'
audio_path = 'audio.wav'
video = VideoFileClip(video_path)
video.audio.write_audiofile(audio_path)
print("✅ Audio extracted.")

# Step 2: Split audio into 10-second chunks
audio = AudioSegment.from_wav(audio_path)
chunk_length_ms = 10 * 1000  # 10 seconds in milliseconds

# Create output directory if it doesn't exist
os.makedirs("audio_chunks", exist_ok=True)

for i in range(0, len(audio), chunk_length_ms):
    chunk = audio[i:i + chunk_length_ms]
    chunk_name = f"audio_chunks/chunk_{i // chunk_length_ms}.wav"
    chunk.export(chunk_name, format="wav")
    print(f"✅ Exported {chunk_name}")
