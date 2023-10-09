"""**Frames Switch**"""

from tkinter import *

master = Tk()#class#
master.geometry("800x400")#screen size#
master.title("this is a title!")#title#
master.resizable(width=False,height=False)#screen resizible#


def menu_reset():

    button0.place(x=10000, y=10)

    button1.place(x=10000, y=10)

    entry0.place(x=10000, y=10)

    entry0.delete(0, END)


def menu_1():

    menu_reset()

    button0.place(x=10, y=50)

    entry0.place(x=10, y=10)


def menu_2():

    menu_reset()

    button1.place(x=10, y=10)


button0 = Button(master, text="go to the second menu", command=menu_2, fg="red")
button0.place(x=10000, y=50)

entry0 = Entry(master)
entry0.place(x=10000, y=10)



button1 = Button(master, text="go back", command=menu_1, fg="blue")
button1.place(x=10000, y=10)






if __name__ == "__main__":

    menu_reset()
    menu_1()
    master.update_idletasks()#screen update#
    master.mainloop()#app loop#
