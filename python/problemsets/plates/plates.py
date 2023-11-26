#https://cs50.harvard.edu/python/2022/psets/2/plates/
def main():
    plate = input("Plate: ").upper()
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if len(s) < 2 or len(s) > 6:
        return False
    if s[0].isdigit() or s[1].isdigit():
        return False
    for char in s:
        if not char.isalnum():
            return False
# Iterates through each letter, and if 'i', while 'i' is less than the length
# of the string, is not an alphabet but is a digit, and the digit is a 0, then
# return false. If 'i', the first digit encountered in the string is not a 0, 
# then the next step, check if the next iteration of the string is not a digit,
# then return false. If the first digit encountered is not a 0 and the following
# string are also digits, then return True.
    i = 0
    while i < len(s):
        if not s[i].isalpha():
            if s[i] == "0":
                return False
            elif not s[i:].isdigit():
                return False
            else:
                return True
        i += 1       
        
    return True


main()