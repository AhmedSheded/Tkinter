from tkinter import *


def open_file():
    print('file has been opend')


def save_file():
    print('file has been saved')


def cut():
    print('you cut some text')


def copy():
    print('you copy some text')


def paste():
    print('you paste some text')


window = Tk()

menubar = Menu(window)
window.config(menu=menubar)

fileMenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label='File', menu=fileMenu)
fileMenu.add_command(label='Open', command=open_file)
fileMenu.add_command(label='Save', command=save_file)
fileMenu.add_separator()
fileMenu.add_command(label='Exit', command=quit)

editMenu=Menu(menubar, tearoff=0, font=('MV Boli', 15))
menubar.add_cascade(label='Edit', menu=editMenu)
editMenu.add_command(label='Cut', command=cut)
editMenu.add_command(label='Copy', command=copy)
editMenu.add_command(label='Paste', command=paste)
window.mainloop()