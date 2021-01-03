#!/usr/bin/env python
# coding: utf-8

# In[59]:


import tkinter
from tkinter import *
window=Tk()
e=Entry(window,width=35,bd=10)
e.grid(row=0,column=0,columnspan=3,padx=10,pady=10)
num=""
window.title("Calculator")
window.geometry("290x440")
window.configure(background="blue")
def button_click(number):
    num=e.get()
    e.delete(0,END)
    num=num+str(number)
    e.insert(0,num)
    #hello
    
def button_add():
    
    value1=e.get()
    e.delete(0,END)
    global fnum,i
    i=1
    fnum=int(value1)
    return(value1)
    
def button_div1():
   
    value1=e.get()
    e.delete(0,END)
    global fnum,i
    i=2
    fnum=int(value1)
    return(value1)
    
def button_sub1():
   
    value1=e.get()
    e.delete(0,END)
    global fnum,i
    i=3
    fnum=int(value1)
    return(value1)

def button_mul1():
    
    value1=e.get()
    e.delete(0,END)
    global fnum,i
    i=4
    fnum=int(value1)
    return(value1)
    
def button_equal():
    value2=e.get()
    e.delete(0,END)
    if (i==1):
        e.insert(0,(int(value2)+fnum))
    if (i==2):
        e.insert(0,(fnum/int(value2)))
    if (i==3):
        e.insert(0,(fnum-int(value2)))
    if (i==4):
        e.insert(0,(int(value2)*fnum))
    
def button_clear():
    e.delete(0,END)

   

button_1=Button(window,text='1',command=lambda:button_click(1),bg="blue",activebackground="green",padx=40,pady=20)
button_2=Button(window,text='2',command=lambda:button_click(2),bg="blue",activebackground="green",padx=40,pady=20)
button_3=Button(window,text='3',command=lambda:button_click(3),bg="blue",activebackground="green",padx=40,pady=20)
button_4=Button(window,text='4',command=lambda:button_click(4),bg="blue",activebackground="green",padx=40,pady=20)
button_5=Button(window,text='5',command=lambda:button_click(5),bg="blue",activebackground="green",padx=40,pady=20)
button_6=Button(window,text='6',command=lambda:button_click(6),bg="blue",activebackground="green",padx=40,pady=20)
button_7=Button(window,text='7',command=lambda:button_click(7),bg="blue",activebackground="green",padx=40,pady=20)
button_8=Button(window,text='8',command=lambda:button_click(8),bg="blue",activebackground="green",padx=40,pady=20)
button_9=Button(window,text='9',command=lambda:button_click(9),bg="blue",activebackground="green",padx=40,pady=20)
button_0=Button(window,text='0',command=lambda:button_click(0),bg="blue",activebackground="green",padx=40.5,pady=20)
button_add=Button(window,text='+',command=button_add,bg="blue",activebackground="green",padx=40.45,pady=20)
button_equal=Button(window,text='=',command=button_equal,bg="blue",activebackground="green",padx=86.35,pady=20)
button_clear=Button(window,text='clear',command=button_clear,bg="blue",activebackground="green",padx=79.35,pady=20)
button_mul=Button(window,text='x',command=button_mul1,bg="blue",activebackground="green",padx=40,pady=20)
button_div=Button(window,text='%',command=button_div1,bg="blue",activebackground="green",padx=40,pady=20)
button_sub=Button(window,text='-',command=button_sub1,bg="blue",activebackground="green",padx=40,pady=20)

button_1.grid(row=3,column=0)
button_2.grid(row=3,column=1)
button_3.grid(row=3,column=2)

button_4.grid(row=2,column=0)
button_5.grid(row=2,column=1)
button_6.grid(row=2,column=2)

button_7.grid(row=1,column=0)
button_8.grid(row=1,column=1)
button_9.grid(row=1,column=2)

button_0.grid(row=4,column=0)
button_add.grid(row=5,column=0)
button_equal.grid(row=5,column=1,columnspan=2)
button_clear.grid(row=4,column=1,columnspan=2)
button_mul.grid(row=6,column=0)
button_sub.grid(row=6,column=1)
button_div.grid(row=6,column=2)


window.mainloop()

