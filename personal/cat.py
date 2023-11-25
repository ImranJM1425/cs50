# Loops. while statements. range
#Meow 3 times.
i = 0
while i < 3:
    print("meow")
    i = i + 1 #or i += 1

#for loop
for i in range(3): #for _ i range(3) can also be used if variable is not important.
    print ("meow")

# Use multiply to print. To concatenate strings.
print ("meow\n" * 3, end="")

# Loop a question infinitely till we get an answer. #1
while True:
    n = int(input("How many meows? "))
    if n < 0:
        continue
    else:
        break

# Loop a question infinitely till we get an answer. #2
while True:
    n = int(input("How many meows? "))
    if n > 0:
        break

for _ in range(n):
    print ("meow")

# Using loops in defining functions 
def main():
    number = get_number()
    meow(number)

def get_number():
    while True:
        n = int(input("How many meows? "))
        if n > 0:
            break  #Can also return n instead of break.
    return n

def meow(n):
    for _ in range(n):
        print("meow")

main()