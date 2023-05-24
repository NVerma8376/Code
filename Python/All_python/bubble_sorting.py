import numpy as np

object1 = np.array([7,21,16,87,105,6])


passes = len(object1)   
print(object1)
distro = 3
 
for j in range (0, (int(passes)-1)):
    for i in range(0, int(passes)-1):
        if(object1[i] > object1[i+1]):
            a = object1[i]
            b = object1[i+1]
            object1[i] = b
            object1[i+1] = a
            print(object1)
#print(object)




