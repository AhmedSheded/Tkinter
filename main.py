from tkinter import *

window = Tk()
# window.geometry("420x420")
window.title("sheded")


icon = PhotoImage(file='photo.png')
window.iconphoto(True, icon)

window.config(background='#5cfcff')


# label
label = Label(window,
              text='Hello world',
              font=('Arial', 40, 'bold'),
              fg='#00ff00',
              bg='black',
              relief=RAISED,
              bd=10,
              padx=20,
              pady=20,
              image=icon,
              compound='bottom'
              )
label.pack()
# label.place(x=100, y=100)
window.mainloop()