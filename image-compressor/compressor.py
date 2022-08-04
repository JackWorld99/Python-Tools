import PIL
from PIL import Image
from tkinter.filedialog import *

img = PIL.Image.open(askopenfilename())
myHeight, myWidth = img.size

img = img.resize((myHeight, myWidth), PIL.Image.ANTIALIAS)
save_path = asksaveasfilename()

img.save(save_path + "_compressed.JPG")
