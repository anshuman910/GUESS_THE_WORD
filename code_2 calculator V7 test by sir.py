from tkinter import*
from tkinter import messagebox
import math
root=Tk()
root.title("Calculator V6")
root.geometry('600x300')
selected=IntVar()
frame1 = Frame(root)
frame2 = Frame(root)
frame3 = Frame(root)
flag=0


def clear_n():
    e1.delete(first=0,last='end')
    e1.focus()
    l1.configure(text="Enter the value: ")

def add_n():
    global flag
    flag=1
    try:
        
        equa = e1.get()+"+"
        e1.delete(first=0,last='end')
        e1.insert(0,equa)
    except ValueError:
        messagebox.showerror('Wrong input', 'Enter only number')


def sub_n():
    global flag
    flag=1
    try:
        equa = e1.get()+"-"
        e1.delete(first=0,last='end')
        e1.insert(0,equa)
    except ValueError:
        messagebox.showerror('Wrong input', 'Enter only number')


def dev_n():
    global flag
    flag=1
    try:
        equa = e1.get()+"//"
        e1.delete(first=0,last='end')
        e1.insert(0,equa)
    except ValueError:
        messagebox.showerror('Wrong input', 'Enter only number')


def mul_n():
    global flag
    flag=1
    try:
        equa = e1.get()+"*"
        e1.delete(first=0,last='end')
        e1.insert(0,equa)
    except ValueError:
        messagebox.showerror('Wrong input', 'Enter only number')



def po_n():
    global flag
    flag=1
    try:
        equa = e1.get()+"**"
        e1.delete(first=0,last='end')
        e1.insert(0,equa)
    except ValueError:
        messagebox.showerror('Wrong input', 'Enter only number')




def log_n():
    global flag
    flag=2
    try:
        global s
        equa = float(e1.get())
        e1.delete(first=0,last='end')
        s=math.log10(equa)
        e1.insert(0,"log("+str(equa)+")")
        
        
        

    except ValueError:
        messagebox.showerror('Wrong input', 'Enter number at 1st box only')


def sin_n():
    global flag
    flag=2
    try:
        global s
        equa = float(e1.get())
        e1.delete(first=0,last='end')
        s=math.sin(equa)
        e1.insert(0,"sin("+str(equa)+")")
        
    except ValueError:
        messagebox.showerror('Wrong input', 'Enter number at 1st box only')



def cos_n():
    global flag
    flag=2
    try:
        global s
        equa = float(e1.get())
        e1.delete(first=0,last='end')
        s=math.cos(equa)
        e1.insert(0,"cos("+str(equa)+")")
        
    except ValueError:
        messagebox.showerror('Wrong input', 'Enter number at 1st box only')



def tan_n():
    global flag
    flag=2
    try:
        global s
        equa = float(e1.get())
        e1.delete(first=0,last='end')
        
        s=math.tan(equa)
        e1.insert(0,"tan("+str(equa)+")")
        
    except ValueError:
        messagebox.showerror('Wrong input', 'Enter number at 1st box only')


def exp_n():
    global flag
    flag=2
    try:
        global s
        equa = float(e1.get())
        e1.delete(first=0,last='end')
        s=math.exp(equa)
        e1.insert(0,"exp("+str(equa)+")")
        
    except ValueError:
        messagebox.showerror('Wrong input', 'Enter number at 1st box only')



def mod_n():
    global flag
    flag=2
    try:
        global s
        equa = float(e1.get())
        e1.delete(first=0,last='end')
        s=math.modf(equa)
        e1.insert(0,"mod("+str(equa)+")")
    except ValueError:
        messagebox.showerror('Wrong input', 'Enter number at 1st box only')




def po10_n():
    global flag
    flag=2
    try:
        global s
        equa = float(e1.get())
        e1.delete(first=0,last='end')
        s=math.pow(10,equa)
        e1.insert(0,"10^"+str(equa))
        
    except ValueError:
        messagebox.showerror('Wrong input', 'Enter number at 1st box only')



def pox_n():
    global flag
    flag=2
    try:
        global s
        equa = float(e1.get())
        e1.delete(first=0,last='end')
        
        s=math.pow(equa,2)
        e1.insert(0,str(equa)+"^2")
    except ValueError:
        messagebox.showerror('Wrong input', 'Enter number at 1st box only')



def fact_n():
    global flag
    flag=2
    try:
        global s
        equa = float(e1.get())
        e1.delete(first=0,last='end')
        
        s=math.factorial(equa)
        e1.insert(0,"fact("+str(equa)+")")
        
    except ValueError:
        messagebox.showerror('Wrong input', 'Enter number at 1st box only')







