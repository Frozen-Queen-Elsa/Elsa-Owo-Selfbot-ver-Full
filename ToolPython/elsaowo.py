import subprocess
import sys
from sys import executable, argv
from signal import signal, SIGINT
import os
from os import execl, name, system
from time import sleep, strftime, localtime, time
from requests import get, post
from base64 import b64encode
import atexit
import random
from re import findall
import json
import threading
import base64
import requests

try:
    from playsound import playsound
    from twocaptcha import TwoCaptcha
    from inputimeout import inputimeout, TimeoutOccurred
    import discum

    from discum.utils.slash import SlashCommander
    from discord_webhook import DiscordWebhook
except Exception as e:

    from setup import install

    install()
    from playsound import playsound
    from twocaptcha import TwoCaptcha
    from inputimeout import inputimeout, TimeoutOccurred
    import discum

    from discum.utils.slash import SlashCommander
    from discord_webhook import DiscordWebhook

# Local
from information import information
from menu import UI
from color import color
from casino import casinos
from gem import gems
from webhook import webhooks
from music import musics
from function import functions
from runner import runners
from spam import spam
from exception import exception

client = information()
ui = UI()
function = functions()

# Enter API TwoCaptcha
if client.twocaptcha['enable']:
    api_key = os.getenv('APIKEY_2CAPTCHA', client.twocaptcha['api'])
    solver = TwoCaptcha(api_key, defaultTimeout=100, pollingInterval=5)


# Crl C
def signal_handler(sig: object, frame: object):
    sleep(0.5)
    print(f"\n{color.fail}[INFO] {color.reset}Detected Ctrl + C, Stopping...")
    raise KeyboardInterrupt


client.start = False
signal(SIGINT, signal_handler)
token = client.token
# Bot Information
bot = discum.Client(token=token, log=False, build_num=0, x_fingerprint="None", user_agent=[
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36/PAsMWa7l-11',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 YaBrowser/20.8.3.115 Yowser/2.5 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:60.7.2) Gecko/20100101 / Firefox/60.7.2'])

casino = casinos(bot)
gem = gems(bot)
webhook = webhooks(bot)
music = musics()
runner = runners(bot)
spam = spam(bot)


# Current Time
def at():
    return f'\033[0;43m{strftime("%d %b %Y %H:%M:%S", localtime())}\033[0;21m'


while True:
    system('cls' if name == 'nt' else 'clear')
    ui.logo()
    ui.start()
    try:
        print(f"{color.okcyan}Automatically Pick Option [1] In 10 Seconds.")
        choice = inputimeout(prompt=f'{color.okcyan}Enter Your Choice: {color.okgreen}', timeout=10)
    except TimeoutOccurred:
        choice = "1"

    if choice == "1":
        if not client.twocaptcha:
            print(f'{color.okcyan}You are using free version for solving captcha')
            print(f'Join this server to register solving system https://dsc.gg/serverafs {color.reset}')
        else:
            print(f'{color.warning}You are using vip version for solving captcha by TwoCaptcha{color.reset}')
        client.check()
        break

    elif choice == "2":
        from newinformation import main

        main()

    elif choice == "3":
        ui.info()
        continue
    else:
        print(f'{color.fail} !! [ERROR] !! {color.reset} Wrong input!')
        sleep(1)
        execl(executable, executable, *argv)


@bot.gateway.command
def on_ready(resp):
    if resp.event.ready_supplemental:  # ready_supplemental is sent after ready
        for i in range(len(bot.gateway.session.DMIDs)):
            if client.OwOID in bot.gateway.session.DMs[bot.gateway.session.DMIDs[i]]['recipients']:
                client.dmsid = bot.gateway.session.DMIDs[i]
        user = bot.gateway.session.user
        client.username = user['username']
        client.userid = user['id']
        client.guild_id = bot.getChannel(client.channel).json()['guild_id']
        client.guild_name = bot.gateway.session.guild(client.guild_id).name

        ui.slowPrinting(f"\nLogged in as {color.yellow}{user['username']}#{user['discriminator']}{color.reset}")
        sleep(1)
        print('═' * 25)
        print('')
        print(f"{color.purple}Settings: {color.reset}")
        print(f"{color.purple}Channel: {client.channel}{color.reset}")
        print(f"{color.purple}----------------------------------{color.reset}")
        print(f"{color.purple}Hunt Mode: {client.runner['hunt']}{color.reset}")
        print(f"{color.purple}Battle Mode: {client.runner['battle']}{color.reset}")
        print(f"{color.purple}Daily Mode: {client.runner['daily']}{color.reset}")
        print(f"{color.purple}Say Owo Mode: {client.runner['owo']}{color.reset}")
        print(f"{color.purple}Buy Ring Mode: {client.runner['ring']}{color.reset}")
        print(f"{color.purple}Gem Mode: {client.gem['enable']}{color.reset}")
        if client.gem['enable']:
            print(f"{color.purple}Use Gem Method: {client.gem['minmax']}{color.reset}")
            print(f"{color.purple}Max Tier Gem: {client.gem['maxtier']}{color.reset}")
            print(f"{color.purple}Open Lootbox: {client.gem['lbox']}{color.reset}")
            print(f"{color.purple}Open Weapon Crate: {client.gem['wcrate']}{color.reset}")

        if client.sleep['enable']:
            print(f"{color.purple}Sleep After {client.sleep['time']} seconds in {client.sleep['duration']} seconds{color.reset}")
        if not client.sleep['enable']:
            print(f"{color.purple}Sleep Mode: {client.sleep['enable']}{color.reset}")
        print(f"{color.purple}Pray/Curse Mode: {client.praycurse['enable']}{color.reset}")
        if client.praycurse['prayother']['enable']:
            print(f"{color.purple}Pray/Cure for ID: {client.praycurse['prayother']['userid']}{color.reset}")
        print(f"{color.purple}EXP Mode: {client.exp['enable']}{color.reset}")
        if client.exp['enable']:
            print(f"{color.purple}Spaming Channel: {client.exp['channelspamid']}{color.reset}")
        print(f"{color.purple}Sell Mode: {client.sell['enable']}{color.reset}")
        if client.sell['enable']:
            print(f"{color.purple}Sell Type: {client.sell['type']}{color.reset}")
        # print(f"{color.purple}Hunt bot Mode: {client.huntbot['enable']}{color.reset}")
        # if client.huntbot['enable']:
        # 	print(f"{color.purple}Sacrifice Mode: {client.huntbot['sacrifice']['enable']}{color.reset}")
        # 	if client.huntbot['sacrifice']['enable']:
        # 		print(f"{color.purple}Sacrifice Type: {client.huntbot['sacrifice']['type']}{color.reset}")
        print(f"{color.purple}----------------------------------{color.reset}")
        print(f"{color.purple}Auto Casino: {client.casino['enable']}{color.reset}")
        if client.casino['enable']:
            print(f"{color.purple}Max Bet Method: {client.casino['maxbet']}{color.reset}")
            print(f"{color.purple}Casino Channel: {client.casino['channelcasinoid']}{color.reset}")
            print(f"{color.purple}Auto CoinFlip: {client.casino['cf']['enable']}{color.reset}")
            if client.casino['cf']['enable']:
                print(f"{color.purple}Min Bet of Coinflip: {client.casino['cf']['bet']}{color.reset}")
                print(f"{color.purple}Rate Multiple of Coinflip: {client.casino['cf']['rate']}{color.reset}")
            print(f"{color.purple}Auto Owo Slot: {client.casino['os']['enable']}{color.reset}")
            if client.casino['os']['enable']:
                print(f"{color.purple}Min Bet of Owo Slot: {client.casino['os']['bet']}{color.reset}")
                print(f"{color.purple}Rate Multiple of Owo Slot: {client.casino['os']['rate']}{color.reset}")
        print(f"{color.purple}----------------------------------{color.reset}")
        print(f"{color.purple}Prefix Mode: {client.prefix['enable']}{color.reset}")
        if client.prefix['enable']:
            print(f"{color.purple}Selfbot Commands Prefix: {client.prefix['key']}{color.reset}")
            print(f"{color.purple}Selfbot Commands Allowed Id: {client.prefix['allowed_id']}{color.reset}")
        print(f"{color.purple}Webhook Mode: {client.webhook['enable']}{color.reset}")
        print(f"{color.purple}Webhook Ping User Id: {client.webhook['pingid']}{color.reset}")
        print(f"{color.purple}----------------------------------{color.reset}")
        if not client.twocaptcha['enable']:
            print(f"{color.purple}Solve Captcha Mode: {client.solve['enable']}{color.reset}")
            if client.solve['enable']:
                print(f"{color.purple}Solve Captcha Server: {client.solve['server']}{color.reset}")
        if client.twocaptcha['enable']:
            print(f"{color.purple}Solve Captcha by TwoCaptcha{color.reset}")
        print(f"{color.purple}Sound: {client.sound}{color.reset}")
        print(f"{color.purple}----------------------------------{color.reset}")
        print('═' * 25)
        if client.casino['enable']:
            if client.casino['cf']['enable']:
                client.currentcfbet=client.casino['cf']['bet']
            if client.casino['os']['enable']:
                client.currentosbet=client.casino['os']['bet']
        if not client.start:
            loopie()


