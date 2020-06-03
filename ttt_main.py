from tkinter import *
from tkinter import ttk
import sqlite3
from tkinter import messagebox
import os

#Creating Directory for database
path=os.environ["userprofile"]
try:
    os.mkdir(path+"\\Documents\\B&B Database")
except FileExistsError:
    pass

con = sqlite3.connect(path+"\\Documents\\B&B Database\main_database.db")
cur = con.cursor()

#Table Names 
ttt="TicTacToe"

root = Tk()

root.title("B&B Game Library")
root.geometry("1920x1080")
state1='disabled'
#state2='disabled'
#state3='disabled'
state3='normal'
allUser = [] #List To store all Users

#Creating Tables
con.execute("create table if not exists TicTacToe (user varchar(20) primary key,password varchar(30),h_s_user varchar(30));")

def gettingDetails():
    
    Id = ent1.get()
    password = ent3.get()
    
    try:
            if (type(int(Id)) == int):
                pass
            else:
                messagebox.showinfo("Invalid Value","Unique ID should be an integer")
                return
    except:
            messagebox.showinfo("Invalid Value","Unique ID should be an integer")
            return
        
    
    sql = "insert into "+ttt+" values ('"+Id+"','"+password+"','" 
    try:
            cur.execute(sql+'0'+"')")
            con.commit()
            messagebox.showinfo("Success", "Successfully registered")
    except:
            messagebox.showinfo("Error inserting","Cannot add data to Database")

    
    ent1.delete(0, END)
    ent3.delete(0, END)
    #ent4.delete(0, END)

def gettingLoginDetails():

    global mode,state1,state2,btn1,btn2,state3

    
    Id = ent1.get()
    password = ent3.get()
    #mode=ent4.get()
    
    sqlLoginID = "select user from "+ttt+" where password = '"+password+"'"
        
    try:
            cur.execute(sqlLoginID)
            for i in cur:
                getLoginID = i[0]
            
            if(getLoginID == Id ):
                messagebox.showinfo("SUCCESS","You have successfully logged in")
                btn1.destroy()
                btn2.destroy()
                
                state1='normal'
                state2='normal'
                state3='normal'
                Menu()
                
            else:
                messagebox.showerror("Failure","Can't log in, check your credentials")
    except:
            messagebox.showinfo("FAILED","Please check your credentials")
            
    
    ent1.delete(0, END)
    ent3.delete(0, END)

def Menu():
    global button1,button2,button3,button4,button5,button6,button6,button7,button8,button9,btn1,btn2
    
    button1=Button(headingFrame, text="", font=('arial',10,'bold'), state=state3)
    button2=Button(headingFrame, text="", font=('arial',10,'bold'), state=state3)
    button3=Button(headingFrame, text="", font=('arial',10,'bold'), state=state3)
    button4=Button(headingFrame, text="", font=('arial',10,'bold'), state=state3)
    button5=Button(headingFrame, text="", font=('arial',10,'bold'), state=state3)
    button6=Button(headingFrame, text="", font=('arial',10,'bold'), state=state3)
    button7=Button(headingFrame, text="", font=('arial',10,'bold'), state=state3)
    button8=Button(headingFrame, text="", font=('arial',10,'bold'), state=state3)
    button9=Button(headingFrame, text="", font=('arial',10,'bold'), state=state3)
    #button1.place(relx=0.87, rely=0.7, relwidth=0.1)
    
    btn1 = Button(moduleFrame,text="Register",font=("arial",12,'bold'),compound = LEFT,command=gettingDetails)
    btn1.place(relx=0,rely=0.17, relwidth=1,relheight=0.12)
    
    btn2 = Button(moduleFrame,text="Tic Tac Toe",font=("arial",12,'bold'), compound= LEFT)#command=ttt,state=state1)
    btn2.place(relx=0,rely=0.44, relwidth=1,relheight=0.12)
    
    
################################## Frames #########################################################################
       
headingFrame = Frame(root,bd=20, relief=RIDGE)
headingFrame.place(relx=0,rely=0,relwidth=1,relheight=0.2)

heading=Label(headingFrame,font=('Times New ROman', 40, 'bold'), text="B&B Game Library")
heading.place(relx=0, rely=0.2)

moduleFrame = Frame(root,bd=20, relief=RIDGE)
moduleFrame.place(relx=0,rely=0.2,relwidth=0.2,relheight=0.8)

headingLabel = Label(moduleFrame, text="MENU",font=("Times New Roman",26,'bold'))
headingLabel.place(relx=0,rely=0, relwidth=1, relheight=0.15)

dFrame= Frame(root,bd=20, relief=RIDGE)
dFrame.place(relx=0.2,rely=0.2,relwidth=0.8,relheight=0.8)

displayFrame=Frame(dFrame, bd=10, relief=SOLID, bg='white')
displayFrame.place(relx=0.05,rely=0.05, relwidth=0.6, relheight=0.9)

scoreFrame=Label(dFrame,bd=10,relief=GROOVE,fg="red",cursor="star")
scoreFrame.place(relx=0.68,rely=0.1,relwidth=0.3,relheight=0.4)

################################################################################

# ID
lb1=Label(headingFrame,text='Unique ID:',font=('arial', 12,'bold'))
lb1.place(relx=0.63, rely=0.01)

ent1=Entry(headingFrame, font=('arial', 12,'bold'))
ent1.place(relx=0.7, rely=0.01, relwidth=0.15)

#Password
lb3=Label(headingFrame,text='Password:',font=('arial', 12,'bold'))
lb3.place(relx=0.63, rely=0.25)

ent3=Entry(headingFrame, font=('arial', 12,'bold'),show="\u2022")
ent3.place(relx=0.7, rely=0.25, relwidth=0.15)

#Role Combobox
lb4=Label(headingFrame,text='Mode:',font=('arial', 12,'bold'))
lb4.place(relx=0.63, rely=0.73)

#ent4=ttk.Combobox(headingFrame, font=('arial', 12, 'bold'), state='readonly', width=23)
#ent4['value']=('','VIP', 'Standard')
#ent4.current(0)
#ent4.place(relx=0.7,rely=0.73,relwidth=0.15)

loginBtn = Button(headingFrame,text="LOGIN", font=("arial",10,'bold'),command=gettingLoginDetails)
loginBtn.place(relx=0.87,rely=0.4, relwidth=0.1)

Menu()
#root.attributes("-topmost", True)
#root.geometry("1520x1080")
#root.resizable(height = False, width = False)
root.title("B&B Game Library")
root.mainloop()
