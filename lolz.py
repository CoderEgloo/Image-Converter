import tkinter as tk
import ttkbootstrap as ttk
from tkinter import Canvas, filedialog 
  
# window named top
top = ttk.Window(themename='minty') 
# set height and width of window 
top.geometry("300x300")  
  
#creating a simple canvas with canvas widget  


file_label = ttk.Frame(master=top)
canvas = Canvas(master = file_label, bg="yellow", height=100, bd=2)
file_label.pack()
canvas.pack()
  
top.mainloop()