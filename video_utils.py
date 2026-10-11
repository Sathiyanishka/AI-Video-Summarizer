import os
from moviepy import VideoFileClip


def extract_audio(video_path):
    audio_folder = "static/audio"
    os.makedirs(audio_folder, exist_ok=True)

    video_name = os.path.splitext(os.path.basename(video_path))[0]
    audio_path = os.path.join(audio_folder, f"{video_name}.wav")

    clip = VideoFileClip(video_path)

    if clip.audio is None:
        raise Exception("This video has no audio track.")

    clip.audio.write_audiofile(audio_path)

    clip.close()

    return audio_path