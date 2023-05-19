import math
pi=math.pi

while True:    
    print("type cir for volume of cylender or sqr for volume of cube or tri for volume of cone or sph for volume of sphere done to finish")
    type1=str(input("-"))
    if type1 == 'cir':
        radius=int(input("radius="))
        streach=int(input("hight="))
        print("volume=",(pi*radius**2)*streach)

    elif type1 == 'sqr':
        length=int(input("length="))
        print("volume=",length**3)
                
    elif type1 == "tri":
        r=int(input("r="))
        h= int(input("h="))
        print("volume=",(math.pi*r**2)*(h/3))
    
    elif type1 == "sph":
        radius = float(input('Please Enter the Radius of a Sphere: '))
        Volume = (4 / 3) * math.pi * radius * radius * radius
        print("The volume of a Sphere =",Volume)

    elif type1 == "done":
        break

    else:
        print("unknown command")