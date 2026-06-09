"""a=[[10,20,30],
   [40,50,60],
   [70,80,90]]
sum=0
for i in range(0,3):
    for j in range(0,3):
        n=(a[i][j])
        sum=sum+n
print(sum)


a=[[10,20,30],
   [40,50,60],
   [70,80,90]]
sum=0
for i in range(0,3):
    for j in range(0,3):
        n=(a[i][j])
        if i==j:
           sum=sum+n
print(sum)
"""


a=[[10,20,30], #0 2
   [40,50,60], #1 1
   [70,80,90]] #2 0
sum=0
for i in range(0,3):
    for j in range(0,3):
        n=(a[i][j])
        if i+j==2:
            sum=sum+n
print(sum)



a=[[10,20,30],#   01
   [40,50,60],#10 11 12
   [70,80,90]]#   31
sum=0
for i in range(0,3):
    for j in range(0,3):
        n=(a[i][j])
        if(i==1 or j==1):
            sum=sum+n
print(sum)


a=[[10,20,30],
   [40,50,60],
   [70,80,90]]
sum=0
for i in range(0,3):
    for j in range(0,3):
        n=(a[i][j])
        if(i!=1 and j!=1):
            sum=sum+n
print(sum)  


a=[[10,20,30],
   [40,50,60],
   [70,80,90]]
s1=s2=s3=s4=s5=s6=0

for i in range(0,3):
    for j in range(0,3):
        if i==0:
            s1=s1+(a[i][j])
        if i==1:
            s2=s2+(a[i][j])
        if i==2:
             s3=s3+(a[i][j])
        if j==0:
            s4=s4+(a[i][j])
        if j==1:
            s5=s5+(a[i][j])
        if j==2:
            s6=s6+(a[i][j])

print("sum of row 1 = ",s1)
print("sum of row 2 = ",s2)
print("sum of row 3 = ",s3)
print("sum of column 1 = ",s4)
print("sum of column 2 = ",s5)
print("sum of column 3 = ",s6)
    



# practice qs

a=[[10,20,30],
   [40,50,60],
   [70,80,90]]

#10 20 30 60 90
for i in range(3):
    for j in range(3):
        if i==0 or j==2:
            print(a[i][j], end=" ")
print()

# 90 60 30 20 10

for i in range(2,-1,-1):
    for j in range(2,-1,-1):
        if i==0 or j==2: 
            print(a[i][j], end=" ")
print()

#10 40 70 80 90

for i in range(3):
    for j in range(3):
        if i==2 or j==0:
            print(a[i][j], end=" ")
print()


#90 80 70 40 10

for i in range(2,-1,-1):
    for j in range(2,-1,-1):
        if i==2 or j==0:
            print(a[i][j], end=" ")
print()


#10 20 30 50 70 80 90

for i in range(3):
    for j in range(3):
        if i==0 or i==j or i==2:
            print(a[i][j], end=" ")
print()
        
#90 80 70 50 30 20 10
for i in range (2,-1,-1):
    for j in range(2,-1,-1):
        if i==0 or i==j or i==2:
            print(a[i][j], end=" ")
print()

        
