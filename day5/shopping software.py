def menu():
    print("======================================")
    print("     WELCOME TO SHOPPING SOFTWARE     ")
    print("======================================")
    print(" SrNO.        Particulars          MRP") 
    print(" 1.           Football             700")
    print(" 2.           Basketball           800")
    print(" 3.           Shoes               2000")
    print(" 4.           Cricket Bat         1200")
    print(" 5.           Skateboard          6550")
    print(" 6.           Cricket Ball         200")
    print(" 7.           Jersey kit          1000")
    print(" 8.           Badminton           1800")
    print("======================================")
    print()
menu()



bill=0
def football():
    print("""Do you  want to buy Football?
======================================
    Type y for yes
    Type n for no
======================================""")
    opt=input()
    global bill 
    if(opt=='y' or opt=='Y'):
        print("Enter quantity: ")
        qnt=int(input())
        amt=qnt*700
        print("Amount: ",amt)
        bill=bill+amt
    elif(opt=='n' or opt=='N'):
        print("Item not selected")
    else:
        print("please enter a valid option")


def basketball():
    print("""Do you  want to buy Basketball?
======================================
    Type y for yes
    Type n for no
======================================""")
    opt=input()
    global bill 
    if(opt=='y' or opt=='Y'):
        print("Enter quantity: ")
        qnt=int(input())
        amt=qnt*800
        print("Amount: ",amt)
        bill=bill+amt
    elif(opt=='n' or opt=='N'):
        print("Item not selected")
    else:
        print("please enter a valid option")


def shoes():
    print("""Do you  want to buy Shoes?
======================================
    Type y for yes
    Type n for no
======================================""")
    opt=input()
    global bill 
    if(opt=='y' or opt=='Y'):
        print("Enter quantity: ")
        qnt=int(input())
        amt=qnt*2000
        print("Amount: ",amt)
        bill=bill+amt
    elif(opt=='n' or opt=='N'):
        print("Item not selected")
    else:
        print("please enter a valid option")


def bat():
    print("""Do you  want to buy Cricket Bat?
======================================
    Type y for yes
    Type n for no
======================================""")
    opt=input()
    global bill 
    if(opt=='y' or opt=='Y'):
        print("Enter quantity: ")
        qnt=int(input())
        amt=qnt*1200
        print("Amount: ",amt)
        bill=bill+amt
    elif(opt=='n' or opt=='N'):
        print("Item not selected")
    else:
        print("please enter a valid option")


def skateboard():
    print("""Do you  want to buy Skateboard?
======================================
    Type y for yes
    Type n for no
======================================""")
    opt=input()
    global bill 
    if(opt=='y' or opt=='Y'):
        print("Enter quantity: ")
        qnt=int(input())
        amt=qnt*6550
        print("Amount: ",amt)
        bill=bill+amt
    elif(opt=='n' or opt=='N'):
        print("Item not selected")
    else:
        print("please enter a valid option")


def ball():
    print("""Do you  want to buy Cricket Ball?
======================================
    Type y for yes
    Type n for no
======================================""")
    opt=input()
    global bill 
    if(opt=='y' or opt=='Y'):
        print("Enter quantity: ")
        qnt=int(input())
        amt=qnt*200
        print("Amount: ",amt)
        bill=bill+amt
    elif(opt=='n' or opt=='N'):
        print("Item not selected")
    else:
        print("please enter a valid option")


def jersey():
    print("""Do you  want to buy Jersey kit?
======================================
    Type y for yes
    Type n for no
======================================""")
    opt=input()
    global bill 
    if(opt=='y' or opt=='Y'):
        print("Enter quantity: ")
        qnt=int(input())
        amt=qnt*1000
        print("Amount: ",amt)
        bill=bill+amt
    elif(opt=='n' or opt=='N'):
        print("Item not selected")
    else:
        print("please enter a valid option")


def badminton():
    print("""Do you  want to buy Badminton?
======================================
    Type y for yes
    Type n for no
======================================""")
    opt=input()
    global bill 
    if(opt=='y' or opt=='Y'):
        print("Enter quantity: ")
        qnt=int(input())
        amt=qnt*1800
        print("Amount: ",amt)
        bill=bill+amt
    elif(opt=='n' or opt=='N'):
        print("Item not selected")
    else:
        print("please enter a valid option")

football()
basketball()
shoes()
bat()
skateboard()
ball()
jersey()
badminton()



disc=0
if(bill>=3000 and bill<5000):
    disc=(bill*5)/100
if(bill>=5000 and bill<10000):
    disc=(bill*10)/100
if(bill>=10000):
    disc=(bill*15)/100

afterdisc=bill-disc
gst=(afterdisc*5)/100
total=afterdisc+gst

print("======================================")
print("===========      BILL    =============")
print("======================================")
print(" Total Amt.                      ",bill)
print(" Discount                        ",disc)
print(" GST                              ",gst)
print(" CGST                           ",gst/2)
print(" SGST                           ",gst/2)
print("======================================")
print(" Final Amount                   ",total)
print("======================================")
print("        THANK YOU FOR SHOPPING        ")
print("======================================")


