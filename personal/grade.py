"""
Conditional statements.
if/elif/else and nesting/chaining. 
Solution 1 is a correct and simply method (Checks the lower and upper bounds
of the score).
Solution 2 makes the code cleaner and faster to write by nesting and chaining
the "and" argument (Still checks the lower and upper bounds of the score).
Solution 3 asks only 1 question, "is the score higher than n" and if it's
not, then the next line is asked. (Makes the program faster to run and code)
"""

score = int(input("Score: "))

## Solution 1
# if score >= 90 and score <=100:
#     print("Grade: A")
# elif score >= 80 and score <90:
#     print("Grade: B")
# elif score >= 70 and score <80:
#     print("Grade: C")
# elif score >= 60 and score <70:
#     print("Grade: D")
# else:
#     print("Grade: F")

## Solution 2
# if 90 <= score <=100:
#     print("Grade: A")
# elif 80 <= score <90:
#     print("Grade: B")
# elif 70 <= score <80:
#     print("Grade: C")
# elif 60 <= score <70:
#     print("Grade: D")
# else:
#     print("Grade: F")

## Solution 3
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")