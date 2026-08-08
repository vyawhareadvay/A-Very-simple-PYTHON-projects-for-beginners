x: str=(input("What is given? r (Radius) or d (Diameter)"))
if x=="r" or x=="R" :
    print("what is the value of r")
    r=(float(input("r = ")))
    print(3.14*r*r , " This is the area of your circle")
elif x=="d" or x=="D" :
    print(3.14*x/2*x/2*x , " This is the area of your circle")
else:
    print("Try Again ")
