from tkinter import *
root=Tk()
f=Frame(root)
f.pack()
def fun():
    print("Hello")
Button(f,text="login",bg="red",command=fun).pack()
Button(f,text="exit",bg="red",command=exit).pack()
root.mainloop()
