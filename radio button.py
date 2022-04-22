from tkinter import *

food = ['pizaa', 'hamburger', 'hotdog']


def order():
    if(x.get()==0):
        print('you orderd pizza')
    elif(x.get()==1):
        print('you orderd a hamburger')
    elif(x.get()==2):
        print('you orderd a hotdog')
    else:
        print('huh?')


window = Tk()

pizzaImage =PhotoImage(file='photo.png', width=50, height=50)
hamborgerImage = PhotoImage(file='photo.png', width=50, height=50)
hotdogImage = PhotoImage(file='photo.png', width=50, height=50)

foodImages = [pizzaImage, hamborgerImage, hotdogImage]
x = IntVar()
for i in range(len(food)):
    radiobutton = Radiobutton(window,
                              text=food[i], # adds text to radio buttons
                              variable=x, # grops radiobuttons together if they share the same variable
                              value=i, # assings each radiobutton a different value
                              padx= 25, # adds padding on x-axis
                              font=('', 50),
                              image=foodImages[i],
                              compound= 'left',
                              indicatoron=0, # eliminate circleindicators
                              width= 400,  #sets width of radio buttons
                              command=order)

    radiobutton.pack(anchor=W)
window.mainloop()