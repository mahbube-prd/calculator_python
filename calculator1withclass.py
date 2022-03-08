from email import message
from tkinter import *
from tkinter import messagebox

window=Tk()

class calc():
    def __init__(self,n1,n2):
      
            self.num1=n1
            self.num2=n2
        

    def multiply(self):
        lbl["text"]= self.num1*self.num2

    def divition(self):
         lbl["text"]= self.num1/self.num2    

    def plus(self):
         lbl["text"]=self.num1+self.num2

    def minus(self):
         lbl["text"]=self.num1-self.num2


def calculat(): 

    try:
        a=int(ent1.get())
        b=int(ent2.get())
    except:
        messagebox.showerror(title="error",message="invalid")
    if type(a)==int and type(b)==int:
        obj=calc(a,b)
   
    if var1.get()==1:
        obj.multiply()
    elif var2.get()==1:
        obj.divition()
    elif var3.get()==1:
        obj.plus()
    elif var4.get()==1:
        obj.minus()



Label(window,text="A").place(x=150,y=150)
ent1=Entry()
ent1.place(x=170,y=151)

Label(window,text="B").place(x=350,y=150)
ent2=Entry()
ent2.place(x=370,y=151)
 
lbl=Label(window,text="javab")
lbl.place(x=250,y=200)

var1=IntVar()
Checkbutton(window,text="multiply",variable=var1).place(x=550,y=150)
var2=IntVar()
Checkbutton(window,text="divition",variable=var2).place(x=550,y=170)
var3=IntVar()
Checkbutton(window,text="plus",variable=var3).place(x=550,y=190)
var4=IntVar()
Checkbutton(window,text="minus",variable=var4).place(x=550,y=210)

Button(window,text="calculator",command=calculat).place(x=250,y=250)

window.geometry("900x600")
window.mainloop()