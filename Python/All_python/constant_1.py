from bubbleSorting import *
from binarySearch import *

input1 = input("enter number:")
inputarray = [int(x) for x in str(input1)]

x = int(input("num to find: "))

binSearch(inputarray, 0, len(inputarray)-1, x)

result = binSearch(inputarray, 0, len(inputarray) - 1, numtofind)

if result != -1:
    print("number is in the array at index:", str(result))
else:
    print("number is not in the array")