import random
frukter = ("Banan", "Melon", "Kiwi", "Citron")
looping = True

def print_fruit(userinput):
    fnr = int(userinput)
    print("\n" + frukter[fnr-1] + "Kommer här! \n")


while looping:
    print("----------------------------------------------------")
    print("-:Fruktautomat:- \n")

    i=1

    for frukt in frukter:
        print(str(i) + ": " + frukt)
        i+=1

    fruktnr = input("\nMata i nr på frukt du vill ha: ")

    print_fruit(fruktnr)

    go = input("Vill du välja en frukt till? J/N")
    print("\n")

    if (go == "n"):
        break


print("---------------------------------------------------------")
print("Du får en frukt till")
slumpfrukt = random.randint(1, 4)
print_fruit(slumpfrukt)