"""a=[10,20,30,40,50]
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
"""


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
