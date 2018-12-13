import math
print("Welcome the Hypotenuse Calculator!")
one = int(input("What's the first side of your triangle?: "))
two = int(input("What's the second side of your triangle?: "))

y = one**2 + two**2
c = y**.5

print(f"Your hypotenuse is {c}")