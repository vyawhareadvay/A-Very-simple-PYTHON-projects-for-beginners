import math
weight=int(input("Please enter your weight :      "))
unit=str(input("(K)g's  or  (L)b's :            "))
if unit == "K" or unit=="k" :
    weight=weight*2.205
    print("Your weight in pounds is    ", weight)
elif unit == "L" or unit=="l":
    weight=weight / 2.205
    print("Your weight in kilograms is    ", weight)
else:
    print("Your unit must br in K/k or L/l")
print("Thank you")
math.