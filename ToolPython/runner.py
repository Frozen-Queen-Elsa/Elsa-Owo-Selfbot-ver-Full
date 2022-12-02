from function import functions
from information import information
from time import sleep, strftime, localtime
from color import color
import random
from re import findall, sub

client = information()
function=functions()

class runners:
    def __init__(self, bot):
        self.bot = bot

    def at(self):
        return f'\033[0;43m{strftime("%d %b %Y %H:%M:%S", localtime())}\033[0;21m'

    def hunt(self, username):
        self.bot.typingAction(str(client.channel))
        sleep(1)
        self.bot.sendMessage(str(client.channel), "owoh")

        print(f"{self.at()}{color.reset}{color.okcyan} User: {username}{color.okgreen} [SENT] {color.reset} owo hunt")
        sleep(2)
        sleep(random.randint(1, 2))

    def battle(self, username):
        self.bot.typingAction(str(client.channel))
        sleep(1)
        self.bot.sendMessage(str(client.channel), "owob")
        print(f"{self.at()}{color.reset}{color.okcyan} User: {username}{color.okgreen} [SENT] {color.reset} owo battle")
        sleep(1.2)
        sleep(random.randint(1, 2))

    def owo(self, username):
        self.bot.typingAction(str(client.channel))
        sleep(1)
        self.bot.sendMessage(str(client.channel), "owo")
        print(f"{self.at()}{color.reset}{color.okcyan} User: {username}{color.okgreen} [SENT] {color.reset} owo")
        sleep(1.6)
        sleep(random.randint(1, 2))

    def ring(self, username):
        self.bot.typingAction(str(client.channel))
        sleep(1)
        self.bot.sendMessage(str(client.channel), "owo buy 1")
        print(f"{self.at()}{color.reset}{color.okcyan} User: {username}{color.okgreen} [SENT] {color.reset} owo buy 1")
        sleep(1.9)
        sleep(random.randint(1, 2))

    def praycurse(self, username):
        if client.praycurse['prayother']['enable']:
            self.bot.sendMessage(str(client.channel), f"owo {client.praycurse['mode'].lower()} <@{client.praycurse['prayother']['userid']}>")
            print(
                f"{self.at()}{color.reset}{color.okcyan} User: {username}{color.okgreen} [SENT] {color.reset} owo {client.praycurse['mode'].lower()} ID {color.yellow}{client.praycurse['prayother']['userid']} {color.reset}")
        else:
            self.bot.sendMessage(str(client.channel), f"owo {client.praycurse['mode'].lower()} ")
            print(f"{self.at()}{color.reset}{color.okcyan} User: {username}{color.okgreen} [SENT] {color.reset} owo {client.praycurse['mode'].lower()} ")
            client.totalcmd += 1
            sleep(random.randint(1, 3))

    def daily(self, username):
        self.bot.typingAction(str(client.channel))
        sleep(3)
        self.bot.sendMessage(str(client.channel), "owo daily")
        print(f"{self.at()}{color.reset}{color.okcyan} User: {username}{color.okgreen} [SENT] {color.reset} owo daily")
        sleep(3)
        msgs = self.bot.getMessages(str(client.channel), num=5)
        msgs = msgs.json()
        daily_string = ""
        length = len(msgs)
        i = 0
        while i < length:
            if msgs[i]['author']['id'] == client.OwOID and msgs[i]['content'] != "" and "Nu" or "daily" in msgs[i]['content']:
                daily_string = msgs[i]['content']
                i = length
            else:
                i += 1
        if not daily_string:
            sleep(5)
            self.daily(username)
        else:
            if "Nu" in daily_string:
                daily_string = findall('[0-9]+', daily_string)
                wait_time_daily = str(int(daily_string[0]) * 3600 + int(daily_string[1]) * 60 + int(daily_string[2]))
                print(f"{self.at()}{color.reset}{color.okcyan} User: {username}{color.okblue} [INFO] {color.reset} Next Daily: {wait_time_daily}s")
            elif "Your next daily" in daily_string:
                print(f"{self.at()}{color.reset}{color.okcyan} User: {username}{color.okblue} [INFO] {color.reset} Claimed Daily")
                wait_time_daily = 24 * 3600
            else:
                wait_time_daily = 1800
        return wait_time_daily

    def huntbot(self, username):
        self.bot.typingAction(str(client.channel))
        sleep(3)
        self.bot.sendMessage(str(client.channel), "owo hb 1")
        print(f"{self.at()}{color.reset}{color.okcyan} User: {username}{color.okgreen} [SENT] {color.reset} owo hb 1")

        sleep(3)
        msgs = self.bot.getMessages(str(client.channel), num=5)
        msgs = msgs.json()
        huntbot_string = ""
        length = len(msgs)
        i = 0
        while i < length:
            if msgs[i]['author']['id'] == client.OwOID and msgs[i]['content'] != "":
                if "I WILL BE BACK IN" in msgs[i]['content'] or "I AM BACK WITH" in msgs[i]['content']:
                    huntbot_string = msgs[i]['content']
                    i = length
                else:
                    i += 1
            else:
                i += 1


        if "I WILL BE BACK IN" in huntbot_string:
            huntbot_string = function.substring_after(huntbot_string, "I WILL BE BACK IN ")
            huntbot_string = function.substring_before(huntbot_string, "DONE")
            huntbot_string = function.substring_before(huntbot_string, ":blank:")
            if "H" in huntbot_string:
                hour_huntbot_string = function.substring_before(huntbot_string, "H")
                wait_hour = int(hour_huntbot_string)
                minute_huntbot_string = function.substring_before(function.substring_after(huntbot_string, "H"), "M")
            else:
                wait_hour = 0
                minute_huntbot_string = function.substring_before(huntbot_string,"M")
            minute_huntbot_string = minute_huntbot_string.lstrip()

            wait_minute = int(minute_huntbot_string)
            wait_time_huntbot = wait_hour * 3600 + wait_minute * 60

            print(f"{self.at()}{color.reset}{color.okblue} [INFO] {color.reset} Next Huntbot: {wait_hour}H {wait_minute}M")
            return wait_time_huntbot
        elif "I AM BACK WITH" in huntbot_string:
            print(f"{self.at()}{color.reset}{color.okblue} [INFO] {color.reset} Claimed Huntbot")
            if client.huntbot['sacrifice']['enable'] and client.stopped != True:
                self.bot.typingAction(str(client.channel))
                sleep(3)
                self.bot.sendMessage(str(client.channel), f"owo sc {client.huntbot['sacrifice']['type'].lower()}")
                print(f"{self.at()}{color.reset}{color.okcyan} User: {username}{color.okgreen} [SENT] {color.reset} owo sc {client.huntbot['sacrifice']['type'].lower()}")
            self.bot.typingAction(str(client.channel))
            sleep(3)
            self.bot.sendMessage(str(client.channel), "owo hb 1")
            print(f"{self.at()}{color.reset}{color.okcyan} User: {username}{color.okgreen} [SENT] {color.reset} owo hb 1")
            wait_time_huntbot = 610
            return wait_time_huntbot
        else:
            return 610


    def sell(self, username):
        self.bot.typingAction(str(client.channel))
        sleep(3)
        self.bot.sendMessage(str(client.channel), f"owo sell {client.sell['type']}")
        print(f"{self.at()}{color.reset}{color.okcyan} User: {username}{color.okgreen} [SENT] {color.reset} owo sell {client.sell['type']}")
        sleep(1)

    def changeChannel(self, channels_spam):
        channel2 = []
        for i in channels_spam:
            if channels_spam[i]['type'] == "guild_text":
                channel2.append(i)
        channel2 = random.choice(channel2)
        return channel2, channels_spam[channel2]['name']
