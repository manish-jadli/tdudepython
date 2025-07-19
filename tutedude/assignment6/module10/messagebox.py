#message box

from tkinter import *
import tkinter.messagebox

window=Tk()

window.geometry("500x500")

# tkinter.messagebox.showinfo("Info","Runnig out time")
# question=tkinter.messagebox.askyesno("Weather","Will it rain?")

# if question ==True:
#     print("Take an umbrella")
# else:
#     print("Okay")

# message=Message(window,text="Python")
# message.pack()


# var=StringVar()
# message=Message(window,textvariable=var,relief=RAISED,padx=20,pady=20)
# var.set("Welcome")
# message.pack()


var=StringVar()
ent_var=StringVar()

def insert():
    result=ent_var.get()
    var.set(result)

message=Message(window,textvariable=var, relief=RAISED,padx=50,pady=50)
entry=Entry(window,textvariable=ent_var)
button=Button(window,text="OK",command=insert)


message.pack()
entry.pack()
button.pack()

#mainloop
mainloop()