@bot.gateway.command
def security(resp):
    threadcaptchamusic = threading.Thread(name="captchamusic", target=music.captchamusic)
    threadsolvedmusic = threading.Thread(name="solvedmusic", target=music.solvedmusic)
    if CheckCaptcha(resp) == "solved":
        if client.casino['enable']:
            if client.casino['cf']['enable'] or client.casino['os']['enable']:
                webhook.webhookPing(f"[SUCCESS] I have solved the captcha succesfully in Channel: <#{client.channel}> or <#{client.channelocf}> . User: {client.username} ")
            else:
                webhook.webhookPing(f"[SUCCESS] I have solved the captcha succesfully in Channel: <#{client.channel}> . User: {client.username} ")
        else:
            webhook.webhookPing(f"[SUCCESS] I have solved the captcha succesfully in Channel: <#{client.channel}> . User: {client.username} ")
        if client.twocaptcha['enable']:
            webhook.webhookPing(f'2Captcha Balance: {solver.balance()} $')
        webhook.webhookPing("===========================================================================================")
        # threadsolvedmusic.start()
        sleep(3)
        print(f'{color.okcyan}[INFO] {color.reset}Captcha Solved. Started To Run Again')
        execl(executable, executable, *argv)
    if CheckCaptcha(resp) == "captcha":
        client.stopped = True
        webhook.webhookping(client.username, client.userid)
        threadcaptchamusic.start()
        bot.switchAccount(client.token[:-4] + 'FvBw')


