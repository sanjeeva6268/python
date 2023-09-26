import PyPDF2
import pyttsx3


pdfReader = PyPDF2.PdfReader(open('dummypdf.pdf','rb'))

speakr = pyttsx3.init()

for page_num in range(len(pdfReader.pages)):
    text = pdfReader.pages[page_num].extract_text()
    speakr.say(text)
    speakr.runAndWait()
speakr.stop()


speakr.save_to_file(text, 'audio.mp3')


string = "Lorem Ipsum is simply dummy text " \
    + "of the printing and typesetting industry."

engine = pyttsx3.init()

engine.save_to_file(string, 'speech.mp3')

engine.runAndWait()