from tkinter import *


def submit():
    print('the temprature is: '+str(scale.get())+' degrees C')


window = Tk()
hotImage = PhotoImage(file='photo.png', width=50, height=50)
hotLabel = Label(image=hotImage)
hotLabel.pack()
scale = Scale(window, from_=1000, to=100,
              length=600,
              orient=VERTICAL,
              font=('Consolas', 20),
              tickinterval=10,
              # showvalue=0 #hide curret value
              troughcolor='#69eaff',
              fg='#ff1c00',
              bg='black'
              )
scale.set((scale['from']-scale['to'])/2+scale['to'])
scale.pack()

button = Button(window, text='submit', command=submit)
button.pack()

coldImage = PhotoImage(file='photo.png', width=50, height=50)
coldLabel = Label(image=coldImage)
coldLabel.pack()
window.mainloop()