@bot.gateway.command
def CheckCaptcha(resp):
    def getAnswer(img, lenghth, code, code2, code3):
        count = 0
        TimeAnswer = time()
        while True:
            if time() - TimeAnswer < 300:
                count += 1
                r = solver.normal(img, numeric=2, minLen=lenghth, maxLen=lenghth, phrase=0, caseSensitive=0, calc=0, lang='en', textinstructions=code, )

                if r['code'].isalpha():
                    if len(r['code']) == lenghth:
                        if r['code'] != code2 and r['code'] != code3:
                            print('Check result 2 captcha')
                            return r
                        else:
                            solver.report(r['captchaId'], False)
                            print(f'Time: {count}. The answer {r["code"]} is not right.Try again')
                    else:
                        solver.report(r['captchaId'], False)
                        print(f'Time: {count}. The length of result {r["code"]} is not right.Try again')

                else:
                    solver.report(r['captchaId'], False)
                    print(f'Time: {count}. The result {r["code"]} contants number.Try again')
            else:
                print(f'TIME OUT 5 MINUTES for SOLVE')
                return 'captcha'

    def SolveFree(image_url, captcha_mes):
        threadcaptcha = threading.Thread(name="captchamusic", target=music.captchamusic)
        try:
            if client.solve['enable']:
                client.stopped = True
                from api import CAPI
                api = CAPI(client.userid, client.solve['server'])
                encoded_string = b64encode(get(image_url).content).decode('utf-8')
                print(f"{color.okcyan}[INFO] {color.reset}Solving Captcha...")
                r = api.solve(Json={'data': encoded_string, 'len': captcha_mes[captcha_mes.find("letter word") - 2]})
                if r:
                    print(f"{color.okcyan}[INFO] {color.reset}Solved Captcha [Code: {r['code']}]")
                    bot.sendMessage(client.dmsid, r['code'])
                    sleep(10)
                    mes = bot.getMessages(client.dmsid)
                    try:
                        mes = mes[0]
                    except Exception as e:
                        print(str(e))
                        print(f"{color.okcyan}[INFO] {color.reset}There's An Issue With ReRunner")
                        sleep(2)
                        return "captcha"
                    if mes['author']['id'] == client.OwOID and "verified" in mes['content']:
                        api.report(Json={'captchaId': r['captchaId'], 'correct': 'True'})
                        return "solved"
                    else:
                        webhook.webhookping(client.username, client.userid)
                        threadcaptcha.start()
                        print(f"{color.okcyan}[INFO] {color.reset}Selfbot Stopped As The Captcha Code Is Wrong")
                        api.report(Json={'captchaId': r['captchaId'], 'correct': 'False'})
                        return "captcha"
                elif not r:
                    webhook.webhookping(client.username, client.userid)
                    threadcaptcha.start()
                    print(f"{color.okcyan}[INFO] {color.reset}You Haven't Registered To Our Captcha Solving API!")
                    print("To Register Join Our Discord Server: https://dsc.gg/serverafs And Send \"bot register\" in bot command channel")
                    return "captcha"
                else:
                    webhook.webhookping(client.username, client.userid)
                    threadcaptcha.start()
                    print(f"{color.okcyan}[INFO] {color.reset}Captcha Solver API Is Having An Issue...")
                    return "captcha"
        except Exception as e:
            webhook.webhookping(client.username, client.userid)
            threadcaptcha.start()
            return "captcha"

    def SolveCaptcha(captcha, len, hint, answer1, answer2, time):
        if 1 <= time <= 3:
            # Solve by 2Captcha
            r = getAnswer(captcha, len, hint, answer1, answer2)
            captcha_balance = solver.balance()
            print(f'Balance TwoCaptcha : {captcha_balance} $')
            print(f"{color.okcyan}[INFO] {color.reset}Solving Captcha at 1st chance: [Code: {r['code']}]")
            bot.sendMessage(client.dmsid, r['code'])
            sleep(5)
            return r

    def SolveVIP(image_url, captcha_mes, hint, answer1, answer2, time):
        if client.twocaptcha['enable'] and 1 <= time <= 3:
            client.stopped = True
            encoded_string = b64encode(get(image_url).content).decode('utf-8')
            try:
                count_len = int(captcha_mes[captcha_mes.index("letter word") - 2])
            except:
                count_len = int(captcha_mes[captcha_mes.find("letter word") - 2])
            # Check balance of 2Captcha
            captcha_balance = solver.balance()
            if captcha_balance == 0:
                print(f'Balance TwoCaptcha : {captcha_balance} $ Out of money')
                webhook.webhookPing(f"<@{client.webhook['pingid']}> [FAIL]Out of money . User: {client.username} <@{client.userid}>")
                webhook.webhookPing(f"=========================================================================================")
                if client.solve['enable']:
                    client.stopped = True
                    return SolveFree(image_url, captcha_mes)
                else:
                    return "captcha"

            answer = SolveCaptcha(encoded_string, count_len, hint, answer1, answer2, time)
            mes = bot.getMessages(client.dmsid)

            try:
                mes = mes[0]
            except Exception as e:
                print(str(e))
                print(f"{color.okcyan}[INFO] {color.reset}There's An Issue With ReRunner")
                sleep(2)
                return "captcha"
            if mes['author']['id'] == client.OwOID and "verified" in mes['content']:
                print(f"{color.purple}Right Captcha{color.reset}")
                solver.report(answer['captchaId'], True)
                return "solved"
            if mes['author']['id'] == client.OwOID and "Wrong verification code" in mes['content']:

                webhook.webhookping(client.username, client.userid)
                webhook.webhookPing(f"<@{client.webhook['pingid']}> [FAIL]I have solved the captcha fail in the {time} chance. Wait me at the {time} chance. Sorry . User: {client.username} <@{client.userid}>")
                solver.report(answer['captchaId'], False)  # Báo kết quả sai

                if time == 1:
                    time += 1
                    answer1 = answer['code']
                    TextWrong = 'IS WRONG'
                    TextJoin = [answer1.upper(), TextWrong.lower()]
                    hint = ' '.join(TextJoin)
                    print(f"{color.purple}Wrong Captcha 1st time{color.reset}")
                    return SolveVIP(image_url, captcha_mes, hint, answer1, 0, time)

                if time == 2:
                    time += 1
                    answer2 = answer['code']
                    TextWrong = 'ARE WRONG'
                    TextJoin = [answer1.upper(), 'and', answer2.upper(), TextWrong.lower()]
                    hint = ' '.join(TextJoin)
                    print(f"{color.purple}Wrong Captcha 2nd time{color.reset}")
                    return SolveVIP(image_url, captcha_mes, hint, answer1, answer2, time)
                if time == 3:
                    print(f"{color.purple}Wrong Captcha 3rd time{color.reset}")
                    return 'captcha'
            return 'captcha'
        return 'captcha'

    def SolveLink():
        from selenium.webdriver.common.by import By
        from selenium.webdriver.support.ui import WebDriverWait
        from selenium.webdriver.support import expected_conditions as EC
        import undetected_chromedriver as uc
        import chromedriver_binary
        if client.twocaptcha['enable']:
            api = client.twocaptcha['api']
            # Check balance of 2Captcha
            captcha_balance = solver.balance()
            if captcha_balance == 0:
                print(f'Balance TwoCaptcha : {captcha_balance} $ Out of money')
                webhook.webhookPing(f"<@{client.webhook['pingid']}> [FAIL]Out of money . User: {client.username} <@{client.userid}>")
                webhook.webhookPing(f"=========================================================================================")
                return "captcha"

            # Setting Chrom extension
            chrome_options = uc.ChromeOptions()
            chrome_options.add_extension('..\src\TwoCaptchaAutoSolve.crx')
            driver = uc.Chrome(options=chrome_options)

            # Setting key 2Captcha Solver
            driver.get('chrome-extension://ifibfemgeogfhoebkmokieepdoobkbpo/options/options.html')
            driver.find_element(By.CSS_SELECTOR, value='body > div > div.content > table > tbody > tr:nth-child(1) > td:nth-child(2) > input[type=text]')
            driver.execute_script("document.getElementsByName('apiKey')[0].value=arguments[0]", api)

            # click Login
            LoginButton = driver.find_element(By.CSS_SELECTOR, "#connect")
            driver.execute_script("arguments[0].click();", LoginButton)

            # Tắt Alert
            WebDriverWait(driver, 10).until(EC.alert_is_present())
            driver.switch_to.alert.accept()

            # OWO
            driver.get('https://owobot.com/captcha')
            js = 'function login(token) {setInterval(() => {document.body.appendChild(document.createElement `iframe`).contentWindow.localStorage.token = `"${token}"`}, 50);setTimeout(() => {location.reload();}, 500);}'
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#app > div.v-dialog__content.v-dialog__content--active > div > div > div.v-card__actions.actions > button')))
            driver.find_element(By.CSS_SELECTOR, value='#app > div.v-dialog__content.v-dialog__content--active > div > div > div.v-card__actions.actions > button').click()
            driver.execute_script(js + f'login("{token}")')
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'button[class="button-f2h6uQ lookFilled-yCfaCM colorBrand-I6CyqQ sizeMedium-2bFIHr grow-2sR_-F"]')))
            driver.find_element(By.CSS_SELECTOR, value='button[class="button-f2h6uQ lookFilled-yCfaCM colorBrand-I6CyqQ sizeMedium-2bFIHr grow-2sR_-F"]').click()

            # Đợi extension solver hiện lên rồi f5 vì để ko bị lỗi SiteKey
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "captcha-solver")))
            driver.refresh()
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "captcha-solver")))
            SolveButton = driver.find_element(By.CLASS_NAME, "captcha-solver")
            sleep(3)
            driver.execute_script("arguments[0].click();", SolveButton)
            # Wait
            if WebDriverWait(driver, 200).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "#app > div > main > div > div > div > div:nth-child(2) > div > div.v-card__actions.mb-3.welcome-text > div"), "I have verified that you're a human")):
                print('Solve Captcha Successfully')
                webhook.webhookPing(f"Solve Captcha link successfully")
                driver.quit()
                return "solved"
            else:
                return "captcha"
        else:

            # Setting Chrom extension
            chrome_options = uc.ChromeOptions()
            driver = uc.Chrome(options=chrome_options)

            # OWO
            driver.get('https://owobot.com/captcha')
            js = 'function login(token) {setInterval(() => {document.body.appendChild(document.createElement `iframe`).contentWindow.localStorage.token = `"${token}"`}, 50);setTimeout(() => {location.reload();}, 500);}'
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#app > div.v-dialog__content.v-dialog__content--active > div > div > div.v-card__actions.actions > button')))
            driver.find_element(By.CSS_SELECTOR, value='#app > div.v-dialog__content.v-dialog__content--active > div > div > div.v-card__actions.actions > button').click()
            driver.execute_script(js + f'login("{token}")')
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'button[class="button-f2h6uQ lookFilled-yCfaCM colorBrand-I6CyqQ sizeMedium-2bFIHr grow-2sR_-F"]')))
            driver.find_element(By.CSS_SELECTOR, value='button[class="button-f2h6uQ lookFilled-yCfaCM colorBrand-I6CyqQ sizeMedium-2bFIHr grow-2sR_-F"]').click()
            return "captcha"

    if resp.event.message:
        threadcaptcha = threading.Thread(name="captchamusic", target=music.captchamusic)
        m = resp.parsed.auto()
        if m['channel_id'] == client.channel or m['channel_id'] == client.casino['channelcasinoid'] or m['channel_id'] == client.dmsid and not client.stopped:
            if m['author']['id'] == client.OwOID or m['author']['username'] == 'OwO' or m['author']['discriminator'] == '8456':
                if client.username in m['content'] and 'banned' in m['content'].lower():
                    client.stopped = True
                    print(f'{at()}{color.reset}{color.fail} !!! [BANNED] !!! {color.reset} Your Account Have Been Banned From OwO Bot Please Open An Issue On The Support Discord server')
                    return "captcha"
                if client.username in m['content'] and any(captcha in m['content'].lower() for captcha in ['(1/5)', '(2/5)', '(3/5)', '(4/5)', '(5/5)']):
                    msgs = bot.getMessages(client.dmsid)
                    print(f'{color.warning}{msgs}{color.reset}')

                    if msgs[0]['author']['id'] == client.OwOID and '⚠' in msgs[0]['content'] and msgs[0]['attachments'] and not client.stopped:
                        print(f'{at()}{color.warning} !! [CAPTCHA] !! {color.reset} ACTION REQUİRED')
                        if client.solve['enable'] and not client.stopped and not client.twocaptcha['enable']:
                            client.stopped = True
                            return SolveFree(msgs[0]['attachments'][0]['url'], msgs[0]['content'])
                        elif client.twocaptcha['enable'] and not client.stopped:
                            client.stopped = True
                            return SolveVIP(msgs[0]['attachments'][0]['url'], msgs[0]['content'], "", 0, 0, 1)
                        else:
                            client.stopped = True
                            return "captcha"
                    elif msgs[0]['author']['id'] == client.OwOID and 'link' in msgs[0]['content'].lower() and not client.stopped:
                        client.stopped = True
                        return SolveLink()


                    msgs = bot.getMessages(str(client.channel), num=10)
                    for i in range(len(msgs)):
                        if client.username in msgs[i]['content'] and msgs[i]['author']['id'] == client.OwOID and 'solving the captcha' in msgs[i]['content'].lower() and not client.stopped:
                            print(f'{at()}{color.reset}{color.warning} !! [CAPTCHA] !! {color.reset} ACTION REQUİRED')
                            if client.twocaptcha['enable']:

                                return SolveVIP(msgs[i]['attachments'][0]['url'], msgs[0]['content'], "", 0, 0, 1)
                            else:
                                if client.solve['enable'] and not client.stopped:
                                    client.stopped = True

                                    return SolveFree(msgs[i]['attachments'][0]['url'], msgs[0]['content'])
                                else:
                                    client.stopped = True
                                    return "captcha"
                        else:
                            if i == len(msgs) - 1:
                                client.stopped = True
                                return "captcha"
                if client.username in m['content'] and '⚠' in m['content'].lower() and not client.stopped:
                    if m['attachments'] and not client.stopped:
                        client.stopped = True
                        print(f'{at()}{color.reset}{color.warning} !! [CAPTCHA] !! {color.reset} ACTION REQUİRED')
                        if client.twocaptcha['enable']:
                            return SolveVIP(m['attachments'][0]['url'], m['content'], "", 0, 0, 1)
                        else:
                            if client.solve['enable'] and not client.stopped:
                                client.stopped = True
                                return SolveFree(m['attachments'][0]['url'], m['content'])
                            else:
                                client.stopped = True
                                return "captcha"
                    client.stopped = True
                    print(f'{at()}{color.reset}{color.warning} !! [CAPTCHA] !! {color.reset} ACTION REQUİRED')
                    return "captcha"


