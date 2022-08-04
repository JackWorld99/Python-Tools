from moviepy.editor import VideoFileClip
from tkinter.filedialog import *
from pathlib import Path

video_file = askopenfilename()
video = VideoFileClip(video_file)
audio = video.audio

audio.write_audiofile(Path(video_file).stem + ".mp3")
print("Conversion Completed")
