import tkinter as Tk
from tkinter import *
v = Tk() 
v.title("Bill Management") 
v.geometry ("500x800")
v.resizable(False,False)

def Reset():
    entry_dosa.delete(0, END) 
    entry_puri.delete(0, END) 
    entry_idli.delete(0, END) 
    entry_parota.delete(0, END) 
    entry_palav.delete(0, END) 
    entry_tea.delete(0, END) 
    entry_coffee.delete(0, END) 
    
def Total():
    try:a1=int(dosa.get())
    except: a1=0
    
    try:a2=int(puri.get()) 
    except: a2=0
    
    try:a3=int(idli.get()) 
    except: a3=0
    
    try:a4=int(parota.get()) 
    except: a4=0
    
    try:a5=int(palav.get()) 
    except: a5=0
   
    try:a6=int(tea.get()) 
    except: a6=0
    
    try:a7=int(coffee.get()) 
    except: a7=0
#define the cost of each item per quantity
    c1=55*a1
    c2=60*a2
    c3=30*a3
    c4=20*a4
    c5=40*a5
    c6=7*a6
    c7=10*a7
    cost = c1+c2+c3+c4+c5+c6+c7
    lbl_total=Label(f2,font=("aria",20,"bold"),text="Total",width=14,fg="lightyellow",bg="purple") 
    lbl_total.place(x=14,y=50) 
    entry_total=Entry(f2,font=("aria",20,"bold"),textvariable=Total_bill,bd=6,width=13,bg="yellow") 
    entry_total.place(x=18,y=100) 
    
    
    String_bill="Rs:"+str("%.2f" %cost)
    Total_bill.set(String_bill)

Label(text="BILL MANAGEMENT",bg="black",fg="white",font=("calibri",33),width="300",height="2").pack() 


#Menu card
f=Frame(v,bg="lightgreen",highlightbackground="black",highlightthickness=2,width=300, height=470) 
f.place(x=20,y=140) 

Label(f,text="Menu",font=("Gabriola",40,"bold"),fg="black",bg="lightgreen").place(x=80, y=0) 


Label(f,font=("Lucida calligraphy",15,"bold"),text="Dosa..:Rs.55/plate",fg="black",bg="lightgreen").place(x=30,y=90) 
Label(f,font=("Lucida calligraphy",15,"bold"),text="puri..:Rs.60/plate",fg="black",bg="lightgreen").place(x=30,y=120) 
Label(f,font=("Lucida calligraphy",15,"bold"),text="idli..:Rs.30/plate",fg="black",bg="lightgreen").place(x=30,y=150) 
Label(f,font=("Lucida calligraphy",15,"bold"),text="parota..:Rs.20/plate",fg="black",bg="lightgreen").place(x=30,y=180) 
Label(f,font=("Lucida calligraphy",15,"bold"),text="palav..:Rs.40/plate",fg="black",bg="lightgreen").place(x=30,y=210) 
Label(f,font=("Lucida calligraphy",15,"bold"),text="tea..:Rs.7/cup",fg="black",bg="lightgreen").place(x=30,y=240) 
Label(f,font=("Lucida calligraphy",15,"bold"),text="coffee..:Rs.10/cup",fg="black",bg="lightgreen").place(x=30,y=270) 

#Bill
f2=Frame(v,bg="lightyellow",highlightbackground="black",highlightthickness=6,width=310,height=470) 
f2.place(x=760,y=140)

Bill=Label(f2,text="Bill",font=("calibri",20,"bold"), bg="lightyellow") 
Bill.place(x=120,y=10)
 
#entry work
dosa=StringVar() 
puri=StringVar()
idli=StringVar()
parota=StringVar() 
palav=StringVar() 
tea=StringVar()
coffee=StringVar() 
Total_bill=StringVar() 

f1=Frame(v,bd=5,width=150,height=300,relief=RAISED) 
f1.pack()

#label
lbl_dosa=Label(f1,font=("aria",20,"bold"),text="Dosa",width=12,fg="blue4") 
lbl_puri=Label(f1,font=("aria",20,"bold"),text="Puri",width=12,fg="blue4") 
lbl_idli=Label(f1,font=("aria",20,"bold"),text="Idli",width=12,fg="blue4") 
lbl_parota=Label(f1,font=("aria",20,"bold"),text="Parota",width=12,fg="blue4")  
lbl_palav=Label(f1,font=("aria",20,"bold"),text="Palav",width=12,fg="blue4")  
lbl_tea=Label(f1,font=("aria",20,"bold"),text="Tea",width=12,fg="blue4")  
lbl_coffee=Label(f1,font=("aria",20,"bold"),text="Coffee",width=12,fg="blue4")  

lbl_dosa.grid(row=1,column=0) 
lbl_puri.grid(row=2,column=0)
lbl_idli.grid(row=3,column=0)
lbl_parota.grid(row=4,column=0)
lbl_palav.grid(row=5,column=0)
lbl_tea.grid(row=6,column=0)
lbl_coffee.grid(row=7,column=0) 

#entry
entry_dosa=Entry(f1,font=("aria",20,"bold"),textvariable=dosa,bd=6,width=8,bg="lightpink")
entry_puri=Entry(f1,font=("aria",20,"bold"),textvariable=puri,bd=6,width=8,bg="lightpink")
entry_idli=Entry(f1,font=("aria",20,"bold"),textvariable=idli,bd=6,width=8,bg="lightpink")
entry_parota=Entry(f1,font=("aria",20,"bold"),textvariable=parota,bd=6,width=8,bg="lightpink")
entry_palav=Entry(f1,font=("aria",20,"bold"),textvariable=palav,bd=6,width=8,bg="lightpink")
entry_tea=Entry(f1,font=("aria",20,"bold"),textvariable=tea,bd=6,width=8,bg="lightpink")
entry_coffee=Entry(f1,font=("aria",20,"bold"),textvariable=coffee,bd=6,width=8,bg="lightpink") 

entry_dosa.grid(row=1,column=1) 
entry_puri.grid(row=2,column=1)
entry_idli.grid(row=3,column=1)
entry_parota.grid(row=4,column=1)
entry_palav.grid(row=5,column=1) 
entry_tea.grid(row=6,column=1) 
entry_coffee.grid(row=7,column=1)

#buttons
btn_reset=Button(f1,bd=5,fg="black",bg="lightblue",font=("ariel",16,"bold"),width=10,text="Reset",command=Reset) 
btn_reset.grid(row=8,column=0) 

btn_total = Button(f1, bd=5, fg="black", bg="lightblue", font=("ariel", 16, "bold"), width=10, text="Total", command=Total)
btn_total.grid(row=8,column=1)


v.mainloop() 

