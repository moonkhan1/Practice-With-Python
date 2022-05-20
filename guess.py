
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

num = random.randint(1,20)
yguess = 0
count = 0

while yguess != num and yguess != "exit":
    yguess = input("Guess my number !(1-20): ")

    if yguess == "exit":
        break
    while not type(yguess) == int:
        if yguess == "exit":
            break
        try:
            yguess = int(yguess)
        except ValueError:
            yguess = input("Insert number(1-20): ")

        yguess = int(yguess)
        count += 1

        if yguess < num:
            print("Your guess is low")
        elif yguess > num:
            print("Your guess is high")
        else:
            again = input(f" Guess count:  {count}. My number was {num} and guessed it!. Do you want to try again ? Y/N")
            if again == "N" or again == "exit":
                break
            if again == "Y":
                yguess = 0
                count = 0
                num = random.randint(1,20)
