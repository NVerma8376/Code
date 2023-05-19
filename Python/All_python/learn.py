import sys

'''a function inside a class is a method'''

'''keyword argument, positionnal argument'''

'''token: keyword, identifier, constant, symbol'''

'''preccendence:({[]}) > * > / > + > -'''
# keyword cant be a identifier/ variable
a = 1
b = "hi"
c = True
d = None
e = {"hi", "yo"}
d = ["soup", "biryani", "hi", "yo"]
#e = 1+2j
print(d[1:4])


'''f = sys.stdin.readline()
g = input()'''

#print(f, g)

# -------------------------


def pet(first, last):
    full = first + last
    return full


a = pet("a", "z")
print(a)


class computer:

    def hi(self):
        print("hi")


com1 = computer()
com1.hi()
computer.hi(com1)


'''class Person(object):

    # Constructor
    def __init__(self, name):
        self.name = name

    # To get name
    def getName(self):
        return self.name

    # To check if this person is an employee
    def isEmployee(self):
        return False


# Inherited or Subclass (Note Person in bracket)
class Employee(Person):

    # Here we return true
    def isEmployee(self):
        return True


# Driver code
emp = Person("Geek1")  # An Object of Person
print(emp.getName(), emp.isEmployee())

emp = Employee("Geek2")  # An Object of Employee
print(emp.getName(), emp.isEmployee())'''
