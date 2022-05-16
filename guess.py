
"""import random

rd = random.randint(1,9)
guess = 0
c = 0
while guess != rd and guess != "exit":
    guess = input("Enter a guess between 1 to 9")

    if guess == "exit":
        break

    guess = int(guess)
    c += 1

    if guess < rd:
        print("Too low")
    elif guess > rd:
        print("Too high")
    else:
        print("Right!")
        print("You took only", c, "tries!")
input()"""

import random

nomre = random.randint(1,20)
texmin = 0
saygac = 0

while texmin != nomre and texmin != "cixis":
    texmin = input("Aglimda tutdugum reqemi tap(1-20): ")

    if texmin == "cixis":
        break
    while not type(texmin) == int:
        if texmin == "cixis":
            break
        try:
            texmin = int(texmin)
        except ValueError:
            texmin = input("Reqem daxil et(1-20): ")

        texmin = int(texmin)
        saygac += 1

        if texmin < nomre:
            print("Texmininiz kicikdir")
        elif texmin > nomre:
            print("Texmininiz boyukdur")
        else:
            tekrar = input(f"Siz {saygac} qeder texmin etdiniz ve menim tutdugum {nomre} reqemin tapdiniz. Yeniden ceh etmek isdeyirsiz? H/Y")
            if tekrar == "y" or tekrar == "cixis":
                break
            if tekrar == "h":
                texmin = 0
                saygac = 0
                nomre = random.randint(1,20)
