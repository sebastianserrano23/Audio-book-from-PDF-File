# import necessary libraries:
import pyttsx3
import PyPDF2
from tkinter.filedialog import *

# read the file in binary mode:
book = open('demo.pdf', 'rb')

# create a pdfFileReader object:
pdfReader = PyPDF2.PdfFileReader(book)

# determine total number of pages in the PDF file:
pages = pdfReader.numPages

# Initialize the speaker:
# Here, init() function is used to get a refernece rto a pyttsx3.Engine instance 
speaker = pyttsx3.init()

# to access voice property of tje speaker:
voices = speaker.getProperty('voices')

# set the speaker's gender: 0-> Male (default), 1-> Female
speaker.setProperty('voices', voices[1].id)

#iterate thriugh the pagaes you want to access
#for acccessing specific pages: Iterate through the correspponding page indices
#note: index of first page-> 0
#here, entire PDF is accessed:
for num in range(pages):
    # ro read current page index:
    page = pdfReader.getPage(num)
    # to extractc the text present in current page:
    text = page.extractText()
    # say() fucntion takes a string as the parameter and then queues the same to be converted from text-to-speach
    speaker.say(text)
    # runAndWait() function blocks  the engine instance until all the currently queued commands are processed 
    speaker.runAndWait()
# to save the audio as a MP3 file, within this project:
# make use of any MP# player to access this recording wehn required
speaker.save_to_file(text, 'audio.mp3')
speaker.runAndWait()