from tkinter import *
from Main import main

m = Tk()
m.title("Auto Toll Window")
ss=-9
def nama():
    global s,ss
    
    nameEE=Label(m,text=("_________________________________________"))
    nameEE.grid(row=4,column=1)
    s = nameE.get()
    nameEE=Label(m,text=("You entered Number Plate = "+s))
    nameEE.grid(row=4,column=1)
    i=1 
    while(i<16):
        ss=main(str(i)+".png")
        print(ss)
        if s!=ss:
            text1="No Match"
            i=i+1
        else:
            text1=("Match found No"+str(i))
            i=i+16

    CHH=Label(m,text=("_________________________________________"))
    CHH.grid(row=3,column=1)
    CHH=Label(m,text=(text1))
    CHH.grid(row=3,column=1)

name=Label(m,text="Number Plate")

nameE=Entry(m)
nameEE=Label(m,text=("_________________________________________"))
namepass=Button(m,text="Enter",command=nama)






name.grid(row=0,column=0)

nameE.grid(row=0,column=1)




namepass.grid(row=0,column=3)


nameEE.grid(row=4,column=1)

m.mainloop()


