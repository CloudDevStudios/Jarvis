from plugin import plugin, alias
import os
import json
from colorama import Fore

FILE_PATH = os.path.abspath(os.path.dirname(__file__))


@alias('phone code of',
       'dialing code of')
@plugin('dial code of')
class DialCode:
    """
    Get dial code of a country
    Usage: dial code of <COUNTRY NAME/ COUNTRY CODE>
    Alias(es): phone code of
               dialing code of
    """

    def __call__(self, jarvis, s):
        if code := self.handle_input(s):
            jarvis.say(f'{Fore.GREEN}Dial code is {Fore.WHITE}{code}')
        else:
            # Ask whether to print all available countries if False
            jarvis.say(f"{Fore.RED}Can't find code for country {Fore.WHITE}'{s}'")
            choice = jarvis.input(
                f'{Fore.GREEN}Print avaliable countries?{Fore.WHITE} (y/N): '
            )

            if choice in ['y', 'Y']:
                # Open the file with dial codes
                codes_file = open(os.path.join(FILE_PATH,
                                               "../data/dial_codes.json"), 'r')

                data = json.loads(codes_file.read())

                all_countries = ''
                for i in data:
                    all_countries += i["country_name"]
                    all_countries += ' * '

                jarvis.say(all_countries)

    def handle_input(self, country):

        with open(os.path.join(FILE_PATH,
                                       "../data/dial_codes.json"), 'r') as codes_file:
            # Load json with codes from file
            data = json.loads(codes_file.read())
        return next(
            (
                i["dial_code"]
                for i in data
                if country
                in [i["country_name"].lower(), i["country_code"].lower()]
            ),
            False,
        )


@alias('country with phone code',
       'countries with dial code',
       'countries with phone code',
       'country with dialing code',
       'countries with dialing code')
@plugin('country with dial code')
class CountryByhDC:
    """
    Get country by dial code
    Usage: country with dial code <CODE>
    Alias(es): country with phone code
               countries with dial code
               countries with phone code
               country with dialing code
               countries with dialing code
    """

    def __call__(self, jarvis, s):
        if countries := self.handle_input(s):
            # String from countries list
            countries_str = '; '.join(countries)
            jarvis.say(Fore.GREEN + countries_str)
        else:
            jarvis.say(f"{Fore.RED}Can't find country with code {Fore.WHITE}'{s}'")

    def handle_input(self, code):
        with open(os.path.join(FILE_PATH,
                                       "../data/dial_codes.json"), 'r') as codes_file:
            # Load json from file
            data = json.loads(codes_file.read())
        countries = [
            i["country_name"]
            for i in data
            if code
            in [i["dial_code"].lower(), i["dial_code"].lower().replace('+', '')]
        ]
        return countries if countries else False
