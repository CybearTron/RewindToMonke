from tkinter import *
import playsound
import os
#Import Oonga Boonga
root=Tk()
root.title("Erectus")
text="Homo Erectus.... The upright man.... its an extinct species of archaic humans. They were in The Ice Age or the  Pleistocene, with its earliest occurence about 2 million years ago.They are from the Genus Homo(i.e. us humans' genus...Get it Homo sapien)H. erectus was the first human ancestor to spread throughout Eurasia, with a continental range extending from the Iberian Peninsula to Java. African populations of H. erectus are likely to be the ancestors to several human species, such as H. heidelbergensis and H. antecessor, with the former generally considered to have been the ancestor to Neanderthals and Denisovans, and sometimes also modern humans. So we are getting closer to monke.. Its our first conversion... Do you wanna continue? As ur already an inferior being with a much simpler and simply(get the pun) lesser advanced brain, Lol. SO ARE U TOTALLY SURE 'BOUT THIS? AS U WILL GET WORSE AND WORSE!!!!!"
frame=Frame(root)
frame.pack()
def opennext():
    os.system('python Australopithecus.py')
message=Message(frame,text=text)
message.pack()
button=Button(frame,text="STAGE OF AUSTRALOPITHECUS!!!! CLICK CLICK!!!!!! ",command=opennext)
button.pack()
root.mainloop()