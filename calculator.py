from tkinter import *
import parser
import tkinter.messagebox
root=Tk()

#adding title
root.title("Calculator")

#clear all
def clearall():
    display.delete(0,END)

#digit displaying
i=0
def get_variable(num):
    global i
    display.insert(i,num)
    i+=1

#operators
def get_operation(operator):
    global i
    lenght=len(operator)
    display.insert(i,operator)
    i+=lenght

#clearing one by one
def undo():
    entire_string=display.get()
    if len(entire_string):
        new_string=entire_string[:-1]
        clearall()
        display.insert(0,new_string)
    else:
        clearall()
        tkinter.messagebox.showinfo("Info", "Error")

#calculation
def calculate():
    entire_string=display.get()
    try:
        a=parser.expr(entire_string).compile()
        result=eval(a)
        clearall()
        display.insert(0,result)
    except Exception:
        clearall()
        tkinter.messagebox.showinfo("Info","Error")


#getting display
display=Entry(root)
display.grid(row=1,columnspan=4)

#getting button
Button(root,text="c",command=lambda :undo()).grid(row=2,column=0)
Button(root,text="(",command=lambda :get_operation("(")).grid(row=2,column=1)
Button(root,text=")",command=lambda :get_operation(")")).grid(row=2,column=2)
Button(root,text="/",command=lambda :get_operation("/")).grid(row=2,column=3)
Button(root,text="7",command=lambda :get_variable(7)).grid(row=3,column=0)
Button(root,text="8",command=lambda :get_variable(8)).grid(row=3,column=1)
Button(root,text="9",command=lambda :get_variable(9)).grid(row=3,column=2)
Button(root,text="*",command=lambda :get_operation("*")).grid(row=3,column=3)
Button(root,text="4",command=lambda :get_variable(4)).grid(row=4,column=0)
Button(root,text="5",command=lambda :get_variable(5)).grid(row=4,column=1)
Button(root,text="6",command=lambda :get_variable(6)).grid(row=4,column=2)
Button(root,text="-",command=lambda :get_operation("-")).grid(row=4,column=3)
Button(root,text="1",command=lambda :get_variable(1)).grid(row=5,column=0)
Button(root,text="2",command=lambda :get_variable(2)).grid(row=5,column=1)
Button(root,text="3",command=lambda :get_variable(3)).grid(row=5,column=2)
Button(root,text="+",command=lambda :get_operation("+")).grid(row=5,column=3)
Button(root,text="AC",command=lambda :clearall()).grid(row=6,column=0)
Button(root,text="0",command=lambda :get_variable(0)).grid(row=6,column=1)
Button(root,text=".",command=lambda :get_variable(".")).grid(row=6,column=2)
Button(root,text="=",command=lambda :calculate()).grid(row=6,column=3)



root.mainloop()