def equal_n():
    if flag==1:
        
        global equa
        equa = e1.get()
        total = str(eval(equa))
        e1.delete(first=0,last='end')
        e1.insert(0,total)
        equa = total
        l1.configure(text="The result is: ")
    elif flag==2:
        e1.delete(first=0,last='end')
        e1.insert(0,s)
        l1.configure(text="The result is: ")
    else:
        equa = e1.get()
        total = str(eval(equa))
        e1.delete(first=0,last='end')
        e1.insert(0,total)
        equa = total
        l1.configure(text="The result is: ")
        
    
        
        
def np_1():
    e1.insert('end',1)
def np_2():
    e1.insert('end',2)
def np_3():
    e1.insert('end',3)
def np_4():
    e1.insert('end',4)
def np_5():
    e1.insert('end',5)
def np_6():
    e1.insert('end',6)
def np_7():
    e1.insert('end',7)
def np_8():
    e1.insert('end',8)
def np_9():
    e1.insert('end',9)
def np_0():
    e1.insert('end',0)




    
l1=Label(frame1,text="Enter the value: ",width=20,height=1)


e1=Entry(frame1)
e1.focus()


l1.grid(row=0,column=0)
e1.grid(row=0,column=1)


b1=Button(frame2,text="Add",command=add_n,activebackground="red",width=10,height=1)
b2=Button(frame2,text="Clear",command=clear_n,activebackground="red",width=10,height=1)
b3=Button(frame2,text="Exit",command=root.destroy,activebackground="red",width=10,height=1)
b4=Button(frame2,text="Subtract",command=sub_n,activebackground="red",width=10,height=1)
b5=Button(frame2,text="Devide",command=dev_n,activebackground="red",width=10,height=1)
b6=Button(frame2,text="Multiply",command=mul_n,activebackground="red",width=10,height=1)
b7=Button(frame2,text="Power",command=po_n,activebackground="red",width=10,height=1)
b8=Button(frame2,text="Log",command=log_n,activebackground="red",width=10,height=1)
b9=Button(frame2,text="Sin",command=sin_n,activebackground="red",width=10,height=1)
b10=Button(frame2,text="Cos",command=cos_n,activebackground="red",width=10,height=1)
b11=Button(frame2,text="Tan",command=tan_n,activebackground="red",width=10,height=1)
b12=Button(frame2,text="Exp",command=exp_n,activebackground="red",width=10,height=1)
b13=Button(frame2,text="Mod",command=mod_n,activebackground="red",width=10,height=1)
b14=Button(frame2,text="10^x",command=po10_n,activebackground="red",width=10,height=1)
b15=Button(frame2,text="x^2",command=pox_n,activebackground="red",width=10,height=1)
b16=Button(frame2,text="Factorial",command=fact_n,activebackground="red",width=10,height=1)
b17=Button(frame2,text="Equal",command=equal_n,activebackground="green",width=10,height=1)



b1.grid(row=4,column=1)
b2.grid(row=4,column=2)
b3.grid(row=4,column=0)
b4.grid(row=5,column=0)
b5.grid(row=5,column=1)
b6.grid(row=5,column=2)
b7.grid(row=6,column=0)
b8.grid(row=6,column=1)
b9.grid(row=6,column=2)
b10.grid(row=7,column=0)
b11.grid(row=7,column=1)
b12.grid(row=7,column=2)
b13.grid(row=8,column=0)
b14.grid(row=8,column=1)
b15.grid(row=8,column=2)
b16.grid(row=9,column=0)
b17.grid(row=0,column=3)




# virtual numpad
np1=Button(frame3,text="1",command=np_1,activebackground="blue",width=4,height=1)
np2=Button(frame3,text="2",command=np_2,activebackground="blue",width=4,height=1)
np3=Button(frame3,text="3",command=np_3,activebackground="blue",width=4,height=1)
np4=Button(frame3,text="4",command=np_4,activebackground="blue",width=4,height=1)
np5=Button(frame3,text="5",command=np_5,activebackground="blue",width=4,height=1)
np6=Button(frame3,text="6",command=np_6,activebackground="blue",width=4,height=1)
np7=Button(frame3,text="7",command=np_7,activebackground="blue",width=4,height=1)
np8=Button(frame3,text="8",command=np_8,activebackground="blue",width=4,height=1)
np9=Button(frame3,text="9",command=np_9,activebackground="blue",width=4,height=1)
np0=Button(frame3,text="0",command=np_0,activebackground="blue",width=4,height=1)






np1.grid(row=10,column=0)
np2.grid(row=10,column=1)
np3.grid(row=10,column=2)
np4.grid(row=11,column=0)
np5.grid(row=11,column=1)
np6.grid(row=11,column=2)
np7.grid(row=12,column=0)
np8.grid(row=12,column=1)
np9.grid(row=12,column=2)
np0.grid(row=13,column=1)
frame1.grid(row=0,column=0)
frame2.grid(row=1,column=0)
frame3.grid(row=1,column=1)








root.mainloop()
