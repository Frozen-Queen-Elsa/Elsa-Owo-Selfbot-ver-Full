import json
from os import system, name, execl
from time import sleep, strftime, localtime
from color import color
from menu import UI
from information import information
from exception import exception
import discum

try:
    from inputimeout import inputimeout, TimeoutOccurred
except Exception as e:
    from setup import install
    install()
    from inputimeout import inputimeout, TimeoutOccurred


wbm = [13, 16]
client = information()
ui = UI()
token = client.token


elsa = '''\
███████╗██╗     ███████╗ █████╗                                                           
██╔════╝██║     ██╔════╝██╔══██╗                                                          
█████╗  ██║     ███████╗███████║                                                          
██╔══╝  ██║     ╚════██║██╔══██║                                                          
███████╗███████╗███████║██║  ██║                                                          
╚══════╝╚══════╝╚══════╝╚═╝  ╚═╝                                                          

███████╗███████╗██╗     ███████╗██████╗  ██████╗ ████████╗
██╔════╝██╔════╝██║     ██╔════╝██╔══██╗██╔═══██╗╚══██╔══╝
███████╗█████╗  ██║     █████╗  ██████╔╝██║   ██║   ██║   
╚════██║██╔══╝  ██║     ██╔══╝  ██╔══██╗██║   ██║   ██║   
███████║███████╗███████╗██║     ██████╔╝╚██████╔╝   ██║   
╚══════╝╚══════╝╚══════╝╚═╝     ╚═════╝  ╚═════╝    ╚═╝   

'''

bot = discum.Client(token=token, log=False, build_num=0, x_fingerprint="None", user_agent=[
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

███████╗███████╗██╗     ███████╗██████╗  ██████╗ ████████╗
██╔════╝██╔════╝██║     ██╔════╝██╔══██╗██╔═══██╗╚══██╔══╝
███████╗█████╗  ██║     █████╗  ██████╔╝██║   ██║   ██║   
╚════██║██╔══╝  ██║     ██╔══╝  ██╔══██╗██║   ██║   ██║   
███████║███████╗███████╗██║     ██████╔╝╚██████╔╝   ██║   
╚══════╝╚══════╝╚══════╝╚═╝     ╚═════╝  ╚═════╝    ╚═╝   
'''


@bot.gateway.command
def on_ready(resp: object) -> None:
    if resp.event.ready_supplemental:
        system('cls' if name == 'nt' else 'clear')
        user = bot.gateway.session.user
        username = user['username']
        userid = user['id']
        print(f'{color.warning}{elsa}{color.reset}')
        print('')
        sleep(1)
        print(f'{color.okgreen}══════════════════════════════════════{color.reset}')
        print(f"{color.okcyan}Logged in as {color.warning}{user['username']}#{user['discriminator']}{color.reset}")
        sleep(0.5)
        print('══════════════════════════════════════')
        ChangeStatus()

def ChangeStatus():
    with open('..\src\statussetting.json', "r", encoding='utf-8') as file:
        data = json.load(file)
        status = data['status']
    count = 1
    while True:
        print(f"{color.fail}Count time: {count}{color.reset}")
        for i in range(status['number']):
            index = i + 1
            StrJoin = ["status", str(index)]
            status_index = '_'.join(StrJoin)
            stt = status[status_index]['stt']
            time_sleep = status[status_index]['time']
            bot.gateway.setCustomStatus(stt)
            print(f"{at()}{color.reset}{color.okblue} [Change Status]{color.green} {stt}{color.reset}")
            sleep(time_sleep)
        count += 1;
        print(f"\n{color.warning}===========================================================\n{color.reset}")
        sleep(1)




bot.gateway.run()
