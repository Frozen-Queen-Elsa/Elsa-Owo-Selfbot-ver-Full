from information import information
from time import sleep, strftime, localtime
from color import color
import random
from re import findall, sub
client = information()

class gems:
    def __init__(self, bot):
        self.bot = bot

    def at(self):
        return f'\033[0;43m{strftime("%d %b %Y %H:%M:%S", localtime())}\033[0;21m'

    def useGem(self):
        nogem = False
        if client.gem['enable'] and client.stopped != True:
            self.bot.typingAction(str(client.channel))
            sleep(1.5)
            self.bot.sendMessage(str(client.channel), "owo inv")
            print(f"{self.at()}{color.reset}{color.reset}{color.reset}{color.okcyan} User: {client.username}{color.okgreen} [SENT] {color.reset} owo inv")
            sleep(3)
            msgs = self.bot.getMessages(str(client.channel), num=10)
            msgs = msgs.json()
            inv = ""
            for i in range(len(msgs)):
                if msgs[i]['author']['id'] == client.OwOID and 'Inventory' in msgs[i]['content']:
                    inv = findall(r'`(.*?)`', msgs[i]['content'])
            if not inv:
                sleep(2)
                self.useGem()
            else:
                if '050' in inv:
                    if client.gem['lbox'] and client.stopped != True:
                        self.bot.sendMessage(str(client.channel), "owo lb all")
                        print(f"{self.at()}{color.reset}{color.okcyan} User: {client.username}{color.okgreen} [SENT] {color.reset} owo lb all")
                        sleep(10)

                if '100' in inv:
                    if client.gem['wcrate'] and client.stopped != True:
                        self.bot.sendMessage(str(client.channel), "owo crate all")
                        print(f"{self.at()}{color.reset}{color.okcyan} User: {client.username}{color.okgreen} [SENT] {color.reset} owo crate all")
                        sleep(2)
                for item in inv:
                    try:
                        if int(item) >= 100 or int(item) <= 50:
                            inv.pop(inv.index(item))  # weapons
                    except:  # backgounds etc
                        inv.pop(inv.index(item))
                tier = [[], [], []]
                countGem = [0, 0, 0, 0, 0, 0, 0]
                print(f"{self.at()}{color.reset}{color.reset} ===========")

                print(f"{self.at()}{color.reset}{color.okblue} [INFO] {color.reset} Found {len(inv)} Gems Inventory")
                available = []
                for gem in inv:
                    gem = sub(r"[^a-zA-Z0-9]", "", gem)
                    gem = int(gem)
                    for i in range(0, 6, 1):
                        if gem == 51 + i or gem == 65 + i or gem == 72 + i:
                            countGem[i] += 1

                print(f"{self.at()}{color.reset}{color.reset} ===========")

                print(f"{self.at()}{color.reset}{color.okgreen} [INFO] {color.okcyan}\n")
                print(f" 		     Gem C: {countGem[0]} loại\n")
                print(f" 		     Gem U: {countGem[1]} loại\n")
                print(f" 		     Gem R: {countGem[2]} loại\n")
                print(f"		     Gem E: {countGem[3]} loại\n")
                print(f" 		     Gem M: {countGem[4]} loại\n")
                print(f" 		     Gem L: {countGem[5]} loại\n")
                print(f" 		     Gem F: {countGem[6]} loại {color.reset}")
                print(f"{self.at()}{color.reset}{color.reset} ===========")
                sleep(1)

                if client.gem['minmax'].lower() == 'min':
                    for i in range(0, client.gem['maxtier']+1, 1):  # i=4 => Gem Mythic
                        if self.use3gem(i + 1, countGem[i]):
                            nogem = False
                            break
                        else:
                            nogem = True
                if client.gem['minmax'].lower() == 'max':
                    for i in range(client.gem['maxtier'], -1, -1):  # i=4 => Gem Mythic
                        if self.use3gem(i + 1, countGem[i]):
                            nogem = False
                            break
                        else:
                            nogem = True
                if nogem:
                    # print(f"{at()}{color.fail} [INFO] {color.reset} {client.checknogem}")
                    print(f"{self.at()}{color.reset}{color.fail} [INFO] {color.reset} You currently don't have the same set of 3 gems so that you can't use them")
        return nogem

    def use3gem(self,level, count):
        if client.gem['enable'] and client.stopped != True:
            a = 50
            b = 64
            c = 71
            # 1 51 65 72 Common
            # 2 52 66 73 Uncommon
            # 3 53 67 74 Rare
            # 4 54 68 75 Epic
            # 5 55 69 76 Mythic
            # 6 56 70 77 Legend
            # 7 57 71 78 Fabled
            a = a + level
            b = b + level
            c = c + level
            typegem = ""
            turngem = 0
            if level == 1:
                typegem = 'Common'.upper()
                turngem = 25
            if level == 2:
                typegem = 'UnCommon'.upper()
                turngem = 25
            if level == 3:
                typegem = 'Rare'.upper()
                turngem = 50
            if level == 4:
                typegem = 'Epic'.upper()
                turngem = 75
            if level == 5:
                typegem = 'Mythic'.upper()
                turngem = 75
            if level == 6:
                typegem = 'Legend'.upper()
                turngem = 100
            if level == 7:
                typegem = 'Fabled'.upper()
                turngem = 100

            if count == 3:
                sleep(2)
                self.bot.sendMessage(str(client.channel), "owo use {} {} {}".format(str(a), str(b), str(c)))
                print(f"{self.at()}{color.reset}{color.okcyan} User: {client.username}{color.okgreen} [SENT] {color.reset} owo use {a} {b} {c} [GEMS {color.purple}{typegem}{color.reset}][{color.cyan}{str(turngem)} turn{color.reset}]")
                client.checkusegem += 1
                print(f'{self.at()}{color.reset}{color.warning} [INFO] !! [USE GEM lần {client.checkusegem}] !! {color.reset} ')
                return True
            else:
                return False

