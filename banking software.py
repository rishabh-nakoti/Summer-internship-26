import mysql.connector
import pandas as pd
mydb=mysql.connector.connect(host="localhost",
                             user="root",
                             password="",
                             database="bank")
mycursor=mydb.cursor()


def Add():
    print("+=========================================+")
    print("    You have selected to add a customer   ")
    print("+=========================================+")
    l=[]
    Accno=int(input("Enter the Account Number: "))
    l.append(Accno)
    Name=input("Enter Customer's Name: ")
    l.append(Name)
    Age=int(input("Enter Customer's Age: "))
    l.append(Age)
    Occup=input("Enter Customer's Occupation: ")
    l.append(Occup)
    Address=input("Enter Customer's Address: ")
    l.append(Address)
    Mob=int(input("Enter Customer's Mobile No.: "))
    l.append(Mob)
    Aadharno=int(input("Enter Customer's Aadhar Number: "))
    l.append(Aadharno)
    Amt=int(input("Enter the Money Deposited: "))
    l.append(Amt)
    Acctype=input("Enter the Account Type (Saving/RD/PPF/Current): ")
    l.append(Acctype)
    cust=(l)
    sql="insert into Account(Accno,Name,Age,Occup,Address,Mob,Aadharno,Amt,Acctype) values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    mycursor.execute(sql,cust)
    mydb.commit()




def View():
    print("+=========================================+")
    print("        Select the Search Criteria        ")
    print("+=========================================+")
    print("1. Acc No. ")
    print("2. Name ")
    print("3. Mobile")
    print("4. Aadhar")
    print("5. View All")
    print("+=========================================+")
    ch=int(input("Enter your choice : "))
    if ch==1:
        s=int(input("Enter Acc no. : "))
        rl=(s,)
        sql="select * from Account where Accno=%s"
        mycursor.execute(sql,rl)
        data=mycursor.fetchall()
        for i in data:
            print(i)

    if ch==2:
        s=input("Enter Name : ")
        rl=(s,)
        sql="select * from Account where Name=%s"
        mycursor.execute(sql,rl)
        data=mycursor.fetchall()
        for i in data:
            print(i)

    if ch==3:
        s=int(input("Enter Mobile no. : "))
        rl=(s,)
        sql="select * from Account where Mob=%s"
        mycursor.execute(sql,rl)
        data=mycursor.fetchall()
        for i in data:
            print(i)

    if ch==4:
        s=int(input("Enter Aadhar no. : "))
        rl=(s,)
        sql="select * from Account where Aadharno=%s"
        mycursor.execute(sql,rl)
        data=mycursor.fetchall()
        for i in data:
            print(i)

    if ch==5:
        sql="select * from Account"
        mycursor.execute(sql)
        res=mycursor.fetchall()
        print("The Customer's Details are as follows : ")
        for x in res:
            k=pd.DataFrame(res,columns=['Accno','Name','Age','Occup','Address','Mob','Aadharno','Amt','Acctype'])
        print(k)



def Deposit():
    print("+=========================================+")
    print("        You have selected to Deposit       ")
    print("+=========================================+")
    l=[]
    Accno=int(input("Enter the Account no. : "))
    l.append(Accno)
    Amtdeposit=eval(input("Enter the Amount to be Deposited : "))
    l.append(Amtdeposit)
    Month=input("Enter the Month of Salary : ")
    l.append(Month)
    cust=(l)
    sql="insert into amt(Accno,AmtDeposit,Month) values(%s,%s,%s)"
    mycursor.execute(sql,cust)
    mydb.commit()
    

def Close():
    print("+=========================================+")
    print("    You have selected to Close an Account  ")
    print("+=========================================+")
    Accno=int(input("Enter the Acc no. : "))
    rl=(Accno,)
    sql="delete from amt where Accno=%s"
    mycursor.execute(sql,rl)
    mydb.commit()
    sql="delete from account where Accno=%s"
    mycursor.execute(sql,rl)
    mydb.commit()
    print("Account",rl," deleted")
    

def Menu():
    ch='y'
    print("+===================================+")
    print("   Welcome to the Banking Sofware    ")
    print("+===================================+")
    while(ch=='y' or ch=='Y'):
        print("Enter 1 to Add the customer")
        print("Enter 2 to View the customer")
        print("Enter 3 to Deposit the money")
        print("Enter 4 to Close an account")
        print("+===================================+")

        try:
            num=int(input("Enter an option from above : "))
        except ValueError:
            exit("\nThats not a number")
        else:
            print("\n")


        if(num==1):
            Add()
        if(num==2):
            View()
        if(num==3):
            Deposit()
        if(num==4):
            Close()
        ch=input("Do you want to continue?????\n (Y/N)?")
Menu()

            
