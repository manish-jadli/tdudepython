#menubar

from tkinter import *

window=Tk()
window.title("Menu")
window.geometry("400x300")


menu = Menu(window)
file = Menu(menu , tearoff = 0)
file.add_command(label = "New")
file.add_command(label = "Open")
file.add_command(label = "Save")
file.add_command(label = "Save as")
file.add_separator()
file.add_command(label="Exit", command=window.quit)


menu.add_cascade(label = "File", menu = file)
window.config(menu = menu)

#mainloop
mainloop()