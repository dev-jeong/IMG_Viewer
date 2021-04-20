import os

from tkinter import *
from PIL import Image,ImageTk

from itertools import cycle

path_dir = './img/'
file_list = os.listdir(path_dir)

img_list = []

viewer=Tk()
viewer.attributes("-fullscreen", True)
viewer.configure(bg='black')

label=Label(viewer)
label.pack()

for file in file_list :
    img_list.append(ImageTk.PhotoImage(Image.open(path_dir + file)))

img_list = cycle(img_list)

def move():
    label.config(image=next(img_list))
    viewer.after(2000,move)

move()
mainloop()