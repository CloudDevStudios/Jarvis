import requests
import datetime
from plugin import plugin, require
from colorama import Fore
from packages.memory.memory import Memory

URL = "https://api-basketball.p.rapidapi.com/"


@require(network=True)
@plugin("basketball")
class basketball():
    """
    Basketball Plugin for getting information about leagues,games and teams
    !!! needs api.basketball.com API_KEY for usage

    """

    def __call__(self, jarvis, s):
        print("Basketball data provided by the api-basketball.com\n")
        self.get_api_key(jarvis)
        while True:
            option = self.get_option(jarvis)
            if option is None:
                return
            self.procces_chosen_option(option, jarvis)

    def get_headers(self):
        return {"x-rapidapi-host": "api-basketball.p.rapidapi.com", "x-rapidapi-key": self.key}

    def fetch_data(self, route):
        r = requests.get(URL + route, headers=self.get_headers())
        r = r.json()
        return None if "errorCode" in r.keys() else r

    def get_api_key(self, jarvis):
        m = Memory("basketball.json")
        if m.get_data("API_KEY") is None:
            user_api_key = jarvis.input("Enter Api-BasketBall.com API_KEY: ", Fore.GREEN)
            m.add_data("API_KEY", user_api_key)
            m.save()
            self.key = user_api_key
        else:
            self.key = m.get_data("API_KEY")

    def procces_chosen_option(self, option, jarvis):
        if option == "search_team":
            self.search_team(jarvis)
        elif option == "list_leagues":
            self.list_leagues(jarvis)
        elif option == "todays_games":
            self.todays_games(jarvis)
        elif option == "search_league":
            self.search_league(jarvis)
        elif option == "new_key":
            self.update_api_key(jarvis)
        else:
            return

    def update_api_key(self, jarvis,):
        user_api_key = jarvis.input("Enter New Api-BasketBall.com API_KEY: ", Fore.GREEN)
        m = Memory("basketball.json")
        m.update_data("API_KEY", user_api_key)
        m.save()
        self.key = user_api_key

    def list_leagues(self, jarvis):
        jarvis.spinner_start('Fetching...')
        response = self.fetch_data("leagues")
        if response is None:
            jarvis.spinner_stop("Error While Loadin Data - Try Again Later.", Fore.YELLOW)
            return
        total_count = response["results"]
        leagues = response["response"]
        jarvis.spinner_stop(f"Found {total_count} Leagues")
        for i in range(total_count):
            print(f' {i + 1}. {leagues[i]["country"]["name"]} {leagues[i]["name"]}')

    def search_request(self, jarvis, query, search_name):
        value = jarvis.input(f"Enter {search_name} Name: ", Fore.GREEN)
        while len(value.strip()) < 3:
            print()
            print("The Search {} must be at least 3 characters in length", search_name.lower())
            value = jarvis.input(f"Enter {search_name} Name: ", Fore.GREEN)
        jarvis.spinner_start('Searching...')
        response = self.fetch_data(f"{query}?search={value.strip()}")
        if response is None:
            jarvis.spinner_stop(
                f"Error While Searching {search_name} - Try Again Later.",
                Fore.YELLOW,
            )
            return
        return response

    def search_team(self, jarvis):
        response = self.search_request(jarvis, "teams", "Team")
        if response is None:
            return
        found_count = response["results"]
        if found_count == 0:
            jarvis.spinner_stop("Nothing was Found With Given Name", Fore.YELLOW)
            return
        jarvis.spinner_stop(f"Found {found_count} Teams")
        teams = response["response"]
        for i in range(found_count):
            team = teams[i]
            print(f""" {i + 1}. '{team["name"]}' Country: {team["country"]["name"]}""")

    def search_league(self, jarvis):
        response = self.search_request(jarvis, "leagues", "League")
        if response is None:
            return
        found_count = response["results"]
        if found_count == 0:
            jarvis.spinner_stop("Nothing was Found With Given Name", Fore.YELLOW)
            return
        jarvis.spinner_stop(f"Found {found_count} Leagues")
        leagues = response["response"]
        for i in range(found_count):
            league = leagues[i]
            name = league["name"]
            seasons = league["seasons"]
            print(f' {i + 1}. {league["country"]["name"]} {name}')
            if len(seasons) > 0:
                print(f"  Last {len(seasons)} {name} Seasons")
                for j in range(len(seasons)):
                    print(
                        f'   Season: {seasons[j]["season"]} Start: {seasons[j]["start"]} End: {seasons[j]["end"]}'
                    )

    def todays_games(self, jarvis):
        jarvis.spinner_start('Fetching...')
        date = datetime.datetime.now().strftime('%Y-%m-%d')
        response = self.fetch_data(f"games?date={date}")
        if response is None:
            jarvis.spinner_stop("Error While Loading Matches - Try Again Later.", Fore.YELLOW)
            return
        total_count = response["results"]
        matches = response["response"]
        if total_count == 0:
            jarvis.spinner_stop("There is No Matches Today", Fore.YELLOW)
            return
        jarvis.spinner_stop(f"Found {total_count} Matches")
        for i in range(total_count):
            match = matches[i]
            time = match["time"]
            country = match["country"]["name"]
            league = match["league"]["name"]
            teams = f'{match["teams"]["home"]["name"]} VS {match["teams"]["away"]["name"]}'
            print(f" {i + 1}. {country} {league} {time} {teams}")

    def get_option(self, jarvis):
        print()
        jarvis.say("How Can I Help You?", Fore.BLUE)
        print()
        print("1: List Todays Games")
        print("2: Search Team By Name")
        print("3: List All Avaliable Leagues")
        print("4: Search League By Name")
        print("5: Insert New API_KEY")
        print("6: Exit ")
        print()
        choice = self.get_choice(jarvis)
        if choice == -1:
            return
        options = {1: "todays_games", 2: "search_team", 3: "list_leagues", 4: "search_league", 5: "new_key"}

        return options[choice]

    def get_choice(self, jarvis):
        while True:
            try:
                inserted_value = int(jarvis.input("Enter your choice: ", Fore.GREEN))
                if inserted_value == 6:
                    return -1
                elif inserted_value in {1, 2, 3, 4, 5}:
                    return inserted_value
                else:
                    jarvis.say(
                        "Invalid input! Enter a number from the choices provided.", Fore.YELLOW)
            except ValueError:
                jarvis.say(
                    "Invalid input! Enter a number from the choices provided.", Fore.YELLOW)
            print()
