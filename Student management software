import mysql.connector

mydb=mysql.connector.connect(host="localhost",
                        user="root",
                        passwd="",
                        database="student")
my=mydb.cursor()

def add():
    l=[]
    print("Please enter the Name ")
    name=input()
    l.append(name)
    print("Please enter the Last Name ")
    lname=input()
    l.append(lname)
    print("Please enter the Address ")
    address=input()
    l.append(address)
    print("Please enter the Phone Number ")
    phn=input()
    l.append(phn)
    print("Please enter the email ")
    email=input()
    l.append(email)
    data=(l)
    sql="insert into t1(name,lname,address,phone,email) values(%s,%s,%s,%s,%s)"
    my.execute(sql,data)
    mydb.commit()
    print("Record added")

def show():
    print("The record of student is ")
    sql="select * from t1"
    my.execute(sql)
    data=my.fetchall()
    for i in data:
        print(i)

def update():
    roll=input("Enter roll no. to update ")
    print(""""Enter your option to update \n1.Name \n2.Lastname \n3.Address \n4.Phone \n5.Email""")
    num=int(input())
    if num==1:
        val=input("Enter new name ")
        sql="update t1 set name=%s where rollno=%s"
        my.execute(sql,(val,roll))
    if num==2:
        val=input("Enter new lastname ")
        sql="update t1 set lname=%s where rollno=%s"
        my.execute(sql,(val,roll))
    if num==3:
        val=input("Enter new address ")
        sql="update t1 set address=%s where rollno=%s"
        my.execute(sql,(val,roll))
    if num==4:
        val=input("Enter new phone ")
        sql="update t1 set phone=%s where rollno=%s"
        my.execute(sql,(val,roll))
    if num==5:
        val=input("Enter new email ")
        sql="update t1 set email=%s where rollno=%s"
        my.execute(sql,(val,roll))
    mydb.commit()
    print("Record updated")

def drop():
    roll=input("Enter roll no to delete ")
    sql="delete from t1 where rollno=%s"
    my.execute(sql,(roll,))
    mydb.commit()
    print("Record deleted")

def menu():
    while(True):
        print("==========================================")
        print("  Welcome to Student Management System ")
        print("==========================================")
        print("::->> Press 1 to Add Student Record")
        print("::->> Press 2 to Show Student Record")
        print("::->> Press 3 to Update Student Record")
        print("::->> Press 4 to Delete Student Record")
        print("===========================================")
        print("Please select the option ......")
        num=int(input())
        if(num==1):
            add()
        if(num==2):
            show()
        if(num==3):
            update()
        if(num==4):
            drop()
        print("Do you want to run the Software Again ...")
        print("Press y for yes ")
        print("Press n for no ")
        ch=input()
        if(ch=='y' or ch=='Y'):
            continue
        if(ch=='n' or ch=='N'):
            print("Software ended salefly....")
            break

menu()
