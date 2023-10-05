from plugin import plugin
import random
from colorama import Fore


@plugin("guess_number_game")
def helloworld(jarvis, s):
    jarvis.say("Hello let's play  guess the number.", Fore.BLUE)
    jarvis.say("I am thinking of a number between 1-100 and you have to guess it.", Fore.BLUE)
    jarvis.say("Every time you guess, i will inform you if the number you guessed", Fore.BLUE)
    jarvis.say("is bigger or smaller than the one i am thinking.", Fore.BLUE)
    jarvis.say("Let's start the game!", Fore.BLUE)

    num = random.randint(1, 100)
    output = ""
    ##jarvis.say("number is--->", str(num), Fore.BLUE)
    jarvis.say("To Exit the game type exit.", Fore.BLUE)
    jarvis.say("----------------------------", Fore.BLUE)
    hearts = jarvis.input("Choose mode: Hard(6 lives) or Normal(8 lives)", Fore.GREEN)
    hearts = hearts.lower()
    while hearts not in ['hard', 'normal', 'exit']:
        jarvis.say("I can't understand you. Can you tell me again?", Fore.BLUE)
        hearts = jarvis.input("Choose mode: Hard(6 lives) or Normal(8 lives)", Fore.GREEN)
        hearts = hearts.lower()

    lives = 0
    if hearts == 'exit':
        return

    elif hearts == 'hard':
        lives = 6
    elif hearts == 'normal':
        lives = 8
    show(1, 101, jarvis)
    jarvis.say("\n")

    number = jarvis.input("give me a number between(1-100):", Fore.GREEN)
    while not number.isnumeric():
        jarvis.say("Your input was not a number", Fore.BLUE)
        number = jarvis.input("give me a number between(1-100):", Fore.GREEN)
    number = int(number)

    start = 1
    end = 100

    while number != num and lives > 1:
        flag = True
        if num < number and end >= number >= start:
            jarvis.say("The number that i am thinking is smaller than the one you guessed", Fore.BLUE)
            end = number - 1
            show(start, end + 1, jarvis)
        elif num < number or num > number and not end >= number >= start:
            flag = False
        elif num > number:
            jarvis.say("The number that i am thinking is bigger than the one you guessed", Fore.BLUE)
            start = number + 1
            show(start, end + 1, jarvis)
        if flag:
            lives -= 1
            jarvis.say("")
            output = f"make the next guess (lives:{lives})"
        else:
            jarvis.say("Your number is out of bounds")
            output = f"Give a number between[{str(start)}-{str(end)}]"
        jarvis.say(output, Fore.BLUE)
        number = jarvis.input()

        while not number.isnumeric():
            jarvis.say("Your input was not a number", Fore.BLUE)
            number = jarvis.input("give me a number between(1-100):", Fore.GREEN)
        number = int(number)

    if number == num:
        jarvis.say("You found it!", Fore.BLUE)
    elif lives == 1:
        jarvis.say("You lost!", Fore.BLUE)


def show(start, end, jarvis):
    c = 1
    output = ""
    if start > 1:
        for i in range(0, start - 1, 1):
            output += "X   "
            if c % 20 == 0 and i != 0:
                output += "\n"

            c = c + 1
    for i in range(start, end, 1):
        output += f"{str(i)}  "
        if i % 20 == 0:
            output += "\n"
        if i < 10:
            output += " "
        c = c + 1
    if end <= 100:
        for i in range(end, 101, 1):
            output += "X   "
            if c % 20 == 0 and i != 0:
                output += "\n"
            c = c + 1

    jarvis.say(output)
