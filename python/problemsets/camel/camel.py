#https://cs50.harvard.edu/python/2022/psets/2/camel/
txt = input("camelCase: ")

print("snake_case: ", end="")

for i in txt:
    if i.isupper():
        print("_" + i.lower(), end="")
    else:
        print(i, end="")