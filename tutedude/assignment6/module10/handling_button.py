#handling button

from tkinter import *

window=Tk()

window.title("Simple")
window.geometry("500x500")

def login_entry():
    print("Logged in")


button=Button(window, text="LOGIN", command=login_entry,width=12,bg="red",fg="white",font=("bold",12),activebackground="black", activeforeground="white",relief=FLAT)


button.pack()

#mainloop
mainloop()