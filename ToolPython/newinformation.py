from menu import UI
from json import load, dump
from time import sleep
from color import color
import time
from version import version

ui = UI()
elsa = '''\
███████╗██╗     ███████╗ █████╗                                                           
██╔════╝██║     ██╔════╝██╔══██╗                                                          
█████╗  ██║     ███████╗███████║                                                          
██╔══╝  ██║     ╚════██║██╔══██║                                                          
███████╗███████╗███████║██║  ██║                                                          
╚══════╝╚══════╝╚══════╝╚═╝  ╚═╝                                                          

 ██████╗ ██╗    ██╗ ██████╗     ███████╗███████╗██╗     ███████╗██████╗  ██████╗ ████████╗
██╔═══██╗██║    ██║██╔═══██╗    ██╔════╝██╔════╝██║     ██╔════╝██╔══██╗██╔═══██╗╚══██╔══╝
██║   ██║██║ █╗ ██║██║   ██║    ███████╗█████╗  ██║     █████╗  ██████╔╝██║   ██║   ██║   
██║   ██║██║███╗██║██║   ██║    ╚════██║██╔══╝  ██║     ██╔══╝  ██╔══██╗██║   ██║   ██║   
╚██████╔╝╚███╔███╔╝╚██████╔╝    ███████║███████╗███████╗██║     ██████╔╝╚██████╔╝   ██║   
 ╚═════╝  ╚══╝╚══╝  ╚═════╝     ╚══════╝╚══════╝╚══════╝╚═╝     ╚═════╝  ╚═════╝    ╚═╝   
'''


# [0] Exit And Save"
# [1] Change All Settings"
# [2] Change Token"
# [3] Change Channel"
# [4] Change Sleep Mode"
# [5] Change Exp Mode"
# [6] Change Auto Setting"
# [7] Change Pray/Curse Mode"
# [8] Change Sell Mode"
# [9] Change Prefix Mode"
# [10] Change Gem Mode"
# [11] Change Casino Mode"
# [12] Change Sound Mode"
# [13] Change Webhook Setting"
# [14] Change Solve Captcha Setting"
# [15] Change TwoCaptcha Setting"
# [16] Change HuntBot Mode"

def main():
    with open("..\src\owosettings.json", "r") as f:
        data = load(f)
    print(f'{color.okcyan}{elsa}{color.reset}')
    print(f"                   {color.purple}Version: {version} {color.reset}")
    time.sleep(0.5)
    print()
    print(f"{color.warning}")
    ui.newData()
    print(f"{color.reset}")
    choice = input(f"{color.okcyan}Enter Your Choice:  {color.okgreen}")
    if choice == "0":
        print(f"{color.reset}")
        pass
    elif choice == "1":
        token(data, True)
        channel(data, True)
        sleep(data, True)
        exp(data, True)
        runner(data, True)
        praycurse(data, True)
        sell(data, True)
        prefix(data, True)
        gem(data, True)
        casino(data, True)
        sound(data, True)
        webhook(data, True)
        solve(data, True)
        twocaptcha(data, True)

    elif choice == "2":
        token(data, False)
    elif choice == "3":
        channel(data, False)
    elif choice == "4":
        sleep(data, False)
    elif choice == "5":
        exp(data, False)
    elif choice == "6":
        runner(data, False)
    elif choice == "7":
        praycurse(data, False)
    elif choice == "8":
        sell(data, False)
    elif choice == "9":
        prefix(data, False)
    elif choice == "10":
        gem(data, False)
    elif choice == "11":
        casino(data, False)
    elif choice == "12":
        sound(data, False)
    elif choice == "13":
        webhook(data, False)
    elif choice == "14":
        solve(data, False)
    elif choice == "15":
        twocaptcha(data, False)
    elif choice == "16":
        huntbot(data, False)
    else:
        print(f"{color.fail}[INFO] {color.reset}Invalid Choice")


def token(data, all):
    print("")
    data['token'] = input(f"{color.okcyan}Please Enter Your Account Token: {color.yellow}")
    file = open("owosettings.json", "w")
    dump(data, file, indent=4)
    file.close()
    print(f"{color.okgreen}[INFO] {color.okcyan}Successfully Saved!{color.reset}")
    if not all:
        main()


def channel(data, all):
    print("")
    data['channel'] = input(f"{color.okcyan}Please Enter Your Channel ID: {color.yellow}")
    file = open("..\src\owosettings.json", "w")
    dump(data, file, indent=4)
    file.close()
    print(f"{color.okgreen}[INFO] {color.okcyan}Successfully Saved!{color.reset}")
    if not all:
        main()


