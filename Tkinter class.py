from tkinter import *
root=Tk()
class demo:
    def init (self,rootone):
        frame=Frame(rootone)
        frame.pack()
        self.p=Button(frame,text="ok",command=self.printmsg)
        self.p.pack()
        Button(frame,text="exit",command=frame.quit).pack()
    def printmsg(self):
        print("Hiii")
obj=demo(root)
root.mainloop()