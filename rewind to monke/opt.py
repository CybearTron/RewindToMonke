from tkinter import *
import playsound
import os
#Import Oonga Boonga

root=Tk()
root.title("OPTION")
def sapien():
    os.system('python sapien.py')


frame=Frame(root)
frame.pack()

label=Label(frame,text="So ur sure about returning to monke then!!! then click next POG!!!!")
label.pack()
button=Button(frame,text="STAGE OF HOMO SAPIENS",command=sapien)
button.pack()
root.mainloop()