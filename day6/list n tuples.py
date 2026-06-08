a=[10,20,30,40,50]
l=len(a)
sum=0
for i in range(0,l):
    sum=sum+a[i]
print("Sum = ",sum)



b=[1,2,3,4,5,6,7,8,9,10]
l=len(b)
s1=0
s2=0
for i in range(0,l):
    if(b[i]%2==0):
        s1=s1+b[i]
    else:
        s2=s2+b[i]
print("Sum of even = ",s1)
print("Sum of odd = ",s2)

        
c=[10,20,30,40,50,60]
l=len(c)

for i in range(0,l):
    if(i%2==0):
        b=c[i]
        c[i]=c[i+1]
        c[i+1]=b
print(c)



a=[10,20,30,40,50,60]
b=[11,22,33,44,55,66]
l=len(a)
for i in range(0,l):
    if i%2==0:
        temp=a[i]
        a[i]=b[i]
        b[i]=temp
print(a)
print(b)



a=[10,20,400,60,-10]
l=len(a)
mx=a[0]
mn=a[0]
for i in range(0,l):
    
    if mx<a[i]:
        mx=a[i]
    elif mn>a[i]:
        mn=a[i]
print("max = ",mx)
print("min = ",mn)


#bubble sort
a=[10,20,400,60,-10]
l=len(a)
for j in range(0,l):
    for i in range(0,l-1):
        if a[i]>a[i+1]:
            a[i],a[i+1]=a[i+1],a[i]
print(a)


a=[10,20,30,40,50,60]
b=[11,22,33,44,55,66]
l=len(a)
for i in range(0,l):
    if i%2==0:
        a[i],b[i+1]=b[i+1],a[i]
print(a)
print(b)


a=[10,20,30,40,50,60]
b=[11,22,33,44,55,66]
l=len(a)
for i in range(l):
    if i%2!=0:
        a[i],b[i-1]=b[i-1],a[i]
print(a)
print(b)


a=[10,20,30,40,50,60]
b=[11,22,33,44,55,66]
l=len(a)
for i in range(l):
    if i%2==0:
        a[i],b[i+1]=b[i+1],a[i]
    elif i%2!=0:
        a[i],b[i-1]=b[i-1],a[i]
print(a)
print(b)


#Tupples


c=(10,20,30,40,50,600)
lst=list(c)
l=len(c)

for i in range(0,l):
    if(i%2==0):
        b=lst[i]
        lst[i]=lst[i+1]
        lst[i+1]=b
c=tuple(lst)
print(c)



a=(10,20,30,40,50,60)
b=(11,22,33,44,55,66)
la=list(a)
lb=list(b)
l=len(la)
for i in range(0,l):
    if i%2==0:
        temp=la[i]
        la[i]=lb[i]
        lb[i]=temp
a=tuple(la)
b=tuple(lb)
print(a)
print(b)



#bubble sort
a=(10,20,400,60,-10)
la=list(a)
l=len(la)
for j in range(0,l):
    for i in range(0,l-1):
        if la[i]>la[i+1]:
            la[i],la[i+1]=la[i+1],la[i]
a=tuple(la)
print(a)


a=(10,20,30,40,50,60)
b=(11,22,33,44,55,66)
la=list(a)
lb=list(b)
l=len(a)
for i in range(0,l):
    if i%2==0:
        la[i],lb[i+1]=lb[i+1],la[i]
a=tuple(la)
b=tuple(lb)
print(a)
print(b)


a=(10,20,30,40,50,60)
b=(11,22,33,44,55,66)
la=list(a)
lb=list(b)
l=len(la)
for i in range(l):
    if i%2!=0:
        la[i],lb[i-1]=lb[i-1],la[i]
a=tuple(la)
b=tuple(lb)
print(a)
print(b)


a=(10,20,30,40,50,60)
b=(11,22,33,44,55,66)
la=list(a)
lb=list(b)
l=len(la)
for i in range(l):
    if i%2==0:
        la[i],lb[i+1]=lb[i+1],la[i]
    elif i%2!=0:
        la[i],lb[i-1]=lb[i-1],la[i]
a=tuple(la)
b=tuple(lb)
print(a)
print(b)
