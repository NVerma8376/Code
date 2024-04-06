import random

num_of_tries = 3000
x = 4
headavg = 0
tailavg = 0
y = 0
z = 0

def monte_carlo(num):
    head = 0
    tail = 0
    sum = 0
    global y
    for i in range(num):
        x = random.randint(0, 1)
        
        if x == 1:
            head += 1
        elif x == 0:
            tail += 1
        
        sum = head
        
    average = sum / num
    
    if average >= 0.5:
        print("The coin is heads")
        y = y +1
        
    else:
        print("The coin is tails")
        y = y -1
     
        
        

for i in range(x):
    monte_carlo(num_of_tries)
    
if y == 0:
    print("Tie")
    

elif y == 4:
    print("All heads")
    
        
elif y == -4:
    print("All tails")
    
else:
    print("Try again")