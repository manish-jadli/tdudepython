#checkbox

from tkinter import *

window=Tk()

window.geometry("500x500")

check_box_1=IntVar()
check_box_2=IntVar()
check_box_3=IntVar()

chk_btn1=Checkbutton(window, text="Apple", onvalue=1, offvalue=8,height=2, width=10)
chk_btn2=Checkbutton(window, text="Mango", onvalue=1, offvalue=8,height=2, width=10)
chk_btn3=Checkbutton(window, text="Plum", onvalue=1, offvalue=8,height=2, width=10)


chk_btn1.pack()
chk_btn2.pack()
chk_btn3.pack()

#mainloop
mainloop()