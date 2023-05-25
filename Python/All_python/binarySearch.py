from bubbleSorting import *
import numpy as np

def binSearch(arr, low, high, x):
    if high >= low:
        mid = (high+low) // 2
        
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binSearch(arr, low, mid-1, x)
        else:
            return binSearch(arr, mid+1, high, x)
    
    else:
        return -1
        
result = binSearch(inputarray, 0, len(inputarray) - 1, numtofind)

if result != -1:
    print("number is in the array at index:", str(result))
else:
    print("number is not in the array")