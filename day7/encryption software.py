def enc():
    a=input("Enter the code to encrypt: ")
    l=len(a)
    b=""
    for i in range (l):
            k=ord(a[i])
            p=chr(k+1)
            b+=p
    print("decrypted code: ",b)

            
def dec():
    a=input("Enter the code to decrypt: ")
    l=len(a)
    b=""
    for i in range (l):
            k=ord(a[i])
            p=chr(k-1)
            b+=p
    print("decrypted code: ",b)
def menu():
        print("===========================")
        print("    Welcome to Encryptor Software"     )
        print("===========================")
        print(" press 1 if you want to encrypt the code")
        print(" press 2 if you want to decrypt the code")
        print("===========================")
        print(" Enter your choice:  ")
        opt=int(input())
        if opt==1:
            enc()
        elif  opt==2:
            dec()
        else:
            print("invalid input")
while True:
    menu()

        
        
    
