import pyautogui
import tkinter as tk 
from tkinter.filedialog import *

root = tk.Tk()

canvas1 = tk.Canvas(root, width = 300, height = 300)
canvas1.pack()

def taksScreenshot():
    img = pyautogui.screenshot()
    img.save(asksaveasfilename() + "_screenshot.png")

button = tk.Button(text = "Screenshot", command = taksScreenshot, font = 12)
canvas1.create_window(150, 150, window = button)

root.mainloop()