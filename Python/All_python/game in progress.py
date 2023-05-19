turns=5
words="loop"
fail=0

while turns > 0:
    letter=input("")
    a=1
    for word in words:
        if letter == word:
            a=1
            print(letter)
            break
        else:
            a=0
            fail +=1
    if a != 1:
        print("wrong")
    
    turns -=1
