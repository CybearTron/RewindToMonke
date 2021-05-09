from tkinter import *
import playsound
import os
from PIL import Image
#Import Oonga Boonga

root=Tk()
#Root window
root.title("RETURN TO MONKE????")
root.iconbitmap("OIP.ico")
def open_file():
    os.system('python opt.py')
    os.exit()
frame=Frame(root)
frame.pack()

label=Label(frame,text="Hwlo Sapien!!!!! So You wanna return to monke????? Then Frickin press this button lol!!!!!!!!!")
label.pack()
button=Button(frame,text="Ret_To_mONKE!!!!!",command=open_file)
button.pack()

root.mainloop()