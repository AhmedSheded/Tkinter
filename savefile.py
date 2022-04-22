from tkinter import *
from tkinter import filedialog


def save_file():
    file = filedialog.asksaveasfile( #defaultextension='.txt',
                                    filetypes=[
                                        ('Text File', '.txt'),
                                        ('HTML file', '.html'),
                                        ('All Files', '.*')
                                    ],
                                    initialdir='/home/sheded')
    if file is None:
        return
    filetext = str(text.get(1.0, END))
    # filetext = input('Enter some text i guess')
    file.write(filetext)
    file.close()

window = Tk()
button = Button(text='save', command=save_file)
button.pack()
text = Text(window, font=('Ink Free', 20), width=25, height=12)
text.pack()

window.mainloop()