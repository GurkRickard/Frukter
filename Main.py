import random
frukter = ("Banan", "Melon", "Kiwi", "Citron")
looping = True

def print_fruit(userinput):
    fnr = int(userinput)
    print("\n" + frukter[fnr-1] + "Kommer här!")


while looping:
    go = input("Vill du välja en frukt till? J/N")
    print("\n")

    if (go == "n"):
        break
