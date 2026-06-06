def add():
    a=int(input("enter 1st no. "))
    b=int(input("enter 2nd no. "))
    c=a+b
    print("Sum = ",c)

def sub():
    a=int(input("enter 1st no. "))
    b=int(input("enter 2nd no. "))
    c=a-b
    print("subtract = ",c)
    
def mul():
    a=int(input("enter 1st no. "))
    b=int(input("enter 2nd no. "))
    c=a*b
    print("product = ",c)

          
def div():
    a=int(input("enter 1st no. "))
    b=int(input("enter 2nd no. "))
    c=a/b
    print("division = ",c)

          
def menu():
    while(True):
        print("""========================
       Calculator
========================
enter 1 for addition
enter 2 for subtraction
enter 3 for multiplication
enter 4 for division
========================
please select an option""")
        opt=int(input())
        if(opt==1):
            add()
        elif(opt==2):
            sub()
        elif(opt==3):
            mul()
        elif(opt==4):
            div()
        else:
            print("please enter a valid option")
            exit()
        print("do you want to run the code again\n========================")
        print("enter y for yes")
        print("enter n for no\n========================")
        a=input("enter your option")

        if(a=='y' or a=='Y'):
            continue
        if(a=='n' or a=='N'):
            print("thank you for using the calculator")
            break
menu()
            
        

