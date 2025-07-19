#place of buttton

from tkinter import *

window=Tk()

window.geometry("500x500")

#buttons
button1=Button(window,text="Reset", width=12, bg="red",fg="white")
button2=Button(window,text="Submit", width=12, bg="red",fg="white")


button1.place(x=25,y=25)
button2.place(x=150,y=25)


#mainloop
mainloop()