#https://cs50.harvard.edu/python/2022/psets/1/bank/
# Solution with startswith() function.
greet = input("Greeting: ").lower().strip()

if greet.startswith("hello"):
    print("$0")
elif greet.startswith("h"):
    print("$20")
else:
    print("$100")