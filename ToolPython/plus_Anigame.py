from time import sleep, strftime, localtime
from menu import UI
from color import color
from information import information
from exception import exception
import discum
from discum.utils.button import Buttoner
try:
    from inputimeout import inputimeout, TimeoutOccurred
except Exception as e:
    from setup import install
    install()
    from inputimeout import inputimeout, TimeoutOccurred


wbm = [13, 16]
ui = UI()
client = information()
AniGameId = '571027211407196161'

bot = discum.Client(token=client.token, log=False, build_num=0, x_fingerprint="None", user_agent=[
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36/PAsMWa7l-11',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 YaBrowser/20.8.3.115 Yowser/2.5 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:60.7.2) Gecko/20100101 / Firefox/60.7.2'])


def at():
    return f'\033[0;43m{strftime("%d %b %Y %H:%M:%S", localtime())}\033[0;21m'


elsa = '''\
            ███████╗██╗     ███████╗ █████╗                           
            ██╔════╝██║     ██╔════╝██╔══██╗                          
            █████╗  ██║     ███████╗███████║                          
            ██╔══╝  ██║     ╚════██║██╔══██║                          
            ███████╗███████╗███████║██║  ██║                          
            ╚══════╝╚══════╝╚══════╝╚═╝  ╚═╝                          
                                                                    
             █████╗ ███╗   ██╗██╗ ██████╗  █████╗ ███╗   ███╗███████╗ 
            ██╔══██╗████╗  ██║██║██╔════╝ ██╔══██╗████╗ ████║██╔════╝ 
            ███████║██╔██╗ ██║██║██║  ███╗███████║██╔████╔██║█████╗   
            ██╔══██║██║╚██╗██║██║██║   ██║██╔══██║██║╚██╔╝██║██╔══╝   
            ██║  ██║██║ ╚████║██║╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗ 
            ╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝ ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝ 
                                                                    
            ███████╗███████╗██╗     ███████╗██████╗  ██████╗ ████████╗
            ██╔════╝██╔════╝██║     ██╔════╝██╔══██╗██╔═══██╗╚══██╔══╝
            ███████╗█████╗  ██║     █████╗  ██████╔╝██║   ██║   ██║   
            ╚════██║██╔══╝  ██║     ██╔══╝  ██╔══██╗██║   ██║   ██║   
            ███████║███████╗███████╗██║     ██████╔╝╚██████╔╝   ██║   
            ╚══════╝╚══════╝╚══════╝╚═╝     ╚═════╝  ╚═════╝    ╚═╝   
                                                                                          
'''


@bot.gateway.command
def on_ready(resp):
    if resp.event.ready_supplemental:  # ready_supplemental is sent after ready
        user = bot.gateway.session.user
        client.username = user['username']
        client.userid = user['id']
        print()
        print()
        print(f'{color.okcyan}{elsa}{color.reset}')
        print(f"                   {color.purple}Version: ELSA-1.0.0 {color.reset}")
        sleep(1)
        print()
        print("╔═════════════════════════════════════════════════════════════════════════════════╗")
        print()
        print(f" {color.yellow}This is the selfbot of AniGame was created by {color.okcyan}Iris {color.yellow}({color.okcyan}FrozenQueenElsa{color.yellow}). {color.reset}")
        print()
        print("╚═════════════════════════════════════════════════════════════════════════════════╝")

        print(f"Logged in as {color.yellow}{user['username']}#{user['discriminator']}{color.reset}")
        sleep(1.5)
        print('═' * 25)


def substring_after(s, substring):
    return s.partition(substring)[2]


def substring_before(s, substring):
    return s.partition(substring)[0]


@bot.gateway.command
def checkanigame(resp):

    if resp.event.message:
        m = resp.parsed.auto()

        channels = [
            '994874200793825361',
            '1020266555080196177',
            '903087289431912478'
        ]
        # for i in channels:
        # if m['channel_id']==channels[i]:

        if m['author']['id'] == AniGameId:
            embeds = m["embeds"]
            if len(embeds) > 0:
                e = embeds[0]
                embed_title = e.get("title", "")

                if "What's this?" in embed_title:

                    try:
                        guildcardid = bot.getChannel(m['channel_id']).json()['guild_id']

                        channels = bot.gateway.session.guild(guildcardid).channels
                        guildname = bot.gateway.session.guild(guildcardid).name
                        for i in channels:
                            if channels[i]['type'] == "guild_text" and channels[i]['id'] == m['channel_id']:
                                channel4 = channels[i]
                        channelname = channel4['name']
                        print(f'{at()}Found the animecard appear at channel {channelname} in server {guildname}')
                        buts = Buttoner(m["components"])
                        sleep(5)
                        bot.click(
                            m["author"]["id"],
                            channelID=m["channel_id"],
                            guildID=guildcardid,
                            messageID=m["id"],
                            messageFlags=m["flags"],
                            data=buts.getButton("Claim!"),
                        )
                    except ValueError:
                        pass


@bot.gateway.command
def checkclaimanigame(resp):

    if resp.event.message:
        m = resp.parsed.auto()
        if m['author']['id'] == AniGameId:
            embeds = m["embeds"]
            if len(embeds) > 0:
                e = embeds[0]
                embed_title = e.get("title", "")
                embed_description = e.get("description", "")

                if "Successfully claimed by" in embed_title and client.username in embed_title:
                    # emoji=':claimed'
                    # line2=substring_after(m['content'], emoji)
                    getclaim = substring_before(embed_description, 'has been added to')
                    rarety = substring_before(getclaim, " ")
                    character = substring_after(getclaim, " ")

                    print(f"{at()}{color.warning} [INFO] {color.yellow} CLAIM {color.okcyan} {rarety} {color.okgreen} {character} {color.reset}")


bot.gateway.run()
