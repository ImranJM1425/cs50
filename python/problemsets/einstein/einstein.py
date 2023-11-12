#Print question and answer
def main():
    mass = int(input("m: "))
    print ("E:", joules(mass))

#Define joules calculation
def joules(e):
    return e * 90000000000000000

main()