def sleep(data, all):
    print("")
    data['sleep']['enable'] = input(f"{color.okcyan}Toggle Sleep Mode (YES/NO): {color.yellow}")
    if data['sleep']['enable'].lower() == 'yes':
        data['sleep']['time'] = input(f"{color.okcyan}Please enter the time the bot is active before sleeping: {color.yellow}")
        if data['sleep']['time'].isdigit():
            data['sleep']['time'] = int(data['sleep']['time'])
        else:
            print(f'{color.fail}Wrong input')
            sleep(data, all)
        data['sleep']['duration'] = input(f"{color.okcyan}Please enter the time the bot sleeps: {color.yellow}")
        if data['sleep']['duration'].isdigit():
            data['sleep']['duration'] = int(data['sleep']['time'])
        else:
            print(f'{color.fail}Wrong input')
            sleep(data, all)
        data['sleep']['enable'] = True
    else:
        data['sleep']['enable'] = False
    file = open("..\src\owosettings.json", "w")
    dump(data, file, indent=4)
    file.close()
    print(f"{color.okgreen}[INFO] {color.okcyan}Successfully Saved!{color.reset}")
    if not all:
        main()


def exp(data, all):
    print("")
    data['exp']['enable'] = input(f"{color.okcyan}Toggle Automatically Send Random Text To Level Up (YES/NO): {color.yellow}")
    if data['exp']['enable'].lower() == 'yes':
        data['exp']['channelspamid'] = input(f"{color.okcyan}Input channel id you want to spam exp(should be a private server): {color.yellow}")
        data['exp']['changechannel'] = input(f"{color.okcyan}Toggle Automatically change channel spam to get more exp (YES/NO): {color.yellow}")
        if data['exp']['changechannel'].lower() == 'yes':
            data['exp']['channelchannel'] = True
        elif data['exp']['changechannel'].lower() == 'no':
            data['exp']['channelchannel'] = False
        else:
            print(f'{color.warning}Invalid Input')
            exp(data, all)

        data['exp']['enable'] = True
    else:
        data['exp']['enable'] = False
    file = open("..\src\owosettings.json", "w")
    dump(data, file, indent=4)
    file.close()
    print(f"{color.okgreen}[INFO] {color.okcyan}Successfully Saved!{color.reset}")
    if not all:
        main()


def runner(data, all):
    print("")
    data['runner']['hunt'] = input(f"{color.okcyan}Do you want to owo hunt automatic? (YES/NO): {color.yellow}")
    data['runner']['battle'] = input(f"{color.okcyan}Do you want to owo battle automatic? (YES/NO): {color.yellow}")
    data['runner']['daily'] = input(f"{color.okcyan}Do you want to claim daily automatic? (YES/NO): {color.yellow}")
    data['runner']['owo'] = input(f"{color.okcyan}Do you want to say owo automatic? (YES/NO): {color.yellow}")
    data['runner']['ring'] = input(f"{color.okcyan}Do you want to buy ring (item1) automatic? (YES/NO): {color.yellow}")
    if data['runner']['hunt'].lower() == 'yes':
        data['runner']['hunt'] = True
    else:
        data['runner']['hunt'] = False
    if data['runner']['battle'].lower() == 'yes':
        data['runner']['battle'] = True
    else:
        data['runner']['battle'] = False
    if data['runner']['daily'].lower() == 'yes':
        data['runner']['daily'] = True
    else:
        data['runner']['daily'] = False
    if data['runner']['owo'].lower() == 'yes':
        data['runner']['owo'] = True
    else:
        data['runner']['owo'] = False
    if data['runner']['ring'].lower() == 'yes':
        data['runner']['ring'] = True
    else:
        data['runner']['ring'] = False
    file = open("..\src\owosettings.json", "w")
    dump(data, file, indent=4)
    file.close()
    print(f"{color.okgreen}[INFO] {color.okcyan}Successfully Saved!{color.reset}")
    if not all:
        main()


