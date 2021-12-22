

from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog
from pytesseract import pytesseract
from googletrans import Translator



#from testing import pic_result_temp




root = Tk()

def open():
    global image_temp
    path_to_tesseract = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


    
    root.filename = filedialog.askopenfilename(initialdir= "C:/Users/bej13/OneDrive - Queensland University of Technology/2021", filetypes=(("png files", "*.png"),("jpg files", "*.jpg"),("all files", "*.*")))
    path = root.filename
    my_label = Label(root, text="current image directory\n" + root.filename).pack()
    image_temp = ImageTk.PhotoImage(Image.open(root.filename))
    
    pytesseract.tesseract_cmd = path_to_tesseract

    img = root.filename
    text = pytesseract.image_to_string(img)
    text_final = text[:-1]
    translat = Translator()


    x = translat.translate(text_final) #e.g.read german

    #resize_image = image_temp.resize((50, 50))
    #img22 = ImageTk.PhotoImage(resize_image)
    
    my_image_label = Label(image = image_temp).pack()


    translatedtext = Label(root, text = x).pack()
    print(x)


btn = Button(root, text="Open Image", command=open).pack()
root.mainloop()