from tkinter import *
from Main import main

m = Tk()
m.title("Toll Window")

def nama():
    global s,s1
    s1=1
    nameEE=Label(m,text=("_________________________________________"))
    nameEE.grid(row=4,column=1)
    s = nameE.get()
    nameEE=Label(m,text=("You entered Number Plate = "+s))
    nameEE.grid(row=4,column=1)
def nama1():
    global s1
    nameEE=Label(m,text=("_________________________________________"))
    nameEE.grid(row=5,column=1)
    s1 = nameE1.get()
    nameEE=Label(m,text=("Check Against = "+s1))
    nameEE.grid(row=5,column=1)
   
def inputt():
    global s1
    ss=main(str(s1)+".png")
    print(ss)
    if s==ss:
        text1="Match"
    else:
        text1="No Match"
    CHH=Label(m,text=("_________________________________________"))
    CHH.grid(row=3,column=1)
    CHH=Label(m,text=(text1))
    CHH.grid(row=3,column=1)



name=Label(m,text="Number Plate")
password=Label(m,text="Test")
nameE=Entry(m)
nameEE=Label(m,text=("_________________________________________"))


name1=Label(m,text="Next Plate")
nameE1=Entry(m)


namepass=Button(m,text="Enter",command=nama)
butpass=Button(m,text="Click To Test",command=inputt)

namepass1=Button(m,text="EnterNext",command=nama1)


name.grid(row=0,column=0)
password.grid(row=1,column=0)
nameE.grid(row=0,column=1)

name1.grid(row=2,column=0)
nameE1.grid(row=2,column=1)

namepass.grid(row=0,column=3)
namepass1.grid(row=2,column=3)
butpass.grid(row=1,column=1)
nameEE.grid(row=4,column=1)

m.mainloop()
