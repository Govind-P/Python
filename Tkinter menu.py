from tkinter import *
root=Tk()
def fun():
    print("ok")
mymenu=Menu(root)
root.config(menu=mymenu)
submenu=Menu(mymenu)
mymenu.add_cascade(label="file",menu=submenu)
submenu.add_command(label="save",command=fun)
submenu.add_separator()
submenu.add_command(label="exit",command=exit)
root.mainloop()
