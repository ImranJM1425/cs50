# Loops
#Basic 1
# def main():
#     print_row(4)

# def print_row(width):
#     print("?" * width)

# main()

# # #Basic 2
# def main():
#     print_column(3)

# def print_column(height):
#     for _ in range(height):
#         print("#")

# main()

# Print in 2D solution 1
# def main():
#     print_square(3)

# def print_square(size):
#     #For each row in square
#     for i in range(size):
#         #For each brick in row
#         for j in range(size):
#             print("#", end="")
#         print()
# main()

# # Print in 2D solution 2
# def main():
#     print_square(3)

# def print_square(size):
#     for i in range(size):
#         print("#" * size)

# main()

#Solution 2 expanded
def main():
    print_square(3)

def print_square(size):
    for i in range(size):
        print_row(size)

def print_row(width):
    print("#" * width)

main()