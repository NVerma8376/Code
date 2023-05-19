num1=int(input("num1="))
num2=int(input("num2="))
num3=int(input("num3="))

def largest(num1, num2, num3):
    if (num1 > num2) and (num1 > num3):
        largest1=num1

    elif (num2 > num3) and (num2 > num1):
        largest1=num2

    else:
        largest1=num3

    print("largest no.=",largest1)

def smallest(num1, num2, num3):
    if (num1 < num2) and (num1 < num3):
        smallest1=num1
    
    elif (num2 < num1) and (num2 < num3):
        smallest1= num2
    
    else:
        smallest1= num3

    print("smallest no.=",smallest1)

largest(num1, num2, num3)
smallest(num1, num2, num3)