import os, time, sys
from version import version
from color import color


class UI:

    @classmethod
    def slowPrinting(cls, text):
        for letter in text:
            sys.stdout.write(letter)
            sys.stdout.flush()
            time.sleep(0.000001)
        print()

    @classmethod
    def logo(cls):
        print(f'{color.okcyan}{elsa}{color.reset}')
        print(f"                   {color.purple}Version: {version} {color.reset}")
        time.sleep(0.5)
        print()
        print("╔═════════════════════════════════════════════════════════════════════════════════╗")
        print()
        print(f" {color.yellow}This is the moded auto by {color.okcyan}Iris {color.yellow}({color.okcyan}FrozenQueenElsa{color.yellow}). {color.reset}")
        print(f" {color.yellow}Thanks to {color.okcyan}ahihiyou20{color.yellow} for the original version{color.reset}")
        print(f" {color.yellow}Thanks to {color.okcyan}Naru2203{color.yellow} for the auto owo slot version{color.reset}")
        print()
        print("╚═════════════════════════════════════════════════════════════════════════════════╝")
        print()
        time.sleep(1)

    @classmethod
    def start(cls):
        print("╔═══════════════════════════════╗")
        print()
        print(f"       {color.purple}[1]{color.reset} Load Data")
        print(f"       {color.purple}[2]{color.reset} Create New data")
        print(f"       {color.purple}[3]{color.reset} Additional Info")
        print()
        print("╚═══════════════════════════════╝")

    @classmethod
    def newData(cls):
        print("╔═══════════════════════════════════════════╗")
        print()
        print("         [0] Exit And Save")
        print("         [1] Change All Settings")
        print("         [2] Change Token")
        print("         [3] Change Channel")
        print("         [4] Change Sleep Mode")
        print("         [5] Change Exp Mode")
        print("         [6] Change Auto Setting")
        print("         [7] Change Pray/Curse Mode")
        print("         [8] Change Sell Mode")
        print("         [9] Change Prefix Mode")
        print("         [10] Change Gem Mode")
        print("         [11] Change Casino Mode")
        print("         [12] Change Sound Mode")
        print("         [13] Change Webhook Setting")
        print("         [14] Change Solve Captcha Setting")
        print("         [15] Change TwoCaptcha Setting")
        print("         [16] Change Huntbot Mode")

        print()
        print("╚═══════════════════════════════════════════╝")

    @classmethod
    def newstatus(cls):
        print("╔═══════════════════════════════════════════╗")
        print()
        print("         [0] Exit And Save")
        print("         [1] Change Status Setting")
        print()
        print("╚═══════════════════════════════════════════╝")


    @classmethod
    def info(cls):
        print(f"{color.purple}╔═════════════════Support════════════════╗{color.reset}")
        print(f"\t{color.purple}https://discord.gg/9uZ6eXFPHD{color.reset}")
        print(" ")
        print(f"{color.purple}╔═══════════════════════════════════════════════════════════════════════════Disclaimer═══════════════════════════════════════════════════════╗{color.reset}")
        print(f"\t{color.purple}This SelfBot Is Only For Education Purpose Only. Deny All Other Promises Or Responsibilities. Use The SelfBot At Your Own Risk.")
        print(" ")
        print(f'{color.purple}╔═════════════════Credit═════════════════╗{color.reset}')
        print(f'\t{color.purple} [Developer] {color.reset} Iris [Frozen Queen Elsa]')
        print(f'\t{color.purple} [Developer] {color.reset} Sudo-Nizel')
        print(f'\t{color.purple} [Developer] {color.reset} ahihiyou20')
        print(" ")
        print(f'{color.purple}╔═════════════════════════Selfbot Commands════════════════════════╗{color.reset}')
        print("\t{Prefix}send {Message} [Send Your Provied Message}")
        print("\t{Prefix}restart [Restart The Selfbot]")
        print("\t{Prefix}exit [Stop The Selfbot]")
        print("\t{Prefix}sleep {on/off} [Turn On Or Off Sleep Mode]")
        print("\t{Prefix}exp {on/off} [Turn On Or Off Exp Mode]")
        print("\t{Prefix}praycurse {on/off} [Turn On Or Off Pray/Curse Mode]")
        print("\t{Prefix}gem {on/off} [Turn On Or Off Gems Mode]")
        print("\t{Prefix}gems [Use Gems]")
        print("\t{Prefix}hunt {on/off} [Turn On Or Off Hunt Mode]")
        print("\t{Prefix}battle {on/off} [Turn On Or Off Battle Mode]")
        print("\t{Prefix}sayowo {on/off} [Turn On Or Off Say Owo Mode]")
        print("\t{Prefix}buyring {on/off} [Turn On Or Off Buy Ring Mode]")
        print("\t{Prefix}sell {on/off} [Turn On Or Off Sell Mode]")
        print("\t{Prefix}casino {on/off} [Turn On Or Off Sell Mode]")
        print(" ")
        print("{Prefix} == Your Prefix")
        print(" ")
        print("Note: Alright If You See Someone Selling This Code Then You Got Scammed Because This Code Is Free!")
        time.sleep(0.5)
        print("Press Enter To Exit")
        input()


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