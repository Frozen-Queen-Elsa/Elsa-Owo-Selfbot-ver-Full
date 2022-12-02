from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import chromedriver_binary
import os
from information import information
import undetected_chromedriver as uc

try:

    from discum import *
    from discum.utils.slash import SlashCommander
    from discord_webhook import DiscordWebhook
except:
    from setup import install

    install()
    from discum import *
    from discord_webhook import DiscordWebhook

client = information()
api = client.twocaptcha['api']
token = client.token

import undetected_chromedriver as uc

if client.twocaptcha['enable']:
    # Setting Chrom extension
    chrome_options = uc.ChromeOptions()
    chrome_options.add_extension('..\src\TwoCaptchaAutoSolve.crx')

    driver = uc.Chrome(options=chrome_options)

    # Setting key 2Captcha Solver
    driver.get('chrome-extension://ifibfemgeogfhoebkmokieepdoobkbpo/options/options.html')
    inputkey = driver.find_element(By.CSS_SELECTOR, value='body > div > div.content > table > tbody > tr:nth-child(1) > td:nth-child(2) > input[type=text]')
    driver.execute_script("document.getElementsByName('apiKey')[0].value=arguments[0]", api)

    # click Login
    loginbutton = driver.find_element(By.CSS_SELECTOR, "#connect")
    driver.execute_script("arguments[0].click();", loginbutton)

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

    while True:
        # Dợi extension solver hiện rồi f5 vì để ko bị lỗi sitekey
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "captcha-solver")))
        driver.refresh()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "captcha-solver")))
        solvebutton = driver.find_element(By.CLASS_NAME, "captcha-solver")
        sleep(3)
        driver.execute_script("arguments[0].click();", solvebutton)
        if WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.CLASS_NAME, "captcha-solver-info"), "Solving")):
            break

    # Wait
    if WebDriverWait(driver, 90).until(EC.text_to_be_present_in_element((By.CLASS_NAME, "captcha-solver-info"), "Captcha solved!")):

        if client.webhookping != 'None':
            webhook = DiscordWebhook(url=client.webhook, content=f"<@{client.webhookping}> Solve Captcha Link Successfully  . User: {client.username} <@{client.userid}>")

        else:
            webhook = DiscordWebhook(url=client.webhook, content=f"<@{client.userid}> <@{client.allowedid}> Solve Captcha Link Successfully. User: {client.username} <@{client.userid}>")
        # os.system('python "mainvip.py"')
        sleep(5)
        driver.quit()

    webhook = DiscordWebhook(url=client.webhook, content=f"<@{client.webhookping}> Solve Captcha Link Fail  . User: {client.username} <@{client.userid}>")

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


