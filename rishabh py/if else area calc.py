print("""========================
Enter Y to start
Enter N to cancel
========================""")
strt=input()
if(strt=='Y' or strt=='y'):
    print("""========================
Enter 1 for area of rectangle
Enter 2 for area of square
Enter 3 for cube
Enter 4 for cuboid
Enter 5 for circle
========================""")
    num=int(input())
    if(num==1):
        print("You have slected area of rectangle")
        a=int(input("enter length."))
        b=int(input("enter breadth."))
        rect=a*b
        print("Area of Rectangle = ",rect)
    elif(num==2):
        print("You have slected area of square")
        a=int(input("enter the side of square"))
        sq=a*a
        print("Area of square = ",sq)
    elif(num==3):
        print("you have selected area of cube")
        a=int(input("enter the side of the cube"))
        cube=6*a*a
        print("area of cube = ",cube)
    elif(num==4):
        print("you have selected area of cuboid")
        a=int(input("enter length"))
        b=int(input("enter breadth"))
        c=int(input("enter height"))
        cuboid=a*b*c
        print("area of cuboid = ",cuboid)
    elif(num==5):
        print("you have selected area of circle")
        r=int(input("enter radius"))
        circle=3.14*r*r
        print("area of circle = ",circle)
    else:
        print("enter a valid option")
        exit()
elif(strt=='n' or strt=='N'):
    print("thankyou!")
else:
    print("enter a valid option")
    exit()            