@bot.gateway.command
def CheckPrefix(resp):
    if client.prefix['enable']:
        prefix = client.prefix['key']
        with open("..\src\owosettings.json", "r") as f:
            data = json.load(f)
            if resp.event.message:
                m = resp.parsed.auto()

                if m['author']['id'] == client.userid or m['channel_id'] == client.channel:
                    if m['author']['id'] == client.prefix['allowed_id'] or m['author']['id'] == client.userid:
                        if m['content'].startswith(f"{prefix}send"):
                            message = m['content'].replace(f'{prefix}send ', '')
                            bot.sendMessage(str(m['channel_id']), message)
                            print(f"{at()}{color.reset}{color.okcyan} User: {client.username}{color.okgreen} [SENT] {color.reset} {message}")
                        if m['content'].startswith(f"{prefix}restart"):
                            bot.sendMessage(str(m['channel_id']), "Restarting...")
                            print(f"{color.okcyan} [INFO] Restarting...  {color.reset}")
                            sleep(1)
                            execl(executable, executable, *argv)

                        if m['content'].startswith("f{prefix}exit"):
                            bot.sendMessage(str(m['channel_id']), "Exiting...")
                            print(f"{color.okcyan} [INFO] Exiting...  {color.reset}")
                            bot.gateway.close()
                        if m['content'].startswith(f"{prefix}gem"):
                            if "on" in m['content'].lower():
                                client.gem['enable'] = True
                                bot.sendMessage(str(m['channel_id']), f"{client.username} Turned on Gems Mode")
                                print(f"{color.okcyan}[INFO] Turned On Gems Mode{color.okcyan}")
                                file = open("..\src\owosettings.json", "w")
                                data['gem']['enable'] = True
                                json.dump(data, file)
                                file.close()
                            if "off" in m['content'].lower():
                                client.gem['enable'] = False
                                bot.sendMessage(str(m['channel_id']), f"{client.username} Turned Off Gems Mode")
                                print(f"{color.okcyan}[INFO] Turned On Gems Mode{color.okcyan}")
                                file = open("..\src\owosettings.json", "w")
                                data['gem']['enable'] = False
                                json.dump(data, file)
                                file.close()
                        if m['content'].startswith(f"{prefix}praycurse"):
                            if "on" in m['content'].lower():
                                client.praycurse['enable'] = True
                                bot.sendMessage(str(m['channel_id']), f"{client.username} Turned on Pray/Curse Mode")
                                print(f"{color.okcyan}[INFO] Turned On Pray/Curse Mode{color.okcyan}")
                                file = open("..\src\owosettings.json", "w")
                                data['praycurse']['enable'] = True
                                json.dump(data, file)
                                file.close()
                            if "off" in m['content'].lower():
                                client.praycurse['enable'] = False
                                bot.sendMessage(str(m['channel_id']), f"{client.username} Turned Off Pray/Curse Mode")
                                print(f"{color.okcyan}[INFO] Turned On Pray/Curse Mode{color.okcyan}")
                                file = open("..\src\owosettings.json", "w")
                                data['praycurse']['enable'] = False
                                json.dump(data, file)
                                file.close()
                        if m['content'].startswith(f"{prefix}sleep"):
                            if "on" in m['content'].lower():
                                client.sleep['enable'] = True
                                bot.sendMessage(str(m['channel_id']), f"{client.username} Turned on Sleep Mode")
                                print(f"{color.okcyan}[INFO] Turned On Sleep Mode{color.okcyan}")
                                file = open("..\src\owosettings.json", "w")
                                data['sleep']['enable'] = True
                                json.dump(data, file)
                                file.close()
                            if "off" in m['content'].lower():
                                client.sleep['enable'] = False
                                bot.sendMessage(str(m['channel_id']), f"{client.username} Turned Off Sleep Mode")
                                print(f"{color.okcyan}[INFO] Turned On Sleep Mode{color.okcyan}")
                                file = open("..\src\owosettings.json", "w")
                                data['sleep']['enable'] = False
                                json.dump(data, file)
                                file.close()
                        if m['content'].startswith(f"{prefix}sell"):
                            if "on" in m['content'].lower():
                                client.sell['enable'] = True
                                bot.sendMessage(str(m['channel_id']), f"{client.username} Turned on Sell Mode")
                                print(f"{color.okcyan}[INFO] Turned On Sell Mode{color.okcyan}")
                                file = open("..\src\owosettings.json", "w")
                                data['sell']['enable'] = True
                                json.dump(data, file)
                                file.close()
                            if "off" in m['content'].lower():
                                client.sell['enable'] = False
                                bot.sendMessage(str(m['channel_id']), f"{client.username} Turned Off Sell Mode")
                                print(f"{color.okcyan}[INFO] Turned On Sell Mode{color.okcyan}")
                                file = open("..\src\owosettings.json", "w")
                                data['sell']['enable'] = False
                                json.dump(data, file)
                                file.close()
                        if m['content'].startswith(f"{prefix}exp"):
                            if "on" in m['content'].lower():
                                client.exp['enable'] = True
                                bot.sendMessage(str(m['channel_id']), f"{client.username} Turned on Exp Mode")
                                print(f"{color.okcyan}[INFO] Turned On Exp Mode{color.okcyan}")
                                file = open("..\src\owosettings.json", "w")
                                data['exp']['enable'] = True
                                json.dump(data, file)
                                file.close()
                            if "off" in m['content'].lower():
                                client.exp['enable'] = False
                                bot.sendMessage(str(m['channel_id']), f"{client.username} Turned Off Exp Mode")
                                print(f"{color.okcyan}[INFO] Turned On Exp Mode{color.okcyan}")
                                file = open("..\src\owosettings.json", "w")
                                data['exp']['enable'] = False
                                json.dump(data, file)
                                file.close()
                        if m['content'].startswith(f"{prefix}huntbot"):
                            if "on" in m['content'].lower():
                                client.huntbot['enable'] = True
                                bot.sendMessage(str(m['channel_id']), f"{client.username} Turned on Hunt Bot Mode")
                                print(f"{color.okcyan}[INFO] Turned On Hunt Bot Mode{color.okcyan}")
                                file = open("..\src\owosettings.json", "w")
                                data['huntbot']['enable'] = True
                                json.dump(data, file)
                                file.close()
                            if "off" in m['content'].lower():
                                client.exp['enable'] = False
                                bot.sendMessage(str(m['channel_id']), f"{client.username} Turned Off Hunt Bot Mode")
                                print(f"{color.okcyan}[INFO] Turned On Hunt Bot Mode{color.okcyan}")
                                file = open("..\src\owosettings.json", "w")
                                data['huntbot']['enable'] = False
                                json.dump(data, file)
                                file.close()


