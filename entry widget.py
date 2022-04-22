from tkinter import *


def submit():
    username = entry.get()
    print('hello '+username+'!')
    entry.config(state=DISABLED)

def delete():
    entry.delete(0, END)


def backspace():
    entry.delete(len(entry.get())-1, END)


window = Tk()

entry = Entry(window,
              font=("Arial", 50),
              fg='green',
              bg='black',
              show='*')

# entry.insert(0, 'Spongebob')
entry.pack(side=LEFT)

sumbit_buttom = Button(window, text='submit', command=submit)
sumbit_buttom.pack(side=RIGHT)

delete_buttom = Button(window, text='delete', command=delete)
delete_buttom.pack(side=RIGHT)

backspace_buttom = Button(window, text='backspace_buttom', command=backspace)
backspace_buttom.pack(side=RIGHT)

window.mainloop()