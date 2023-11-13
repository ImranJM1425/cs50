#https://cs50.harvard.edu/python/2022/psets/1/interpreter/
#User Input
math = input("Expression: ")
#Split variables
x, y, z = math.split(" ")
#Convert data to int
xx = int(x)
zz = int(z)
#Calculation and print with 1 decimal place.
if y == "+":
    ans = xx + zz
if y == "-":
    ans = xx - zz
if y == "*":
    ans = xx * zz
if y == "/":
    ans = xx / zz
print (f"{ans:.1f}")