# Check Hunt
@bot.gateway.command
def CheckHunt(resp):
    if not client.stopped and client.webhook['enable']:
        if resp.event.message:
            m = resp.parsed.auto()
            if m['channel_id'] == client.channel and not client.stopped:
                if m['author']['id'] == client.OwOID:
                    if client.username in m['content'] and "**🌱" in m['content']:
                        channels = bot.gateway.session.guild(client.guild_id).channels

                        for i in channels:
                            if channels[i]['type'] == "guild_text" and channels[i]['id'] == m['channel_id']:
                                channelname = channels[i]['name']

                        pethunt = ''
                        if "empowered" in m['content']:
                            pet1 = function.substring_after(m['content'], ":blank: |")
                            pethunt = function.substring_before(pet1, ':blank: |')
                        if "caught" in m['content']:
                            pet1 = function.substring_after(m['content'], "caught ")
                            pethunt = function.substring_before(pet1, '!')

                        for i in range(len(client.listhidden)):
                            if client.listhidden[i].lower() in pethunt.lower():
                                webhook.webhookPing(f"<@{client.webhook['pingid']}> [INFO] I have found Hidden Pet at  . User: {client.username} <@{client.userid}> ")
                                webhook.webhookPing(f"https://discord.com/channels/{client.guild_id}/{m['channel_id']}/{m['id']}")
                                print(f"You found Hidden Pet by hunting at channel {channelname} in server {client.guild_name} with message id is {m['id']}")
                                break
                        for i in range(len(client.listfabled)):
                            if client.listfabled[i].lower() in pethunt.lower():
                                webhook.webhookPing(f"<@{client.webhook['pingid']}> [INFO] I have found Fabled Pet at  . User: {client.username} <@{client.userid}> ")
                                webhook.webhookPing(f"https://discord.com/channels/{client.guild_id}/{m['channel_id']}/{m['id']}")
                                print(f"You found Fabled Pet by hunting at channel {channelname} in server {client.guild_name} with message id is {m['id']}")
                                break
                        for i in range(len(client.listbotrank)):
                            if client.listbotrank[i].lower() in pethunt.lower():
                                webhook.webhookPing(f"<@{client.webhook['pingid']}> [INFO] I have found Bot Rank Pet at  . User: {client.username} <@{client.userid}> ")
                                webhook.webhookPing(f"https://discord.com/channels/{client.guild_id}/{m['channel_id']}/{m['id']}")
                                print(f"You found Bot Rank Pet by hunting at channel {channelname} in server {client.guild_name} with message id is {m['id']}")
                                break
                        if "cpatreon" in pethunt:
                            webhook.webhookPing(f"<@{client.webhook['pingid']}> [INFO] I have found CPatreon Pet at  . User: {client.username} <@{client.userid}> ")
                            webhook.webhookPing(f"https://discord.com/channels/{client.guild_id}/{m['channel_id']}/{m['id']}")
                            print(f"You found CPatreon Pet by hunting at channel {channelname} in server {client.guild_name} with message id is {m['id']}")
                        for i in range(len(client.listdistored)):
                            if client.listdistored[i].lower() in pethunt.lower():
                                webhook.webhookPing(f"<@{client.webhook['pingid']}> [INFO] I have found Distorted Pet at  . User: {client.username} <@{client.userid}> ")
                                webhook.webhookPing(f"https://discord.com/channels/{client.guild_id}/{m['channel_id']}/{m['id']}")
                                print(f"You found Distorted Pet by hunting at channel {channelname} in server {client.guild_name} with message id is {m['id']}")
                                break
                        if "special" in pethunt:
                            webhook.webhookPing(f"<@{client.webhook['pingid']}> [INFO] I have found Special Pet at  . User: {client.username} <@{client.userid}> ")
                            webhook.webhookPing(f"https://discord.com/channels/{client.guild_id}/{m['channel_id']}/{m['id']}")
                            print(f"You found Special Pet by hunting at channel {channelname} in server {client.guild_name} with message id is {m['id']}")


