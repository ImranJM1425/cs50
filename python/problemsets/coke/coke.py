#https://cs50.harvard.edu/python/2022/psets/2/coke/
i = 50

while i > 0:
    print("Amount Due:",i)
    coin = int(input("Insert Coin: "))
    if coin in [5, 10, 25]:
        i -= coin
else:
    x = abs(i)
    print(f"Change Owed: {x}")