def praycurse(data, all):
    print("")
    data['praycurse']['enable'] = input(f"{color.okcyan}Toggle Automatically Send Pray/Curse/No (YES/NO): {color.yellow}")
    if data['praycurse']['enable'].lower() == 'yes':
        data['praycurse']['mode'] = input(f"{color.okcyan}Do you want to Pray or Curse (PRAY/CURSE): {color.yellow}")
        if data['praycurse']['mode'].lower() == 'pray' or data['praycurse']['mode'].lower() == 'curse':
            data['praycurse']['mode'] == data['praycurse']['mode'].lower()
        else:
            print(f"{color.fail}WRONG INPUT")
            praycurse(data, all)
        data['praycurse']['prayother']['enable'] = input(f"{color.okcyan}Do you want to Pray or Curse to other player? (YES/NO): {color.yellow}")
        if data['praycurse']['prayother']['enable'].lower() == 'yes':
            data['praycurse']['prayother']['userid'] = input(f"{color.okcyan}Input player Id which you want to pray/curse to: {color.yellow}")
            data['praycurse']['prayother']['enable'] = True
        else:
            data['praycurse']['prayother']['enable'] = False
        data['praycurse']['enable'] = True
    else:
        data['praycurse']['enable'] = False

    file = open("..\src\owosettings.json", "w")
    dump(data, file, indent=4)
    file.close()
    print(f"{color.okgreen}[INFO] {color.okcyan}Successfully Saved!{color.reset}")
    if not all:
        main()


def sell(data, all):
    print("")
    data['sell']['enable'] = input(f"{color.okcyan}Toggle Automatically Sell Animal (YES/NO): {color.yellow}")
    if data['sell']['enable'].lower() == "yes":
        print(f"{color.warning}Animal Type: C, U, R, E, M, L, F, ... (Type \"all\" To Sell All Animals)")
        print(f"{color.warning}C = Common, U = Uncommon, ect...")
        data['sell']['type'] = input(f"{color.okcyan}Enter Animal Type: {color.yellow}")
        data['sell']['enable'] = True
    else:
        data['sell']['enable'] = False
    file = open("..\src\owosettings.json", "w")
    dump(data, file, indent=4)
    file.close()
    print(f"{color.okgreen}[INFO] {color.okcyan}Successfully Saved!{color.reset}")
    if not all:
        main()


def prefix(data, all):
    print("")
    data['prefix']['enable'] = input(f"{color.okcyan}Toggle Selfbot Commands, You Can Control Your Selfbot Using Commands (YES/NO): {color.yellow}")
    if data['prefix']['enable'].lower() == "yes":
        data['prefix']['key'] = input(f"{color.okcyan}Enter Your Selfbot Prefix: {color.yellow}")
        data['allowedid'] = input(f"{color.okcyan}Do You Want Allow An User To Use Your Selfbot Commands? If Yes Enter The Account ID, Otherwise Enter \"None\": {color.yellow}")
        data['prefix']['enable'] = True
        print(f"{color.warning}Great! You Can View Selfbot Commands At Option [3] Info At The Main Menu!")

    else:
        data['prefix']['enable'] = False
    file = open("..\src\owosettings.json", "w")
    dump(data, file, indent=4)
    file.close()
    print(f"{color.okgreen}[INFO] {color.okcyan}Successfully Saved!{color.reset}")
    if not all:
        main()


def gem(data, all):
    print("")
    data['gem']['enable'] = input(f"{color.okcyan}Toggle Automatically Use Gems Mode (YES/NO): {color.yellow}")
    if data['gem']['enable'].lower() == "yes":
        data['gem']['wcrate'] = input(f"{color.okcyan}Toggle Automatically Open Weapon Crate Mode (YES/NO): {color.yellow}")
        data['gem']['lbox'] = input(f"{color.okcyan}Toggle Automatically Open Loot Box Mode (YES/NO): {color.yellow}")
        data['gem']['minmax'] = input(f"{color.okcyan}Do You Prefer Using Gems From MIN Or MAX  [MIN/MAX]: {color.yellow}")
        if data['gem']['minmax'].lower()=='min' or data['gem']['max'].lower()=='max':
            data['gem']['minmax']=data['gem']['minmax'].lower()
        else:
            print(f"{color.fail}WRONG INPUT")
            gem(data, all)
        data['gem']['maxtier'] = input(f"{color.okcyan}Which best Gems do you prefer to use [F/L/M/E/R/C/U]: {color.yellow}")
        if data['gem']['maxtier'].lower() == 'f':
            data['gem']['maxtier'] = 7

        elif data['gem']['maxtier'].lower() == 'l':
            data['gem']['maxtier'] = 6

        elif data['gem']['maxtier'].lower() == 'm':
            data['gem']['maxtier'] = 5

        elif data['gem']['maxtier'].lower() == 'e':
            data['gem']['maxtier'] = 4

        elif data['gem']['maxtier'].lower() == 'r':
            data['gem']['maxtier'] = 3

        elif data['gem']['maxtier'].lower() == 'c':
            data['gem']['maxtier'] = 2

        elif data['gem']['maxtier'].lower() == 'u':
            data['gem']['maxtier'] = 1

        else:
            print(f"{color.fail}Invalid Input{color.reset}")
            gem(data, all)

        if data['gem']['wcrate'].lower() == 'yes':
            data['gem']['wcrate'] = True
        else:
            data['gem']['wcrate'] = False
        if data['gem']['lbox'].lower() == 'yes':
            data['gem']['lbox'] = True
        else:
            data['gem']['lbox'] = False
        data['gem']['enable'] = True
    else:
        data['gem']['enable'] = False
    file = open("..\src\owosettings.json", "w")
    dump(data, file, indent=4)
    file.close()
    print(f"{color.okgreen}[INFO] {color.okcyan}Successfully Saved!{color.reset}")
    if not all:
        main()


