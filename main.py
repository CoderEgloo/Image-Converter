import tkinter as tk
import ttkbootstrap as ttk
from tkinter import Canvas, filedialog
from PIL import Image
import os


#declaring basic window infow
window = ttk.Window(resizable=(False, True)) #can only be streched in the y direction
window.title("iKon") 
window.configure(background="#9C3587") #color
w = 860
h = 400
window.geometry(f"{w}x{h}")

filepath = {}
selectedextensions = ["JPEG/JPG", "PNG"]
originalExtension = []


def openfile():
    #opening the finder to search for images
    files = filedialog.askopenfiles(title="Select Image Type")
    #declaring the global variables
    global filepath
    global originalExtension 



    if files:
        print("Selected files:  ")
        files_frame = tk.Frame(master=window, highlightbackground="#E53F71", highlightthickness=3, width=800, height=h-20)
        for file_path in files:
            print(file_path.name)
            file_frame = tk.Frame(master=files_frame, highlightbackground="#E53F71", highlightthickness=3)
            Filename_label = tk.Label(master = file_frame, text=os.path.splitext(os.path.basename(file_path.name))[0], foreground="green", background="yellow", borderwidth=3)
            Filename_label.pack(side="left")
            
            Fileextension_label = tk.Label(master = file_frame, text=os.path.splitext(file_path.name)[1:], foreground="green", background="yellow", borderwidth=3)
            Fileextension_label.pack(side="left", padx=10)
            
            originalExtension = os.path.splitext(file_path.name)[1:]
            clicked = tk.StringVar()
            clicked.set(selectedextensions[0])
  

            drop = tk.OptionMenu(file_frame , clicked , *selectedextensions )
            drop.pack()
            filepath[file_path.name] = clicked

            



            file_frame.pack(padx=25, pady=5)
        files_frame.pack()
        files_frame.pack_propagate(False) 
        
    else:
        print("No files selected.")

def convertfile():
    global filepath
    global originalExtension 
    print (filepath)

    for image_path, selected_extension in filepath.items():
            image = Image.open(image_path)
            extension = selected_extension.get()
            if extension == "PNG":
                image.save(os.path.dirname(image_path) + "/LOL.png")
                print(os.path.dirname(image_path) + "/LOL.png")
                image.show()




    

     


title_label = tk.Label(master=window, text="Image Conversion", font="Calibri 24")
title_label.pack()

input_frame = ttk.Frame(master=window)

entryINT = tk.IntVar()
#entry = ttk.Entry(master=input_frame, textvariable=entryINT)
Select_button = tk.Button(master=input_frame, text="Select Files", command=openfile)
Select_button.pack(side="left", padx=10)



Convert_button = tk.Button(master=input_frame, text="Convert + Save", command= convertfile)
Convert_button.pack(side="left")

input_frame.pack(pady=20)


window.mainloop()


