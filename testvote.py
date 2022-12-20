from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data import data
import undetected_chromedriver as uc

client = data()
driver = uc.Chrome()
token =client.token

driver.get('https://discord.com/login?redirect_to=%2Foauth2%2Fauthorize%3Fscope%3Didentify%2520guilds%2520email%26redirect_uri%3Dhttps%253A%252F%252Ftop.gg%252Flogin%252Fcallback%26response_type%3Dcode%26client_id%3D422087909634736160%26state%3DL2JvdC80MDg3ODUxMDY5NDIxNjQ5OTIvdm90ZQ%3D%3D')
js = 'function login(token) {setInterval(() => {document.body.appendChild(document.createElement `iframe`).contentWindow.localStorage.token = `"${token}"`}, 50);setTimeout(() => {location.reload();}, 500);}'

driver.execute_script(js + f'login("{token}")')

WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'button[class="button-f2h6uQ lookFilled-yCfaCM colorBrand-I6CyqQ sizeMedium-2bFIHr grow-2sR_-F"]'))
    )

driver.find_element(By.CSS_SELECTOR, value='button[class="button-f2h6uQ lookFilled-yCfaCM colorBrand-I6CyqQ sizeMedium-2bFIHr grow-2sR_-F"]').click()


WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[class="chakra-button css-ed599q"]'))
    )

driver.find_element(By.CSS_SELECTOR, value='button[class="chakra-button css-ed599q"]').click()

print('VOTED')
sleep(5)
driver.quit()