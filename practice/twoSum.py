def twoSum(list, num):
    for i in range(len(list)):
        for j in range(i+1, len(list)):
            if list[i] + list[j] == num:
                return [i, j]
    return None

list = input("Enter a list of numbers: ").split()
num = 9

print(twoSum(list, num))