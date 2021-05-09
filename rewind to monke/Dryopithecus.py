from tkinter import *
import playsound
import os
#Import Oonga Boonga
root=Tk()
root.title("Dryopithecus")
text="OK MATE UR AT THE LAST STAGE OF MONKE!!!!!!!!!!! DON'T YOU DARE EYE ME LIKE THAT!!!im scared ;-;....You know Dryopithecus are deemed to be the ancestors of both man and apes. They lived in China, Africa, Europe and India. The genus Dryopithecus refers to the oak wood apes. When Dryopithecus was alive, the tropical lowlands which it inhabited were densely forested, so the members could have predominantly been herbivores.OK MONKE UR AN APE NOW SO TO BE QUALIFIED AS AN APE AND GET FREE BANANAS PRESS THE RIGHT BUTTON BELOW... U PRESS THE WRONG ONE NO BANANAS FOR YOU OK... HEY DON'T BE ANGRY AT ME !!!!!!!!!!CLICK CLICK CLICK!!!!!"
def opennext():
    os.system('python bananas.py')
frame=Frame(root)
frame.pack()
message=Message(frame,text=text)
message.pack()
button=Button(frame,text="BANANANANANANNANANANANANANANAS!!!!!!!!!!!!!!!!!",command=opennext)
button.pack()

root.mainloop()