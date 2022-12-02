import random
from time import sleep, strftime, localtime

from color import color
from information import information

client = information()


class casinos:
    def __init__(self, bot):
        self.bot = bot

    def at(self):
        return f'\033[0;43m{strftime("%d %b %Y %H:%M:%S", localtime())}\033[0;21m'

    # OCF
    def CoinFlip(self, currentbet):
        self.bot.typingAction(str(client.casino['channelcasinoid']))
        sleep(0.6)
        self.bot.sendMessage(str(client.casino['channelcasinoid']), f"owo cf {currentbet}  ".format(currentbet))
        print(f"{self.at()}{color.reset}{color.okcyan} User: {client.username} {color.warning}[SENT]  owo cf {currentbet}  {color.reset}")
        sleep(2)
        sleep(random.randint(1, 4))

    # Owo Slot
    def Slot(self, currentbet):
        self.bot.typingAction(str(client.casino['channelcasinoid']))
        sleep(0.6)
        self.bot.sendMessage(str(client.casino['channelcasinoid']), f"owo s {currentbet}  ".format(currentbet))
        print(f"{self.at()}{color.reset}{color.okcyan} User: {client.username} {color.warning}[SENT]  owo s {currentbet}  {color.reset}")
        sleep(3)
        sleep(random.randint(1, 4))
