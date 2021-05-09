from tkinter import *
import playsound
import os
#Import Oonga Boonga
root=Tk()
text="OK SO UR AN Australopithecus!!! An early hominin and the predecessor of The genus homo. So your getting real close to being an ape... Your face looks like you wanna smash the pc and smash my face lol! Australopithecus existed during the Late Pliocene and Early Pleistocene. The genera Homo (which includes modern humans), Paranthropus, and Kenyanthropus evolved from Australopithecus.Australopithecus is a member of the subtribe Australopithecina, which also includes Ardipithecus, though the term australopithecine is sometimes used to refer only to members of Australopithecus. Debate exists as to whether some Australopithecus species should be reclassified into new genera, or if Paranthropus and Kenyanthropus are synonymous with Australopithecus, in part because of the taxonomic inconsistency. SO UR FRICKIN CLOSE TO MONKE PLEASE STOP THIS IF U DONT WANNA BECOME SO LESS ADVANCED AND STUPID.... WAIT UR ALREADY SO STUPID THAT U ARE DOING THIS CRAP SO CONTINUE!!!!"
root.title("Australopithecus")
def opennext():
    os.system('python Ramapithecus.py')
frame=Frame(root)
frame.pack()
message=Message(frame,text=text)
message.pack()
button=Button(frame,text="JUS FRICKIN PRESS THIS TO BECOME RAMAPITHECUS",command=opennext)
button.pack()
root.mainloop()