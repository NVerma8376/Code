import math

#binary to decimal
binaryIntInput = input("enter binary number:")
binary = [int(x) for x in str(binaryIntInput)]
power = len(binary)
base10 = 0
for y in range(0, len(binary)):
    base10 = binary[y] * math.pow(2, power-1) + base10
    power = power - 1
    
print(base10)    

#decimal to binary
decimalIntInput = int(input("enter decimal number:"))
deci = decimalIntInput
binaryarr = []
for l in range(0, decimalIntInput):
    divi = int(deci%2)
    binaryarr.append(divi)
    deci = int(deci / 2)
    if (deci == 0):
        break
binaryOut = []   
for j in range(len(binaryarr)-1, -1, -1):
    binaryOut.append(binaryarr[j])

for g in binaryOut:
    print(g, end="")
    
print("")