def casino(data, all):
    print("")
    data['casino']['enable'] = input(f"{color.okcyan}Do you want to play Casino (YES/NO): {color.yellow}")
    if data['casino']['enable'].lower() == "yes":
        data['casino']['channelcasinoid'] = input(f"{color.okcyan}Enter Casino Channel Id {color.yellow}")
        data['casino']['maxbet'] = input(f"{color.okcyan}Are you prefer all in to die or reset bet when the bet > 150k ? (AllIn/Reset): {color.yellow}")
        if data['casino']['maxbet'].lower() == 'allin' or data['casino']['maxbet'] == 'reset':
            data['casino']['maxbet'] = data['casino']['maxbet'].lower()
        else:
            print(f'{color.fail}Invalid Input')
            casino(data, all)
        data['casino']['cf']['enable'] = input(f"{color.okcyan}Do you want to play CoinFlip (YES/NO/): {color.yellow}")
        if data['casino']['cf']['enable'].lower() == 'yes':
            print(f"{color.okgreen}[INFO] {color.warning}Input Coinflip Information")
            data['casino']['cf']['bet'] = input(f"{color.okcyan}Enter Your Bet Amount for CoinFlip (Must Be Integer): {color.yellow}")
            if data['casino']['cf']['bet'].isdigit() == False:
                print(f'{color.okgreen}Wrong input{color.reset}')
                casino(data, all)
            else:
                data['casino']['cf']['bet'] = int(data['casino']['cf']['bet'])

            data['casino']['cf']['rate'] = input(f"{color.okcyan}Enter Your Bet Rate Multiple for CoinFlip (Ngã ở đâu x? ở đó) (Best is x4) (x2 is not good) (Must Be Integer): {color.yellow}")
            if data['casino']['cf']['rate'].isdigit() == False:
                print(f'{color.okgreen}Wrong input{color.reset}')
                casino(data, all)
            else:
                data['casino']['cf']['rate'] = int(data['casino']['cf']['rate'])

            data['casino']['cf']['enable'] = True
        else:
            data['casino']['cf']['enable'] = False

        data['casino']['os']['enable'] = input(f"{color.okcyan}Do you want to play Owo Slot (YES/NO/): {color.yellow}")
        if data['casino']['os']['enable'].lower() == 'yes':
            print(f"{color.okgreen}[INFO] {color.warning}Input Coinflip Information")
            data['casino']['os']['bet'] = input(f"{color.okcyan}Enter Your Bet Amount for OwoSlot (Must Be Integer): {color.yellow}")
            if data['casino']['os']['bet'].isdigit() == False:
                print(f'{color.okgreen}Wrong input{color.reset}')
                casino(data, all)
            else:
                data['casino']['os']['bet'] = int(data['casino']['os']['bet'])
            data['casino']['os']['rate'] = input(f"{color.okcyan}Enter Your Bet Rate Multiple for OwoSlot (Ngã ở đâu x? ở đó) (Best is x3) (x2 is not good) (Must Be Integer): {color.yellow}")
            if data['casino']['os']['rate'].isdigit() == False:
                print(f'{color.okgreen}Wrong input{color.reset}')
                casino(data, all)
            else:
                data['casino']['os']['rate'] = int(data['casino']['os']['rate'])
            data['casino']['os']['enable'] = True
        else:
            data['casino']['os']['enable'] = False
        data['casino']['enable'] = True
    else:
        data['casino']['enable'] = False
    file = open("..\src\owosettings.json", "w")
    dump(data, file, indent=4)
    file.close()
    print(f"{color.okgreen}[INFO] {color.okcyan}Successfully Saved!{color.reset}")
    if not all:
        main()


def sound(data, all):
    print("")
    data['sound'] = input(f"{color.okcyan}Do you want to ping by music? (YES/NO): {color.yellow}")
    if data['sound'].lower()=='yes':
        data['sound']=True
    elif data['sound'].lower()=='no':
        data['sound']=False
    else:
        print(f"{color.fail}WRONG INPUT")
        sound(data,all)
    file = open("..\src\owosettings.json", "w")
    dump(data, file, indent=4)
    file.close()
    print(f"{color.okgreen}[INFO] {color.okcyan}Successfully Saved!{color.reset}")
    if not all:
        main()


