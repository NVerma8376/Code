import random
value = 0
total = 0
times = 5

def estimate_pi(n):
    count = 0
    for i in range(n):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        if x**2 + y**2 <= 1:
            count += 1
    global value
    value = (4 * count / n)


n = int(input())

for i in range(times):
    estimate_pi(n)
    print(value)
    total = total + value

print("Average is:",total/times)