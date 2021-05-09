from tkinter import *
import playsound
import os

#Import Oonga Boonga
root=Tk()
root.title("BANANAS")
frame=Frame(root)
frame.pack()
EXIT=Frame(root)
EXIT.pack(side=BOTTOM)
text="I SAID THE RIGHT ONE PEA-BRAIN!!!! YOU ARE A NOOB!!! NO BANANAS HAHAHAHAHA!!!!! WAIT NO DONT!!!!"


def quitt():
    os.system('python pcsmash.py')
    
    
    

    
    


button=Button(frame,text="DESTROY THE PC!!!! THE PC HAS BANANAS CLICK THIS!!!!!!!",command=quitt)
button.pack(side=BOTTOM)

message=Message(frame,text=text)
message.pack()



root.mainloop()