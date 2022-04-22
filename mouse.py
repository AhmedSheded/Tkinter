from tkinter import *


def doSomthing(event):
    print('click '+str(event.x)+' '+str(event.y))

window = Tk()

window.bind("<Button-1>", doSomthing)


window.mainloop()