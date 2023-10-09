"""**Frames Switch**"""

from tkinter import *

master = Tk()#class#
master.geometry("800x400")#screen size#
master.title("this is a title!")#title#
master.resizable(width=False,height=False)#screen resizible#



def login(login_bool):

    if password_entry.get() != "" and login_bool == True:

        print("logged in")

        menu_2()

    else:

        print("please fill in the entry")




def reset_screen():

    password_entry.delete(0, END)

    password_entry.place(x=250, y=10000)

    button_login.place(x=250, y=10000)

    welcome_label.place(x=250, y=10000)

    button_back.place(x=250, y=10000)



def menu_1():

    reset_screen()

    password_entry.place(x=250, y=150)

    button_login.place(x=250, y=220)


def menu_2():

    reset_screen()

    welcome_label.place(x=250, y=150)

    button_back.place(x=250, y=220)



#menu1

login_bool = True

password_entry = Entry(master, show="*")

button_login = Button(master, text="Register", command=lambda: login(login_bool))


#menu2
welcome_label = Label(master, textvariable=None)

button_back = Button(master, text="Go back!", command=menu_1)


reset_screen()
menu_1()

if __name__ == "__main__":

    master.update_idletasks()#screen update#
    master.mainloop()#app loop#
