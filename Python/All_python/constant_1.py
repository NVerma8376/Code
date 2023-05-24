import math

def logx(x):
    if x == 0:
        return - 100
    return math.log(x)

print(logx(16))