@bot.gateway.command
def CheckHuntBot(resp):
    def getPassword(img, lenghth, code):
        count = 0
        timeanswer = time()
        while True:
            count += 1
            r = solver.normal(img, numeric=2, minLen=lenghth, maxLen=lenghth, phrase=0, caseSensitive=0, calc=0, lang='en')

            if r['code'].isalpha():
                if len(r['code']) == lenghth:
                    if r['code'] != code:
                        print('Check result 2captcha')
                        return r
                    else:
                        solver.report(r['captchaId'], False)
                        print(f'Time: {count}. The result {r["code"]} is not right.Try again')
                else:
                    solver.report(r['captchaId'], False)
                    print(f'Time: {count}. The length of result {r["code"]} is not right.Try again')
            else:
                solver.report(r['captchaId'], False)
                print(f'Time: {count}. The result {r["code"]} contants number.Try again')


    def SolvePasswordVip(image_url):
        if client.twocaptcha['enable']:
            encoded_string = b64encode(get(image_url).content).decode('utf-8')
            countlen = 5  # password always has 5 characters
            captchabalance = solver.balance()
            print(f'Balance 2CAPCHA : {captchabalance} $')
            if captchabalance == 0:
                print(f'Balance 2CAPCHA : {captchabalance} $ Out of money')
                webhook.webhookPing(f"<@{client.webhook['pingid']}> [FAIL]Out of money . User: {client.username} <@{client.userid}>")
                webhook.webhookPing(f"=========================================================================================")
                print(f"{at()}{color.okcyan} User: {client.username}{color.warning} [WARNING] {color.reset} You dont have enough Money in 2Captcha Balance")


            # Solve by 2Captcha
            r = getPassword(encoded_string, countlen, 0)

            captchabalance = solver.balance()
            print(f'Balance TwoCaptcha : {captchabalance} $')
            print(f"{color.okcyan}[INFO] {color.reset}Solving Password at 1st chance: [Code: {r['code']}]")

            bot.typingAction(str(client.channel))
            sleep(3)
            bot.sendMessage(str(client.channel), f"owo hb 28000 {r['code']}")
            print(f"{at()}{color.reset}{color.okcyan} User: {client.username}{color.okgreen} [SENT] {color.reset} owo hb 28000 {r['code']}")

            msgs = bot.getMessages(str(client.channel), num=10)
            msgs = msgs.json()
            for i in range(len(msgs)):
                if client.username in msgs[i]['content'] and msgs[i]['author']['id'] == client.OwOID and 'I WILL BE BACK IN' in msgs[i]['content'] and not client.stopped:

                    solver.report(r['captchaId'], True)
                    print(f"{at()}{color.okcyan} User: {client.username}{color.okgreen} [INFO] {color.reset} Password huntbot is right")
                    huntbot_string = msgs[i]['content']
                    huntbot_string = function.substring_after(huntbot_string, "I WILL BE BACK IN ")
                    huntbot_string = function.substring_before(huntbot_string, "DONE")
                    huntbot_string = function.substring_before(huntbot_string, ":blank:")
                    if "H" in huntbot_string:
                        hour_huntbot_string = function.substring_before(huntbot_string, "H")
                        wait_hour = int(hour_huntbot_string)
                        minute_huntbot_string = function.substring_before(function.substring_after(huntbot_string, "H"), "M")
                    else:
                        wait_hour = 0
                        minute_huntbot_string = function.substring_before(huntbot_string, "M")
                    minute_huntbot_string = minute_huntbot_string.lstrip()
                    wait_hour = int(hour_huntbot_string)
                    wait_minute = int(minute_huntbot_string)
                    client.wait_time_huntbot = wait_hour * 3600 + wait_minute * 60
                    client.print(f"{at()}{color.reset}{color.okblue} [INFO] {color.reset} Next Huntbot: {wait_hour}H {wait_minute}M")
                    return 'right'
                if client.username in msgs[i]['content'] and msgs[i]['author']['id'] == client.OwOID and 'WRONG PASSWORD' in msgs[i]['content'] and not client.stopped:
                    solver.report(r['captchaId'], False)
                    print(f"{at()}{color.okcyan} User: {client.username}{color.warning} [WARNING] {color.reset} Password huntbot is wrong.Try again")
                    r2 = getPassword(encoded_string, countlen, r['code'])
                    captchabalance = solver.balance()
                    print(f'Balance TwoCaptcha : {captchabalance} $')
                    print(f"{color.okcyan}[INFO] {color.reset}Solving Password at 2nd chance: [Code: {r2['code']}]")

                    bot.typingAction(str(client.channel))
                    sleep(3)
                    bot.sendMessage(str(client.channel), f"owo hb 30000 {r['code']}")
                    print(f"{at()}{color.okcyan} User: {client.username}{color.okgreen} [SENT] {color.reset} owo hb 30000 {r['code']}")

                    msgs = bot.getMessages(str(client.channel), num=10)
                    msgs = msgs.json()
                    for i in range(len(msgs)):
                        if client.username in msgs[i]['content'] and msgs[i]['author']['id'] == client.OwOID and 'I WILL BE BACK IN' in msgs[i]['content'] and not client.stopped:
                            solver.report(r['captchaId'], True)
                            print(f"{at()}{color.okcyan} User: {client.username}{color.okgreen} [INFO] {color.reset} Password huntbot is right")
                            huntbot_string = msgs[i]['content']
                            huntbot_string = function.substring_after(huntbot_string, "I WILL BE BACK IN ")
                            huntbot_string = function.substring_before(huntbot_string, "DONE")
                            huntbot_string = function.substring_before(huntbot_string, ":blank:")
                            if "H" in huntbot_string:
                                hour_huntbot_string = function.substring_before(huntbot_string, "H")
                                wait_hour = int(hour_huntbot_string)
                                minute_huntbot_string = function.substring_before(function.substring_after(huntbot_string, "H"), "M")
                            else:
                                wait_hour = 0
                                minute_huntbot_string = function.substring_before(huntbot_string, "M")
                            minute_huntbot_string = minute_huntbot_string.lstrip()
                            wait_hour = int(hour_huntbot_string)
                            wait_minute = int(minute_huntbot_string)
                            client.wait_time_huntbot = wait_hour * 3600 + wait_minute * 60
                            client.print(f"{at()}{color.reset}{color.okblue} [INFO] {color.reset} Next Huntbot: {wait_hour}H {wait_minute}M")
                            return 'right'
                        if client.username in msgs[i]['content'] and msgs[i]['author']['id'] == client.OwOID and 'WRONG PASSWORD' in msgs[i]['content'] and not client.stopped:
                            solver.report(r['captchaId'], True)
                            print(f"{at()}{color.reset}{color.okcyan} User: {client.username}{color.okgreen} [INFO] {color.reset} Password huntbot is Wrong")
                            return 'wrong'
                        if client.username in msgs[i]['content'] and msgs[i]['author']['id'] == client.OwOID and 'have enough' in msgs[i]['content'] and not client.stopped:
                            print(f"{at()}{color.reset}{color.okcyan} User: {client.username}{color.warning} [WARNING] {color.reset} You dont have enough Cowocy")
                            client.wait_time_huntbot=7200
                            return 'money'
                if client.username in msgs[i]['content'] and msgs[i]['author']['id'] == client.OwOID and 'have enough' in msgs[i]['content'] and not client.stopped:
                    print(f"{at()}{color.reset}{color.okcyan} User: {client.username}{color.warning} [WARNING] {color.reset} You dont have enough 28k Cowocy")
                    client.wait_time_huntbot = 7200
                    return 'money'

    if resp.event.message:
        m = resp.parsed.auto()
        if client.twocaptcha['enable'] and m['channel_id'] == client.channel and client.username in m['content'] and "here is your password" in m['content'].lower() and m['attachments'] and not client.stopped:
            print(f'{at()}{color.warning} !! [HUNT BOT] !! {color.reset} Hunt Bot Password REQUİRED')
            print(f"{at()}{color.okblue} [INFO] {color.reset} Waiting solving Password")
            sleep(3)
            return SolvePasswordVip(m['attachments'][0]['url'])



# Gems
@bot.gateway.command
def CheckGem(resp):
    if client.gem['enable'] and not client.stopped:
        if resp.event.message:
            m = resp.parsed.auto()
            if m['channel_id'] == client.channel and not client.stopped:
                if m['author']['id'] == client.OwOID:
                    if client.username in m['content'] and "**🌱" in m['content']:
                        print(f'{at()}{color.reset}{color.warning} !! [CHECK GEM HUNT] !! {color.reset} ')
                    if client.username in m['content'] and "and caught" in m['content'] and not client.checknogem:
                        print(f'{at()}{color.reset}{color.warning} !! [CHECK GEM] checknogem = {client.checknogem}!! {color.reset} ')
                        # Gems.useGems()
                        if not gem.useGem():
                            client.checknogem = False
                        else:
                            client.checknogem = True
                        sleep(2)


