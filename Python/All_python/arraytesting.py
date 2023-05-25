
input1 = input("enter number:")
inputarray = [int(x) for x in str(input1)]
reversed_array = [int(x) for x in str(input1)]
length = len(inputarray)

for i in range(0, length):
    re = inputarray[i]
    reversed_array[(length-1) - i] = re
    
print(inputarray)
print(reversed_array)

conjoined = ""
for j in range(0, length):
    toBeAdded = str(reversed_array[j])
    conjoined = conjoined + toBeAdded
    
print(conjoined)