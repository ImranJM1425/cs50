"""
Functions/variable
"""
# # Ask user for name
# name = input("what's your name? ").strip().title()

# #Split first and last name
# first, last = name.split(" ")
# # Say hello to user
# print (f"hello, {first}")

#Defining hello. To create my own functions
def hello(to="world"):
    print("Hello,", to)

hello()
name = input("What's your name? ").strip().title()
hello(name)
