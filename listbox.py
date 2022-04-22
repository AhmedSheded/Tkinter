from tkinter import *


def submit():
    food = []
    for i in listbox.curselection():
        # food.insert(i, listbox.get(i))
        food.append(listbox.get(i))

    print('You have ordered: ')
    for i in food:
        print(i)

    # order = listbox.get(listbox.curselection())
    # print('you have ordered '+order)


def add():
    listbox.insert(listbox.size(), entryBox.get())
    entryBox.delete(0, END)
    listbox.config(height=listbox.size())


def delete():
    for i in reversed(listbox.curselection()):
        listbox.delete(i)

    # listbox.delete(listbox.curselection())
    listbox.config(height=listbox.size())


window = Tk()

listbox = Listbox(window,
                  bg='#f7ffde',
                  font=('Constantia', 30),
                  width=12,
                  selectmode=MULTIPLE
                  )
listbox.pack()

food = ['pizza', 'pasta', 'tea', 'soup', 'salad']
for i, item in enumerate(food):
    listbox.insert(i, item)

listbox.config(height=listbox.size())

entryBox = Entry(window)
entryBox.pack()

addButton = Button(window, text='add', command=add)
addButton.pack()


submitButton = Button(window, text='submit', command=submit)
submitButton.pack()

deleteButton = Button(window, text='delete', command=delete)
deleteButton.pack()

window.mainloop()