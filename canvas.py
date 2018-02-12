import tkinter
from tkinter import *
root=Tk()
c=Canvas(root,height=500,width=500,bg="red")
c.pack()
c.create_line(450,100,60,120,fill="darkblue",width=3)
c.create_line(450,450,60,120,fill="darkblue",width=3)

root.mainloop()
