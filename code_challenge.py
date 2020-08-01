from tkinter import *
from tkinter import messagebox as m

root=Tk()
root.title("Employee details system")
root.geometry('900x450+0+0')
root.configure(background="blue")

Tops=Frame(root,width=1350,height=50,bd=8,bg="powder blue")
Tops.pack(side=TOP)

f1=Frame(root,width=600,height=600,bd=8,bg="powder blue")
f1.pack(side=LEFT)
f2=Frame(root,width=300,height=700,bd=8,bg="powder blue")
f2.pack(side=RIGHT)

fla=Frame(f1,width=600,height=200,bd=8,bg="powder blue")
fla.pack(side=TOP)
flb=Frame(f1,width=300,height=600,bd=8,bg="powder blue")
flb.pack(side=TOP)

lblinfo=Label(Tops,font=('arial',45,'bold'),text="Employee Details" ,bd=10,fg="green")
lblinfo.grid(row=0,column=0)

def exit():
  exit=tkinter.messagebox.askyesno("Employee system","Do you want to exit the system")
  if exit>0:
    root.destroy()
    return
def save():
    #db=pymysql.connection()
    N=etxname.get()
    Emp=etxEmployeeNo.get()
    S=etxstreet.get()
    c=etxstate.get()
    co=etxcode.get()

    s=N+ ' ,'+Emp+','+S+','+c+','+co+'\n'
    #s='insert into employeedetails values({},{},{},{},{})'.format()
    f=open("Employeedeatails.csv",'a+')
    f.write(s)
    f.close()
    m.showinfo("save","REcord added")  


def reset():
  Name.set("")
  EmployeeNo.set("")
  street.set("")
  city.set("")
  state.set("")
  code.set("")
  
def enterinfo():
  txt.delete("1.0",END)
  txt.insert(END,"Name :\t\t"+Name.get()+"\n\n")
  txt.insert(END," Employee No:\t\t"+EmployeeNo.get()+"\n\n")
  txt.insert(END,"street :\t\t"+street.get()+"\n\n")
  txt.insert(END," city :\t\t"+city.get()+"\n\n")
  txt.insert(END," state :\t\t"+state.get()+"\n\n")
  txt.insert(END," code:\t\t"+code.get()+"\n\n")
  

#Variables
Name=StringVar()
EmployeeNo=StringVar()
street=StringVar()
city=StringVar()
state=StringVar()
code=StringVar()


# Label 

lblName=Label(fla,text="Name",font=('arial',16,'bold'),bd=20,fg="red",bg="powder blue").grid(row=0,column=0)
lblEmployeeNo=Label(fla,text="EmployeeNo",font=('arial',16,'bold'),bd=20,fg="red",bg="powder blue").grid(row=0,column=2)
lblstreet=Label(fla,text="street",font=('arial',16,'bold'),bd=20,fg="red",bg="powder blue").grid(row=1,column=0)
lblcity=Label(fla,text="city",font=('arial',16,'bold'),bd=20,fg="red",bg="powder blue").grid(row=1,column=2)
lblstate=Label(fla,text="state",font=('arial',16,'bold'),bd=20,fg="red",bg="powder blue").grid(row=2,column=0)
lblcode=Label(fla,text="code",font=('arial',16,'bold'),bd=20,fg="red",bg="powder blue").grid(row=2,column=2)


# Entry  

etxname=Entry(fla,textvariable=Name,font=('arial',16,'bold'),bd=16,width=22,justify='left')
etxname.grid(row=0,column=1)

etxEmployeeNo=Entry(fla,textvariable=EmployeeNo,font=('arial',16,'bold'),bd=16,width=22,justify='left')
etxEmployeeNo.grid(row=0,column=3)

etxstreet=Entry(fla,textvariable=street,font=('arial',16,'bold'),bd=16,width=22,justify='left')
etxstreet.grid(row=1,column=1)

etxcity=Entry(fla,textvariable=city,font=('arial',16,'bold'),bd=16,width=22,justify='left')
etxcity.grid(row=2,column=1)

etxstate=Entry(fla,textvariable=state,font=('arial',16,'bold'),bd=16,width=22,justify='left')
etxstate.grid(row=2,column=3)

etxcode=Entry(fla,textvariable=code,font=('arial',16,'bold'),bd=16,width=22,justify='left')
etxcode.grid(row=1,column=3)

#buttons
btnsave=Button(flb,text='Save details',padx=16,pady=16,bd=8,font=('arial',16,'bold'),width=14,command=save,fg="red",bg="powder blue").grid(row=0,column=5)
btnexit=Button(flb,text='Exit System',padx=16,pady=16,bd=8,font=('arial',16,'bold'),width=14,command=exit,fg="red",bg="powder blue").grid(row=0,column=3)

root.mainloop()


