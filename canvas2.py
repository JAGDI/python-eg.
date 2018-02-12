import tkinter
from tkinter import*
root= Tk()
l=Label(root,text="login page")
l.grid(row=0,column=2)
l1=Label(root,text="username")
l1.grid(row=1,column=1)
e=Entry(root,bd=2)
e.grid(row=1,column=2)
l2=Label(root,text="password")
l2.grid(row=2,column=1)
e=Entry(root,bd=2,show='*')
e.grid(row=2,column=2)
b=Button(root,text="login",bd=2)
b.grid(row=3,column=1)
print(e)

root.mainloop()
