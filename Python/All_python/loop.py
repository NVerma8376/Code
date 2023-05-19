a=input("-")
b=input("-")
c=input("-")
d=input("-")
e=input("-")
numbers=(int)(a),(int)(b),(int)(c),(int)(d),(int)(e)
sum=0
for val in numbers:
    sum=sum+val
    print(val)
    
print("")
    
for i in range(5):
    print(i)
    
b=0
for i in range(1,5):
    while b <= i:
        print("*")
        b += 1
        
print("")
        
for f in range(5):
    for g in range(4):
        print(g)
        print(" ")
        
maximum=int (input("-"))
for n in range(1, maximum + 1):
    if (n % 2 !=0):
        print(n)
        print("")
my="python"
x=0
for i in my:
    x=x+1
    print(my[0:x])
for i in my:
    x=x-1
    print(my[0:x])