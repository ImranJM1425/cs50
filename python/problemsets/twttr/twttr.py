#https://cs50.harvard.edu/python/2022/psets/2/twttr/# #Solution 1
# txt = input("Input: ")

# print("Output:",txt.translate({ord(x): None for x in 'aeiouAEIOU'}))


#Solution 2

txt = input("Input: ")

print("Output: ", end="")

for nonvowel in txt:
    if not nonvowel.lower() in ['a','e','i','o','u']:
        print(nonvowel, end="")

print()
