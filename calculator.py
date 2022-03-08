from tkinter import *

window=Tk()


def calculat():
    n1=int(ent1.get())
    n2=int(ent2.get())
    if var1.get()==1:
        multiply(n1,n2)
    elif var2.get()==1:
        divition(n1,n2)
    elif var3.get()==1:
        plus(n1,n2)
    elif var4.get()==1:
        minus(n1,n2)

def multiply(a,b):
    lbl["text"]=a*b

def divition(a,b):
    lbl["text"]=a/b    

def plus(a,b):
    lbl["text"]=a+b 

def minus(a,b):
    lbl["text"]=a-b 


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