while True:    
    type=str(input("type="))
    if type == "F":
        F=float(input("F="))
        print("C=",(F-32)/1.8000)

    elif type == "C":
        C=float(input("C="))
        print("F=",(C*1.8000)+32)

    elif type == "done":
        break

    else:
        print("command not found")
        