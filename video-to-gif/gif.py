from moviepy.editor import VideoFileClip
from tkinter.filedialog import *

video = VideoFileClip(askopenfilename())
video.write_gif("demo.gif")