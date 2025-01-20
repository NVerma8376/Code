num = int(input("Enter the number: "))

if num == 0:
    print("Number is zero")
else:
    if num % 2 == 0:
        print("Number is even")
    else:
        print("Number is odd")



def is_leap_year(year):
    # A year is a leap year if:
    # 1. It is divisible by 4 and not divisible by 100, OR
    # 2. It is divisible by 400
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    return False

# Input: Get the year from the user
year = int(input("Enter a year: "))

# Output: Check and print the result
if is_leap_year(year):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")


sum1 = 0

for i in range(1,15):
    if i%2!=0:
        sum1 += i
print(sum1)




sum2 = 0

for i in range(1,21):
    if i%2==0:
        sum2 += i
print(sum2)








first_name = input("First name: ")

last_name = input("Last name: ")

full_name = first_name + " " + last_name

print(full_name)




num = int(input("Enter the number: "))
for i in range(1,11):
    print(num,"*",i,"=",num*i)



marks = []

for i in range(5):
    mark = float(input("Mark: "))
    marks.append(mark)

print("The average marks are:", sum(marks)/5)



n = int(input("Enter number: "))

i = 1

while i <= n:
    print(i)
    i += 1



for i in range(5):
    for i in range(i):
        print('*', end=" ")
    print()
    
print("\n")
    


for i in range(5):
    for i in range(5,i,-1):
        print('*', end=" ")
    print()
    

























        
