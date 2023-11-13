"""
Conditional statements.
Match
Solution 1 is a simple way to determine the House by the name input
using if/elif/else statements.
Solution 2 consolidates the names of those who belong in Gryffindor into
1 'if' statement.
Best solution uses the new 'match' statement. Available in python 3.10+. 
"""

name = input("What's your name? ")

# Best solution for 'match' conditional.
match name:
    case "Harry" | "Hermione" | "Ron":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _:
        print("Who?")

# #Solution 1
# if name == "Harry":
#     print("Gryffindor")
# elif name == "Hermione":
#     print("Gryffindor")
# elif name == "Ron":
#     print("Gryffindor")
# elif name == "Draco":
#     print("Slytherin")
# else:
#     print("Who?")

# # Solution 2
# if name == "Harry" or name == "Hermione" or name == "Ron":
#     print("Gryffindor")
# elif name == "Draco":
#     print("Slytherin")
# else:
#     print("Who?")