from tkinter.filedialog import *
from pyzbar.pyzbar import decode
from PIL import Image

message = decode(Image.open(askopenfilename()))
print(message[0].data.decode("ascii"))