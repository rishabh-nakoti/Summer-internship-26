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



        


        



        
