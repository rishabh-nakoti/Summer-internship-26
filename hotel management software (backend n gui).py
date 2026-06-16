import tkinter as tk
import mysql.connector

mydb=mysql.connector.connect(host="localhost",user="root",passwd="",database="hotel")
my=mydb.cursor()


root=tk.Tk()
root.geometry("1000x600")
root.title("Welcome to Hotel OYO")
#root.config()

def dataTransfer():
    first=EN1.get()
    last=EN2.get()
    sql="insert into t1(fn,ln) values (%s,%s)"
    data=(first,last)
    my.execute(sql,data)
    mydb.commit()
    print("record Added Safely")


def dataGET():

    # NEW WINDOW
    win = tk.Toplevel()

    win.geometry("600x400")

    win.title("All Customer Data")

    # TEXT BOX
    output = tk.Text(
        win,
        font=("Arial",20),
        width=40,
        height=15
    )

    output.pack()

    # DATABASE QUERY
    sql = "select * from t1"

    my.execute(sql)

    result = my.fetchall()

    # SHOW DATA
    for row in result:

        output.insert(tk.END, row[0] + "  ")

        output.insert(tk.END, row[1] + "\n")
    


heading=tk.Label(
    root,
    text=("Hotel management System"),
    font=("poppinsBold",20),
    bg="BLACK",
    fg="WHITE"
    )

heading.place(x=300,y=20)

FN=tk.Label(
    root,
    text=("First Name "),
    font=("Arial",20),
    )
FN.place(x=20,y=80)

EN1=tk.Entry(
    root,
    font=("Arial",20)
    )
EN1.place(x=200,y=80)



LN=tk.Label(
    root,
    text=("Last Name "),
    font=("Arial",20),
    )
LN.place(x=20,y=150)

EN2=tk.Entry(
    root,
    font=("Arial",20)
    )
EN2.place(x=200,y=150)




BTN=tk.Button(
     root,
     text="SAVE DATA ",
     font=("Arial",20),
     command=dataTransfer,
     bg="orange",
     fg="white"
    )

BTN.place(x=200,y=200)




BTN2=tk.Button(
     root,
     text="GET DATA ",
     font=("Arial",20),
     command=dataGET,
     bg="yellow",
     fg="black"
     
    )

BTN2.place(x=430,y=200)