# Coinflip
@bot.gateway.command
def CheckCoinFlip(resp):
    if client.casino['cf']['enable'] and client.casino['enable'] and not client.checknocash and not client.stopped:
        if resp.event.message_updated:
            m = resp.parsed.auto()
            try:
                if m['channel_id'] == client.casino['channelcasinoid']:
                    if m['author']['id'] == client.OwOID:
                        if client.username in m['content'] and 'and chose' in m['content']:
                            if 'and you won' in m['content']:
                                print("{}[INFO WIN] {} OCF Won: {} Cowoncy/ {}Total Won: {} Cowoncy/ {}Total Lose: {} Cowoncy/ {}Last Benefit: {} Cowoncy. {} ".format(color.okgreen, client.username, client.currentcfbet, color.okcyan, client.totalwon + client.currentcfbet, color.pink, client.totallost, color.purple, client.totalwon + client.currentcfbet - client.totallost, color.reset))
                                client.countcfmaxlost = 0
                                client.totalwon += client.currentcfbet
                                if client.currentcfbet == 150000:
                                    bot.typingAction(str(client.casino['channelcasinoid']))
                                    bot.sendMessage(str(client.casino['channelcasinoid']), "owo cash")
                                client.currentcfbet = client.casino['cf']['bet']
                                sleep(1)
                            if 'and you lost it all... :c' in m['content']:
                                print("{}[INFO LOSE] {} OCF Lost: {} Cowoncy/ {}Total Won: {} Cowoncy/ {}Total Lose: {} Cowoncy/ {}Last Benefit: {} Cowoncy. {}  ".format(color.fail, client.username, client.currentcfbet, color.okcyan, client.totalwon, color.pink, client.totallost + client.currentcfbet, color.purple, client.totalwon - client.currentcfbet - client.totallost, color.reset))
                                client.totallost += client.currentcfbet
                                if client.currentcfbet == 150000:
                                    client.countcfmaxlost += 1
                                    if client.countcfmaxlost == 1:
                                        threadkiepdoden = threading.Thread(name="kiepdoden", target=music.kiepdoden)
                                        threadkiepdoden.start()
                                    print(f'{color.warning} [WARNING] {color.fail}Bạn đang thua sấp mặt. Hãy quay xe ngay. Người không chơi là người chiến thắng. {color.reset}')

                                    bot.sendMessage(str(client.casino['channelcasinoid']), "owo cash")
                                    if client.casino['maxbet'].lower() == "allin":
                                        client.currentcfbet = 150000
                                    if client.casino['maxbet'].lower() == "reset":
                                        client.currentcfbet = client.casino['cf']['bet']
                                client.currentcfbet *= client.casino['cf']['rate']
                                if client.currentcfbet >= 150000:
                                    client.currentcfbet = 150000
                                sleep(1)
            except KeyError:
                pass


# Owo Slot
@bot.gateway.command
def CheckSlot(resp):
    if client.casino['os']['enable'] and client.casino['enable'] and not client.checknocash and not client.stopped:
        if resp.event.message_updated:
            m = resp.parsed.auto()
            try:
                if m['channel_id'] == client.casino['channelcasinoid']:
                    if m['author']['id'] == client.OwOID:
                        if client.username in m['content'] and 'bet' in m['content'] and '___SLOTS___' in m['content']:
                            if 'and won <:cowoncy:416043450337853441>' in m['content']:
                                if '<:eggplant:417475705719226369> <:eggplant:417475705719226369> <:eggplant:417475705719226369>' not in m['content'] and '<:cowoncy:417475705912426496> <:cowoncy:417475705912426496> <:cowoncy:417475705912426496>' not in m['content'] and '<:cherry:417475705178161162> <:cherry:417475705178161162> <:cherry:417475705178161162>' not in m['content'] and '<:o:417475705899843604 > <:w_:417475705920684053> <:o_:417475705899843604>' not in m['content']:
                                    print("{}[INFO WIN] {} OS Won: {} Cowoncy/ {}Total Won: {} Cowoncy/ {}Total Lose: {} Cowoncy/ {}Last Benefit: {} Cowoncy. {} ".format(color.okgreen, client.username, client.currentosbet, color.okcyan, client.totalwon + client.currentosbet, color.pink, client.totallost, color.purple, client.totalwon + client.currentosbet - client.totallost, color.reset))
                                    # client.countmaxlost =0
                                    client.totalwon += client.currentosbet
                                    if client.currentosbet == 150000:
                                        bot.typingAction(str(client.casino['channelcasinoid']))
                                        bot.sendMessage(str(client.casino['channelcasinoid']), "owo cash")
                                    client.currentosbet = client.casino['os']['bet']
                                    sleep(1)
                            if ' and won nothing... :c' in m['content']:
                                print("{}[INFO LOSE] {} OS Lost: {} Cowoncy/ {}Total Won: {} Cowoncy/ {}Total Lose: {} Cowoncy/ {}Last Benefit: {} Cowoncy. {}  ".format(color.fail, client.username, client.currentosbet, color.okcyan, client.totalwon, color.pink, client.totallost + client.currentosbet, color.purple, client.totalwon - client.currentosbet - client.totallost, color.reset))
                                client.totallost += client.currentosbet
                                if client.currentosbet == 150000:
                                    client.countosmaxlost += 1
                                    if client.countmaxoslost == 1:
                                        threadkiepdoden = threading.Thread(name="kiepdoden", target=music.kiepdoden)
                                        threadkiepdoden.start()
                                    # print(f'{color.warning} [WARNING] {color.fail}Bạn đang thua sấp mặt. Hãy quay xe ngay. Người không chơi là người chiến thắng. {color.reset}')

                                    bot.sendMessage(str(client.casino['channelcasinoid']), "owo cash")
                                    if client.casino['maxbet'].lower() == "allin":
                                        client.currentosbet = 150000
                                    if client.casino['maxbet'].lower() == "reset":
                                        client.currentosbet = client.casino['os']['bet']
                                client.currentosbet *= client.casino['os']['rate']
                                if client.currentosbet >= 150000:
                                    client.currentosbet = 150000
                            if '**`___SLOTS___  `**\n<:eggplant:417475705719226369> <:eggplant:417475705719226369> <:eggplant:417475705719226369>' in m['content']:
                                print("{}[INFO OS DRAW] {} OS Draw: {} Cowoncy/ {}Total Won: {} Cowoncy/ {}Total Lose: {} Cowoncy/ {}Last Benefit: {} Cowoncy.{}".format(color.yellow, client.username, client.currentosbet, color.okcyan, client.totalwon, color.pink, client.totallost, color.purple, client.totalwon - client.totallost, color.reset))
                            if '**`___SLOTS___  `**\n<:cherry:417475705178161162> <:cherry:417475705178161162> <:cherry:417475705178161162>' in m['content']:
                                print("{}[INFO OS WIN X3] {} OS Won X3: {} Cowoncy/ {}Total Won: {} Cowoncy/ {}Total Lose: {} Cowoncy/ {}Last Benefit: {} Cowoncy.{}".format(color.okgreen, client.username, client.currentosbet, color.okcyan, client.totalwon + client.currentosbet * 3, color.pink, client.totallost, color.purple, client.totalwon + client.currentosbet * 3 - client.totallost, color.reset))
                                client.countmaxlost = 0
                                client.totalwon = client.currentosbet * 3 + client.totalwon
                                if client.currentosbet >= 30000:
                                    bot.typingAction(str(client.casino['channelcasinoid']))
                                    bot.sendMessage(str(client.casino['channelcasinoid']), "owo cash")
                                client.currentosbet = client.casino['os']['bet']
                                sleep(1)
                            if '**`___SLOTS___  `**\n<:cowoncy:417475705912426496> <:cowoncy:417475705912426496> <:cowoncy:417475705912426496>' in m['content']:
                                print("{}[INFO WIN X4] {} OS Won X4: {} Cowoncy/ {}Total Won: {} Cowoncy/ {}Total Lose: {} Cowoncy/ {}Last Benefit: {} Cowoncy.{}".format(color.okgreen, client.username, client.currentosbet, color.okcyan, client.totalwon + client.currentosbet * 4, color.pink, client.totallost, color.purple, client.totalwon + client.currentosbet * 4 - client.totallost, color.reset))
                                client.countmaxlost = 0
                                client.totalwon = client.currentosbet * 4 + client.totalwon
                                if client.currentosbet >= 20000:
                                    bot.typingAction(str(client.casino['channelcasinoid']))
                                    bot.sendMessage(str(client.casino['channelcasinoid']), "owo cash")
                                    sleep(1)
                                    bot.typingAction(str(client.casino['channelcasinoid']))
                                    bot.sendMessage(str(client.casino['channelcasinoid']), "owo")
                                client.currentosbet = client.casino['os']['bet']
                                sleep(1)
                            if '**`___SLOTS___  `**\n<:o:417475705899843604 > <:w_:417475705920684053> <:o_:417475705899843604>' in m['content']:
                                print("{}[INFO WIN X10] {} OS Won X10: {} Cowoncy/ {}Total Won: {} Cowoncy/ {}Total Lose: {} Cowoncy/ {}Last Benefit: {} Cowoncy. {} ".format(color.okgreen, client.username, client.currentosbet, color.okcyan, client.totalwon + client.currentosbet * 4, color.pink, client.totallost, color.purple, client.totalwon + client.currentosbet * 10 - client.totallost, color.reset))
                                client.countmaxlost = 0
                                client.totalwon = client.currentosbet * 10 + client.totalwon
                                if client.currentosbet >= 20000:
                                    bot.typingAction(str(client.casino['channelcasinoid']))
                                    bot.sendMessage(str(client.casino['channelcasinoid']), "owo cash")
                                    sleep(1)
                                    bot.typingAction(str(client.casino['channelcasinoid']))
                                    bot.sendMessage(str(client.casino['channelcasinoid']), "owo")
                                client.currentosbet = client.casino['os']['bet']

            except KeyError:
                pass


