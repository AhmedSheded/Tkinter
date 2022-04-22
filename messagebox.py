from tkinter import *
from tkinter import messagebox


def click():
    # messagebox.showinfo(title='This is an info message box', message='you are a person')

    # while(True):
    #     messagebox.showwarning(title='worning!', message='you have a virus!')

    # messagebox.showerror(title='ERROR!', message='You have an error!')

    # if messagebox.askokcancel(title='ask ok cancel', message='do you want to do the thing'):
    #     print('you did a thing')
    # else:
    #     print('you canceled a thing')

    # if messagebox.askretrycancel(title='ask retry cancel', message='do you wint to retry'):
    #     print('you retry')
    # else:
    #     print('you did not retry')

    # if messagebox.askyesno(title='ask yes or no', message='Do you like cake?'):
    #     print('i like cake to')
    # else:
    #     print('why do you not like cake')

    # answer = messagebox.askquestion(title='ask question', message='do ou like pie?')
    # if (answer == 'yes'):
    #     print('i like pie too')
    # else:
    #     print('why do you not like pie?')

    answer = messagebox.askyesnocancel(title='yes no cancel', message='do you like to code? ', icon='error')
    if (answer==True):
        print("i like to code to")
    elif (answer==False):
        print('why do you not like to code')
    else:
        print('fuck you! ')


window = Tk()
button = Button(window, command=click, text='click me')
button.pack()


window.mainloop()