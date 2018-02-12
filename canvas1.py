import tkinter
from tkinter import *
root=Tk()
c=Canvas(root,height=500,width=500,bg="red")
c.pack()
c.create_rectangle(450,50,50,450,fill="green")
c.create_rectangle(400,100,100,400,fill="yellow")
c.create_oval(400,100,100,400,fill="blue")
root.mainloop()
