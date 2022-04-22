from tkinter import *


def display():
    if(x.get()):
        print('you agree')
    else:
        print("you don't agree")


window = Tk()
x = BooleanVar()
photo = PhotoImage(file='photo.png')

check_button = Checkbutton(window,
                           text='I agree to this',
                           variable=x,
                           onvalue=True,
                           offvalue=0,
                           command=display,
                           font=('Arial', 20),
                           fg="green",
                           bg='black',
                           activeforeground='green',
                           activebackground='black',
                           padx=25,
                           pady=10,
                           image=photo,
                           compound='left')
check_button.pack()
window.mainloop()