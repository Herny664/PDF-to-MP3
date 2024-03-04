import pyttsx3
from PyPDF2 import PdfReader

with open('Time Is Money - Aiden_Nolan.pdf', 'rb') as file:
    pdfReader = PdfReader(file)
    text = ''
    #Extract text from each page
    for page_num in range(len(pdfReader.pages)):
        text += pdfReader.pages[page_num].extract_text()

speaker = pyttsx3.init()
speaker.save_to_file(text, 'audio.mp3')
speaker.runAndWait()
speaker.stop()