from tkinter import *
import playsound
import os
#Import Oonga Boonga
root=Tk()
root.title("RamaPithecus")
def opennext():
    os.system('python Dryopithecus.py')
text="Ok mate.. Your obviously looking like an ape and ur almost at the last stage of monke.... I am scared to look at you... You ARE GONNA SMASH THE PC !!!!!!!!!!Btw you know that you're the predecessor of Australopithecus(Like you didnt expect this lol). Ramapithecus were the Late Miocene and early Pliocene apes.(We are so close POG!!!!)known from fragmentary fossils from E. Africa, south-eastern Europe, and northern India and Pakistan, dating from 14–10 Ma ago, and apparently identical or very similar to the E. African Kenyapithecus. Ramapithecus is regarded by many as transitional between the true Miocene apes (the Dryopithecinae) and the later Hominidae. If this is so, then the human and ape lines diverged prior to the late Miocene, 15–25 Ma ago. More recent evidence, however, suggests that Ramapithecus and the related or identical Sivapithecus are nearer to the evolutionary line that led to the orang-utan.SO IM GONNA CAP THIS SO UR TINY BRAIN CAN UNDERSTAND THIS LOL!!!!!! PRESS THE BUTTON BELOW FOR FREE COOKIES LOLOLOLOL POG!!!!!! COOKIES!!COOKIES!!!COOKIES!!!!MUAHAHHAHAHAHAHAHHAHAHAHA!!!!!"
frame=Frame(root)
frame.pack()
message=Message(frame,text=text)
message.pack()
button=Button(frame,text="CLICK FOR COOKIES HEHEHEHEHEH!!! COOKIES",command=opennext)
button.pack()
root.mainloop()