"""
Conditional statements.
if / elif / else. 
Solution 1 requires the program to ask the question 3 times no matter if the 
answer is found or not. (Not well designed). Makes the process run too long. 
Solution 2 is a shorter process where the program stops once the answer is 
found unless x == y.
Solution 3 makes the process even shorter where if x is not less/greater than y,
then x is equal to y.
Solution 4 makes the program even more optimized and shorter. Only 1 question
is asked, "is x equal to y?". Makes the code and process more compact.
"""

x = int(input("What's x? "))
y = int(input("What's y? "))

## Solution 1
# if x < y:
#     print ("x is less than y")
# if x > y:
#     print("x is greater than y")
# if x == y:
#     print("x is equal to y")

## Solution 2
# if x < y:
#     print ("x is less than y")
# elif x > y:
#     print("x is greater than y")
# elif x == y:
#     print("x is equal to y")

## Solution 3
# if x < y:
#     print ("x is less than y")
# elif x > y:
#     print("x is greater than y")
# else:
#     print("x is equal to y")

## Solution 4
if x != y:
    print("x is not equal to y")

else:
    print("x is equal to y")