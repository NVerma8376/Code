import math
while True:    
    a=str(input("="))
    if a == "done":
        break
    m1=float(input("mass1="))
    m2=float(input("mass2="))
    r= float(input("distance="))
    G=6.6726*(10**-11)
    f=(G*m1*m2)/(r**2)
    print("gravitational force=",f,"N" )