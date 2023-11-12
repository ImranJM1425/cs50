def main():
    typein = input()
    print (smiley(typein))

def smiley(text):
    return text.replace(":)","🙂").replace(":(","🙁")

main()