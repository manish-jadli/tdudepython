#entry box and grid layout

from tkinter import *

window=Tk()

window.title("Simple")
window.geometry("250x50")

#labels
label1=Label(window, text="mail")
label2=Label(window, text="password")

#buttons
resetBtn=Button(text="Reset",bg="blue")
submitBtn=Button(text="Submit",bg="blue")

#input entry
e1=Entry(window,width=40,borderwidth=5)
e2=Entry(window,width=40,borderwidth=5)


label1.grid(row =0, column=1)
label2.grid(row=1,column=1)

e1.grid(row=0,column=2)
e2.grid(row=1,column=2)

resetBtn.grid(row=2,column=0)
submitBtn.grid(row=2,column=1)

#mainloop
mainloop()