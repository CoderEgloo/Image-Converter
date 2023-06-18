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
window.eval('tk::PlaceWindow . center')


#creating the global variables
filepath = {}
selectedextensions = ["JPEG/JPG", "PNG", "WEBP", "ICNs"]
originalExtensions = []
filenames = []


def openfile():
    #opening the finder to search for images
    files = filedialog.askopenfiles(title="Select Image Type")
    #initializing the global variables
    global filepath
    global originalExtensions
    global filenames 



    if files:
        print("Selected files:  ")
        files_frame = tk.Frame(master=window, highlightbackground="#E53F71", highlightthickness=3, width=800, height=h-20)
        for file_path in files:
            print(file_path.name)
            file_frame = tk.Frame(master=files_frame, highlightbackground="#E53F71", highlightthickness=3)
            Filename_label = tk.Label(master = file_frame, text=os.path.splitext(os.path.basename(file_path.name))[0], foreground="green", background="yellow", borderwidth=3)
            Filename_label.pack(side="left")
            filenames.append(os.path.splitext(os.path.basename(file_path.name))[0])
            
            Fileextension_label = tk.Label(master = file_frame, text=os.path.splitext(file_path.name)[1:], foreground="green", background="yellow", borderwidth=3)
            Fileextension_label.pack(side="left", padx=10)
            
            originalExtensions.append(os.path.splitext(file_path.name)[1:])
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
    #initializing the global variables
    global filepath
    global originalExtensions
    global filenames 
    #print (filepath)
    #print (originalExtensions)


    for image_path, selected_extension, originalExtension, filename in zip(filepath.keys(), filepath.values(), originalExtensions, filenames):
            image = Image.open(image_path)
            extension = selected_extension.get()
            if originalExtension != extension:
                if extension == "JPEG/JPG":
                 extension = "JPG"
                if extension in ["PNG", "WEBP", "JPG"]:
                    image.save(f"{os.path.dirname(image_path)}/{filename}.{extension}")
                    print(f"{os.path.dirname(image_path)}/{filename}.{extension}")
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


