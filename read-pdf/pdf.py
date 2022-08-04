import pyttsx3
import PyPDF2
from tkinter.filedialog import *

book = askopenfilename()
pdfreader = PyPDF2.PdfReader(book)
pages = pdfreader.numPages

apppend_text = ''
for num in range(0, pages):
    page = pdfreader.getPage(num)
    text = page.extractText()
    # apppend_text += text

    player = pyttsx3.init()
    player.setProperty('rate', 130)
    voices = player.getProperty('voices') 
    #player.setProperty('voice', voices[0].id) # Male
    #player.setProperty('voice', voices[2].id) # Google
    player.setProperty('voice', voices[1].id) # Female

    player.say(text)
    player.runAndWait()
    player.stop()

# Save audio
# player.save_to_file(apppend_text, 'text-to-audio.mp3')
# player.runAndWait()