def webhook(data, all):
    print("")
    data['webhook']['enable'] = input(f"{color.okcyan}Toggle Discord Webhook, If You Want It To Ping You If OwO Asked Captcha. [YES/NO]: {color.yellow}")
    if data['webhook']['enable'].lower() == "no":
        data['webhook']['enable'] == False
    elif data['webhook']['enable'].lower() == "yes":
        data['webhook']['enable'] == True
        data['webhook']['link'] = input(f"{color.okcyan}Input Webhook link: {color.yellow}")
        data['webhook']['pingid'] = input(f"{color.okcyan}Do You Want To Ping A Specified User When OwO Asked Captcha? If Yes Enter User ID. Otherwise Enter \"None\": {color.yellow}")
    else:
        print(f'{color.fail}WRONG INPUT')
        webhook(data,all)
    file = open("..\src\owosettings.json", "w")
    dump(data, file, indent=4)
    file.close()
    print(f"{color.okgreen}[INFO] {color.okcyan}Successfully Saved!{color.reset}")
    if not all:
        main()


def solve(data, all):
    print("")
    data['solve']['enable'] = input(f"{color.okcyan}Toggle Automatically Captcha Solving By Human Free(YES/NO): {color.yellow}")
    if data['solve']['enable'].lower() == "yes":
        print("Available Captcha Solving Server:\n1: https://autofarmsupport.tk\n2: https://afbot.dev")
        data['solve']['server'] = input(f"{color.okcyan}Which Server Do You Want To Use (1/2): {color.yellow}")
        if data['solve']['server'] == "1" or data['solve']['server'] == "2":
            data['solve']['server'] = int(data['solve']['server'])
        else:
            print(f"{color.fail}Invalid Input{color.reset}")
            solve(data, all)
        data['solve']['enable'] = True
    else:
        data['solve']['enable'] = False

    file = open("..\src\owosettings.json", "w")
    dump(data, file, indent=4)
    file.close()
    print(f"{color.okgreen}[INFO] {color.okcyan}Successfully Saved!{color.reset}")
    if not all:
        main()


def twocaptcha(data, all):
    print("")
    data['twocaptcha']['enable'] = input(f"{color.okcyan}Do you have API Two Captcha, Enter API Two Captcha If You have [YES/NO]: {color.yellow}")
    if data['twocaptcha']['enable'].lower() =='yes':
        data['twocaptcha']['api'] = input(f"{color.okcyan}Input your two captcha API{color.reset}")
        data['twocaptcha']['enable'] = True
    elif data['twocaptcha']['enable'].lower() =='no':
        data['twocaptcha']['enable'] = False
    else:
        print(f"{color.fail}Wrong Input")
        twocaptcha(data,all)
    file = open("..\src\owosettings.json", "w")
    dump(data, file, indent=4)
    file.close()
    print(f"{color.okgreen}[INFO] {color.okcyan}Successfully Saved!{color.reset}")
    if not all:
        main()


def huntbot(data, all):
    print("")
    data['huntbot']['enable'] = input(f"{color.okcyan}Toggle Automatically Send Huntbot/Autohunt.Only available if you have TwoCaptcha API (YES/NO): {color.yellow}")
    if data['huntbot']['enable'].lower() == "yes":
        data['huntbot']['sacrifice']['enable'] = input(f"{color.okcyan}Toggle Automatically Sacrifice Huntbot/Autohunt (YES/NO): {color.yellow}")
        if data['huntbot']['sacrifice']['enable'].lower() == 'yes':
            print(f"{color.warning}Animal Type: C, U, R, E, M, L, F, ... (Type \"all\" To sacrifice All Animals)")
            print(f"{color.warning}C = Common, U = Uncommon, ect...")
            data['huntbot']['sacrifice']['type'] = input(f"{color.okcyan}Enter Animal Type: {color.yellow}")
            data['huntbot']['sacrifice']['enable'] = True
        else:
            data['huntbot']['sacrifice'] = False
        data['huntbot']['enable'] = True
    else:
        data['huntbot']['enable'] = False
    file = open("..\src\owosettings.json", "w")
    dump(data, file, indent=4)
    file.close()
    print(f"{color.okgreen}[INFO] {color.okcyan}Successfully Saved!{color.reset}")
    if not all:
        main()


if __name__ == "__main__":
    main()
