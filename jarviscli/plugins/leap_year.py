from plugin import plugin


@plugin("leap year")
def leap_year(jarvis, s):
    from collections import namedtuple
    year = int(input("Enter a year: ").strip())
    try:
        year = year
    except:
        jarvis.say('Wrong input. Please make sure you just enter an integer e.g. \'2012\'.')

    leap = (
        (year % 400 == 0)
        and (year % 100 == 0)
        or (year % 4 == 0)
        and (year % 100 != 0)
    )
    if leap:
        jarvis.say(f'{year} is a leap year.')
    else:
        jarvis.say(f'{year} is not a leap year.')
    

