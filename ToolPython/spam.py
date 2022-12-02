from information import information
from time import sleep, strftime, localtime
from color import color
from requests import get,post
import random
from re import findall, sub
client = information()

class spam:
    def __init__(self, bot):
        self.bot = bot

    def at(self):
        return f'\033[0;43m{strftime("%d %b %Y %H:%M:%S", localtime())}\033[0;21m'

    def exp(self,channel_spam,username):

        try:
            response = get("https://quote-garden.herokuapp.com/api/v3/quotes/random")
            if response.status_code == 200:
                json_data = response.json()
                data = json_data['data']
                self.bot.sendMessage(str(channel_spam), data[0]['quoteText'])
                print(f'{self.at()}{color.reset}{color.okcyan} User: {username}{color.okcyan} [SPAM] {color.reset}')
                client.totaltext += 1
                sleep(random.randint(1, 6))
        except:
            pass