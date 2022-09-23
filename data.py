from version import Version
from requests import get
from color import color
from menu import UI
from time import sleep
from re import findall
from inputimeout import TimeoutOccurred, inputimeout
import json
ui = UI()
class data:
	def __init__(self):
		self.commands=[
			"hunt",
			"hunt",
			"battle"
			]
		self.wbm = [13,18]
		self.OwOID = '408785106942164992'
		self.totalcmd = 0
		self.totaltext = 0
		self.username=""
		self.userid = ""
		self.checknogem=False
		self.stopped = False
		self.version = int(''.join(map(str, Version)))
		self.wait_time_daily = 60
		self.channel2 = []

		#OCF
		self.checknocash=False
		self.totalwon=0
		self.totallost=0
		self.checknocash=False
		self.countcfmaxlost=0
		self.countosmaxlost=0
		#Gems
		self.checkgemtime=0
		self.checkusegem = 0
		self.skipcheckgem=0
	

		with open('settings.json', "r") as file:
			data = json.load(file)
			self.token = data["token"]
			self.channel = data["channel"]
			self.channelspam=data['channelspam']
			self.gm = data["gm"]
			self.wcrate = data["wcrate"]
			self.lbox = data["lbox"]
			self.usegem = data["usegem"]
			self.sm = data["sm"]
			self.pm = data["pm"]
			self.prayid = data["prayid"]
			self.em = data["em"]
			self.prefix = data["prefix"]
			self.allowedid = data["allowedid"]
			self.webhook = data["webhook"]
			self.webhookping = data["webhookping"]
			self.daily = data["daily"]
			self.stop = data["stop"]
			self.change = data['change']			
			self.sell = data['sell']
			self.solve = data['solve']
			self.sound = data['sound']
			self.rhunt = data['rhunt']
			self.rbattle = data['rbattle']
			self.rowo = data['rowo']
			self.rbuyring = data['rbuyring']
			#OCF
			self.casinom =data['casinom']
			self.cfm =data['cfm']
			self.cfbet = int(data["cfbet"])
			self.current_cfbet = self.cfbet
			self.cfrate = int(data["cfrate"])
			self.osm =data['osm']
			self.osbet = int(data["osbet"])
			self.current_osbet = self.osbet
			self.osrate = int(data["osrate"])
			self.maxbet = data["maxbet"]
			self.channelocf =data["channelocf"]
			self.api=data['api']
		self.tokenbackup=self.token
		self.channelspambackup=self.channelspam

	def Version(self):
		response = get("https://raw.githubusercontent.com/ahihiyou20/discord-selfbot-owo-bot/development/source/src/version.py")
		version = response.text
		version = findall(r'\b\d+\b', version)
		return int(''.join(version))
	def check(self):
		version = self.Version()
		if self.token and self.channel == 'nothing':
			print(f"{color.fail} !!! [ERROR] !!! {color.reset} Please Enter Information To Continue")
			sleep(2)
			from newdata import main
			main()
		else:
			response = get('https://discord.com/api/v9/users/@me',headers={"Authorization": self.token})
			if response.status_code != 200:
				print(f"{color.fail} !!! [ERROR] !!! {color.reset} Invalid Token")
				sleep(2)

a = data()
a.check()
