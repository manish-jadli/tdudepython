#frame and button using tkinter

from tkinter import *

#gui interaction
window=Tk()
window.title("Simple")
window.geometry("500x700")
window.config(bg="yellow")

#adding frame
frame1=Frame(window,width=300,height=300,cursor="dot")
frame2=Frame(window,width=300,height=300,cursor="dotbox")

#adding button
button1=Button(frame1,text="Button1",bg="blue")
button2=Button(frame2,text="Button2",bg="green")
button3=Button(frame1,text="Logged",fg="red")

#pack
frame1.pack(side=TOP)
frame2.pack(side=BOTTOM)
button1.pack()
button2.pack()
button3.pack()


#mainloop
mainloop()