import math


def add():
    print("add")
    a=int(input("-"))
    b=int(input("-"))
    print(a+b)

def sub():
    print("subtract")
    a=int(input("-"))
    b=int(input("-"))
    print(a-b)

def mutiply():
    print("multiply")
    a=int(input("-"))
    b=int(input("-"))
    print(a*b)

def divide():
    print("divide")
    a=int(input("-"))
    b=int(input("-"))
    print(a/b)

def square():
    print("square")
    a=int(input("-"))   
    print(a*a)

def square_root():
    print("square root")
    a=int(input("-"))
    print(math.sqrt(a))

while True:
    add()
    sub()
    mutiply()
    divide()
    square()
    square_root()