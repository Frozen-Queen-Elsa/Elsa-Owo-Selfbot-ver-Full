from playsound import playsound
from information import information
client = information()

class musics:


    def captchamusic(self):
        if client.sound:
            playsound('..\src\KhueMocLang.mp3')
            #playsound('Files/Captcha.mp3')

    def solvedmusic(self):
        if client.sound:
            playsound('..\src\Solved.mp3')

    def kiepdoden(self):
        if client.sound :
            playsound("..\src\KiepDoDen.mp3")