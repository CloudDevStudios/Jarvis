import requests
from colorama import Fore
from plugin import plugin, require

def fetch(route):
    
    url = 'https://api.agify.io?name='
    r = requests.get(url + route)
    r = r.json()
    return None if "errorCode" in r.keys() else r

@require(network=True)
@plugin('age')
class Age():
    
    def __call__(self, jarvis, s):
        option = self.get_option(jarvis)
        if option is None:
            return
        
        r = fetch((str(option)))
        print("Your age is "+str(r["age"]))        
        
        
    def get_option(self, jarvis):
        
        # Ask for the option
        jarvis.say("Give a name :", Fore.BLUE)
        print()
        while True:
            return str(jarvis.input("Enter your choice: ", Fore.GREEN))
        
