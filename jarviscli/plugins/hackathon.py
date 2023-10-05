import bs4
import requests
import json

from plugin import plugin, require


@require(network=True)
@plugin('hackathon')
class Hackathon():
    """
    Find upcoming hackathons from hackerearth
    """

    def __call__(self, jarvis, s):
        jarvis.say('--- Fetching hackathons--- \n')
        self.format(self.get_hackathon_data(self.get_csrf_token()), jarvis)

    def get_csrf_token(self):
        csrf_request = requests.get('https://www.hackerearth.com/challenges/')

        # extract line with CSRF_COOKIE =
        csrf_token = [line for line in csrf_request.text.split(
            '\n') if 'var CSRF_COOKIE =' in line][0]

        # extract lines between ""
        csrf_token = csrf_token.split('"')[1]
        return csrf_token

    def get_hackathon_data(self, csrf_token):
        headers = {
            'Referer': 'https://www.hackerearth.com/challenges/',
            'X-CSRFToken': csrf_token,
            'X-Requested-With': 'XMLHttpRequest',
        }
        cookie = {'csrftoken': csrf_token}
        request = requests.post(
            'https://www.hackerearth.com/AJAX/filter-challenges/',
            data='',
            headers=headers,
            cookies=cookie)

        return request.text

    def format(self, data, jarvis):
        # parse json
        data = json.loads(data)['data']

        # parse html
        soup = bs4.BeautifulSoup(data, 'lxml')
        upcoming = soup.find('div', {'class': 'upcoming challenge-list'})

        if upcoming is not None:

            all_hackathons = upcoming.find_all(
                'div', {'class': 'challenge-content'})

            for i, hackathon in enumerate(all_hackathons, 1):
                challenge_type = hackathon.find(
                    'div', {'class': 'challenge-type'}).text.replace("\n", " ").strip()
                challenge_name = hackathon.find(
                    'div', {'class': 'challenge-name'}).text.replace("\n", " ").strip()
                date_time = hackathon.find(
                    'div', {
                        'class': 'challenge-list-meta challenge-card-wrapper'}).text.replace(
                    "\n", " ").strip()
                jarvis.say(f"[{str(i)}] {challenge_name}\n{challenge_type}\n{date_time}\n\n")
        else:
            jarvis.say("No hackathon data found.")
