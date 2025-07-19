#import tkinter

from tkinter import *

#gui interaction

window=Tk()

#adding inputs
window.title("Simple")
window.geometry("500x700")
window.config(bg="yellow")
frame1=Frame(window,width=300,height=300,cursor="dot")
frame2=Frame(window,width=300,height=300,cursor="dotbox")


button1=Button(frame1,text="Button 1",bg="blue")
button2=Button(frame2,text="Button 2",bg="blue")
button3=Button(frame1,text="Logged",bg="red")



frame1.pack(side=TOP)
frame2.pack(side=BOTTOM)
button3.pack()


button1.pack()
button2.pack()
# inp= Label(window, text="Hello world")
# inp.pack()


#mainloop

window.mainloop()