#38 & 39
n=int(input("enter a no. ")
k=0
for i in range(1,n+1):
  if(n%i==0):
    k=k+1
if(k==2):
  print("prime")
else:
  print("composite")



#41
n=int(input("enter a no. ")
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
hcf=1
for i in range(1,a+1):
    if(a%i==0 and b%i==0):
      hcf=i
print("HCF = ",hcf)



#44
for i in range(1,1001):
  k=0
  for j in range(1,i+1):
      if(i%j==0):
        k=k+1
      if(k==2):
        print(i)



#45
for i in range(1,1001):
  k=0
  for j in range(1,i):
      if(i%j==0):
        k=k+j
  if(k==i):
      print(i)
    
