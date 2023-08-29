def bubbleSort(object1):
    passes = len(object1)   
    distro = 3
 
    for j in range (0, (int(passes)-1)):
        for i in range(0, int(passes)-1):
            if(object1[i] > object1[i+1]):
                a = object1[i]
                b = object1[i+1]
                object1[i] = b
                object1[i+1] = a

    return object1

