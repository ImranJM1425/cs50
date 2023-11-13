#https://cs50.harvard.edu/python/2022/psets/0/faces/
def main():
    typein = input()
    print (smiley(typein))

def smiley(text):
    return text.replace(":)","🙂").replace(":(","🙁")

main()