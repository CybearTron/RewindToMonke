from tkinter import *
import playsound
import os
#Import Oonga Boonga

root=Tk()
root.title("Sapien")
text="Hwlo Sapien!!!! So you are here because of millions of years of evolution. Homo Sapiens are the modern humans.Humans are the most populous and widespread primates, characterized by bipedality and large complex brains,which has allowed the development of advanced tools,culture and language. The computer ur currently using is the work of the advanced brains of Human Beings..(The exception of the person using this being an advanced species that has better computers and tech than my potato pc). Remember jus after the next step You wont be able to work with the pc properly?"

def opennext():
    os.system('python erectus.py')
frame=Frame(root)
frame.pack()

message=Message(frame,text=text)
message.pack()
button=Button(frame,text="STAGE OF HOMO ERECTUS LOL!!!!",command=opennext)
button.pack()
root.mainloop()