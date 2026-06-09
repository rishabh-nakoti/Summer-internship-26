a="computer"
l=len(a)
vowels="aeiou"
v=0
c=0
for i in range(l):
    if a[i] in vowels:
        v+=1
    else:
        c+=1
print("vowels = ",v)
print("consonants = ",c)


a="computer"
l=len(a)
b=""
for i in range(l):
    if a[i] == 'a' or a[i] == 'e' or a[i] == 'i' or a[i] == 'o' or a[i] == 'u':
        b=b+a[i].upper()
    else:
        b=b+a[i]
print(b)


a="computer"
l=len(a)
b=""
vowels="aeiou"
for i in range(l):
    if a[i] in "aeiou":
        print
        b=b+'#'
    else:
        b=b+a[i]
print(b)


a="computer"
l=len(a)
b=""
vowels="aeiou"
for i in range(l):
    if a[i] in vowels:
        k=ord(a[i])
        p=chr(k+1)
        b=b+p
    else:
        k=ord(a[i])
        p=chr(k-1)
        b=b+p
print(b)
        

