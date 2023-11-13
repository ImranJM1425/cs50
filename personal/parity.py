""" 
Conditionals statements.
Bools and Modulo (%)
Solution 1 simply checks if the remainder of the calculation returns a 0.
Solution 2 makes use of boolean values True/False in an 'if' conditional.
Solution 3 is the best way to write True/False in python. (smaller, simple code)
"""
## Solution 1
# x = int(input("What's x? "))

# if x % 2 == 0:
#     print("Even")
# else:
#     print("Odd")

# # Solution 2
# def main():
#     x = int(input("Whats x? "))
#     if is_even(x):
#         print("Even")
#     else:
#         print("Odd")

# def is_even(n):
#     if n % 2 == 0:
#         return True
#     else:
#         return False

# main()

# Solution 3
def main():
    x = int(input("Whats x? "))
    if is_even(x):
        print("Even")
    else:
        print("Odd")

def is_even(n):
    return True if n % 2 == 0 else False
    # return n % 2 == 0 #because the answer is either True or False thus if/else is not needed

main()