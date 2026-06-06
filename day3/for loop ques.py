#37
#123456789

"""for i in range(1,10):
    print(i,end=" ")
print()


# 2 4 6 8 10 12 14 16 18

for i in range(1,10):
    print(2*i,end=" ")
print()


#1 3 5 7 9 11 13
    
for i in range(0,7):
    print(2*i+1,end=" ")
print()


#1 11 111 1111 11111 111111
j=0
for i in range(1,7):
    j=j*10+1
    print(j,end=" ")
print()

#1 10 100 1000 10000 100000
j=1
for i in range(1,7):
    print(j,end=" ")
    j=10*j
print()


# 1 4 9 16 25 36 49

for i in range(1,8):
    print(i*i,end=" ")


# 2 4 8 16 32 64
n=1
for i in range(1,7):
    n=n*2
    print(n,end=" ")


# 0 3 8 15 24 35
for i in range(1,7):
    print(i*i-1,end=" ")




# 2 5 10 17 26 37
for i in range(1,7):
    print(i*i+1,end=" ")


#0 1 1 2 3 5 8 13 (fibonacci)
a=0
b=1
for i in range(1,9):
    c=a+b
    print(a,end=" ")
    a=b
    b=c
print()

# tribonacci
a=0
b=0
c=1
for i in range(1,9):
    d=a+b+c
    print(a,end=" ")
    a=b
    b=c
    c=d



#38 & 39
n=int(input("enter a no. "))
k=0
for i in range(1,n+1):
  if(n%i==0):
    k=k+1
if(k==2):
  print("prime")
else:
  print("composite")



#41
n=int(input("enter a no. "))
k=0
for i in range(1,n):
    if(n%i==0):
        k=k+i
if(k==n):
    print("perfect no.")
else:
    print("not")



#42
a = int(input("Enter 1st no."))
b = int(input("Enter 2nd no."))
for i in range(a, a * b + 1):
    if i % a == 0 and i % b == 0:
        print("LCM =", i)
        break




#43
a = int(input("Enter 1st no."))
b = int(input("Enter 2nd no."))
hcf=0
for i in range(1,a+1):
    if(a%i==0 and b%i==0):
        hcf=i
print("HCF = ",hcf)
      



#45
for i in range(1,1001):
  k=0
  for j in range(1,i+1):
      if(i%j==0):
        k=k+1
  if(k==2):
        print(i)


"""
#46
for i in range(1,1001):
  k=0
  for j in range(1,i):
      if(i%j==0):
        k=k+j
  if(k==i):
      print(i)