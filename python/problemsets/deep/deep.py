# Solution 1
ans = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ").strip()
if ans == "42" or ans.lower() == "forty-two" or ans.lower() == "forty two":
    print("Yes")
else:
    print("No")

# # Solution 2 using define function
# def main():
#     ans = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ").lower().strip()
#     check(ans)

# def check(x):
#     if x == "42" or x == "forty two" or x == "forty-two":
#         print("Yes")
#     else:
#         print("No")

# main()

# # Solution 3 using match function
# def main():
#     answer = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ").lower().strip()

#     match answer:
#         case "42" | "forty-two" | "forty two":
#             print("Yes")
#         case _:
#             print("No")

# main()