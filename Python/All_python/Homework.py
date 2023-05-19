from functools import reduce

# -----------------------
#a = []
#num = int(input('How many numbers: '))
# for n in range(num):
#    numbers = int(input('Enter number '))
#    a.append(numbers)
#total = 0
# for i in range(0, len(a)):
#    total = total + a[i]
#total2 = sum(a[:])
#print(total, total2)
#
#
#c = [1, 2, 3, 4, 5]
#
# for i in c[:]:
#    i += 1
#    print(int(c[:i]))

# ---------------------------

#a = []
#n = int(input("Enter the number of elements in list:"))
# for x in range(0, n):
#    element = int(input("Enter element" + str(x+1) + ":"))
#    a.append(element)
#b = set()
#unique = []
# for x in a:
#    if x not in b:
#        unique.append(x)
#        b.add(x)
#print("Non-duplicate items:")
# print(unique)

# ---------------
#import random
#a = []
#
# if len(a) == 0:
#    print("emp")
#
#
#test_list = [1, 4, 5, 6, 3]
#
#print("The original list is : " + str(test_list))
#
# random.shuffle(test_list)
#
#print("The shuffled list is : " + str(test_list))
#
#ran = random.choice(test_list)
#
# print(ran)
#

#global exam_marks
#exam_marks = []
#
#
# class English:
#    def Name(name):
#        name = input("Name:")
#        exam_marks.append(name)
#
#    def Roll_no(roll):
#        roll = input("Roll number:")
#        exam_marks.append(roll)
#
#    def EMarks(marks):
#        marks = 50
#        exam_marks.append(marks)
#
#
# class Maths(English):
#    def Name(name):
#        exam_marks.append(name)
#
#    def Roll_no(roll):
#        exam_marks.append(roll)
#
#    def MMarks(marks):
#        marks = 46
#        exam_marks.append(marks)
#
#
#eng = English()
#mathss = Maths()
#
#
# def English_result():
#    eng.Name()
#    eng.EMarks()
#    eng.Roll_no()
#    print(exam_marks)
#
#
# English_result()
#
#
# def Math_result():
#    mathss.Name()
#    mathss.MMarks()
#    mathss.Roll_no()
#    print(exam_marks)
#
#
# Math_result()


#english_marks = []
#
#math_marks = []
#
#sst_marks = []
#
#
# class exam:
#    def english(self):
#        marks = 50
#        roll = int(input("Roll: "))
#        name = input("Name: ")
#
#        english_marks.append(marks)
#        english_marks.append(name)
#        english_marks.append(roll)
#
#    def maths(self):
#        marks = 30
#        roll = int(input("Roll: "))
#        name = input("Name: ")
#
#        math_marks.append(marks)
#        math_marks.append(name)
#        math_marks.append(roll)
#
#    def sst(self):
#        marks = 40
#        roll = int(input("Roll: "))
#        name = input("Name: ")
#
#        sst_marks.append(marks)
#        sst_marks.append(name)
#        sst_marks.append(roll)
#
#
#exam1 = exam()
#
# exam1.english()
# exam1.maths()
# exam1.sst()
#
#print(english_marks, " ", math_marks, " ", sst_marks)


# def fibonacci(num):
#    num1 = 0
#    num2 = 1
#    series = 0
#    for i in range(num):
#        print(series, end=' ')
#        num1 = num2
#        num2 = series
#        series = num1 + num2
#
#
# running function after takking user input
#num = int(input('Enter how many numbers needed in Fibonacci series- '))
# fibonacci(num)
#

#n = int(input("primes till: "))

# primes = reduce(lambda r, x: r - set(range(x**2, n, x))
#                if x in r else r, range(2, int(n**0.5) + 1), set(range(2, n)))

# print(primes)

#num = []
#prime = []
#
# for i in range(1, n + 1):
#    num.append(i)
# for a in num:
#    if num[a-1] / num[a-1] == 1:
#        prime.append(a)
#
# print(num)
# print(prime)
#

#listA = [['Mon', 3, 'Tue', 7, 'Wed', 4], [
#    'Thu', 5, 'Fri', 11, 'Tue', 7]]
#
#print("Given list of lists : \n", listA)
#
#res = list(set.intersection(*map(set, listA)))
#
#print("The common elements among inners lists : ", res)

def convert(list):
      

    s = [str(i) for i in list]
      

    res = int("".join(s))
      
    return(res)
  

list = [1, 2, 3]
print(convert(list))

L = [1, 2, 3, 4, 5, 6, 7]
li = []
count = 0
for i in L:
    if count % 2 == 1:
        li.append(i)
    count += 1