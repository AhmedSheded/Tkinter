from tkinter import *
from tkinter.ttk import *
import time


def start():
    GB = 130
    download = 0
    speed = 1
    while(download<GB):
        time.sleep(0.05)
        bar['value']+=(speed/GB)*100
        download+=speed
        percent.set(str(int(download/GB*100))+'%')
        text.set(str(download)+'/'+str(GB)+" GB completed")
        window.update_idletasks()

window = Tk()

percent =StringVar()
text = StringVar()

# s = Style()
# s.theme_use('green')


bar = Progressbar(window, orient=HORIZONTAL, length=400)
bar.pack(pady=10)

percentLabel = Label(window, textvariable=percent).pack()

taskLabel = Label(window, textvariable=text).pack()


button = Button(window, text='download', command=start).pack()


window.mainloop()