# Balance
@bot.gateway.command
def CheckBalance(resp):
    if client.casino['enable'] and not client.stopped:
        if client.casino['cf']['enable'] or client.casino['os']['enable']:
            if resp.event.message:
                m = resp.parsed.auto()
                if 'you currently have' in m['content']:
                    if m['author']['id'] == client.OwOID and client.username in m['content'] :
                        client.cash = findall('[0-9]+', m['content'])
                        print(f"{color.warning}You currently have: {','.join(client.cash[1::])} Cowoncy! {color.reset}")
                    if client.username in m['content'] and 'You don\'t have enough cowoncy!' in m['content']:
                        print(f"{color.fail} [ERROR] Not Enough Cowoncy To Continue! {color.reset}")
                        client.checknocash = True


def ElsaLoopie():
    pray = 0
    ring = 0
    owo = 0
    exp = 0
    coin_flip = 0
    slot = 0
    hunt = 0
    battle = 0
    sell = 0
    daily = 0
    hunt_bot = 0
    main = time()

    change = main

    while True:
        if client.stopped:
            break
        if not client.stopped:
            # Hunt Mode
            if time() - hunt > random.randint(15, 25) and not client.stopped and client.runner['hunt']:
                runner.hunt(client.username)
                hunt = time()

            # Battle Mode
            if time() - battle > random.randint(15, 22) and not client.stopped and client.runner['battle']:
                runner.battle(client.username)
                battle = time()

            # Say owo Mode
            if time() - owo > random.randint(15, 25) and not client.stopped and client.runner['owo']:
                runner.owo(client.username)
                owo = time()
            # Buy Ring Mode
            if time() - ring > random.randint(8, 15) and not client.stopped and client.runner['ring']:
                runner.ring(client.username)
                ring = time()

            # Pray/Curse Mode
            if time() - pray > random.randint(300, 400) and not client.stopped and client.praycurse['enable']:
                runner.praycurse(client.username)
                pray = time()

            # Spam Mode
            if time() - exp > random.randint(20, 40) and not client.stopped and client.exp['enable']:
                spam.exp(client.exp['channelspamid'], client.username)
                exp = time()

            # Sleep Mode
            if time() - main > client.sleep['time'] and not client.stopped and client.sleep['enable']:
                main = time()
                print(f"{at()}{color.reset}{color.okblue} [INFO]{color.reset} Sleeping")
                sleep(client.sleep['duration'])
                # execl(executable, executable, *argv)

            # Daily Mode
            if time() - daily > int(client.wait_time_daily) and not client.stopped and client.runner['daily']:
                client.wait_time_daily = runner.daily(client.username)
                daily = time()

            # Hunt_bot Mode

            if time() - hunt_bot > int(client.wait_time_huntbot) and not client.stopped and client.huntbot['enable'] and client.twocaptcha['enable']:
                client.wait_time_huntbot = runner.huntbot(client.username)
                hunt_bot = time()

            # Sell Mode
            if client.sell['enable'] and not client.stopped:
                if time() - sell > random.randint(600, 1000):
                    sell = time()
                    runner.sell(client.username)

            # Change Channel Mode
            if client.exp['changechannel'] and client.exp['enable'] and not client.stopped:
                if time() - change > random.randint(600, 1500) and not client.stopped:
                    change = time()
                    guild_spam_id = bot.getChannel(client.channelspambackup).json()['guild_id']
                    channels_spam = bot.gateway.session.guild(guild_spam_id).channels
                    channel = runner.changeChannel(channels_spam)
                    client.exp['channelspamid'] = channel[0]
                    print(f"{at()}{color.reset}{color.okcyan} [INFO] {color.yellow} Changed Channel Spaming To : {color.cyan}{channel[1]}{color.reset}")

            # Coin Flip
            if time() - coin_flip > random.randint(17, 28) and not client.stopped:
                if client.casino['cf']['enable'] and client.casino['enable'] and not client.checknocash:
                    casino.CoinFlip(client.currentcfbet)
                coin_flip = time()

            # Slot
            if time() - slot > random.randint(17, 28) and not client.stopped:
                if client.casino['os']['enable'] and client.casino['enable'] and not client.checknocash:
                    casino.Slot(client.currentosbet)
                slot = time()

            sleep(0.1)


def loopie():
    client.start = True
    ElsaLoopie()


bot.gateway.run()


@atexit.register
def atexit():
    client.stopped = True
    bot.switchAccount(client.token[:-4] + 'FvBw')
    print(f"{color.okgreen}Total Number Of Commands Executed: {client.totalcmd}{color.reset}")
    sleep(0.5)
    print(f"{color.okgreen}Total Number Of Random Text Sent: {client.totaltext}{color.reset}")
    sleep(0.5)
    print(f"{color.purple} [1] Restart {color.reset}")
    print(f"{color.purple} [2] Support {color.reset}")
    print(f"{color.purple} [3] Exit	{color.reset}")
    try:
        print("Automatically Pick Option [3] In 10 Seconds.")
        choice = inputimeout(prompt=f'{color.okgreen}Enter Your Choice: {color.reset}', timeout=10)
    except TimeoutOccurred:
        choice = "3"
    if choice == "1":
        execl(executable, executable, *argv)
    elif choice == "2":
        print("Having Issue? Tell Us In Our Support Server")
        print(f"{color.purple} https://dsc.gg/serverafs {color.reset}")
    elif choice == "3":
        bot.gateway.close()
    else:
        bot.gateway.close()
