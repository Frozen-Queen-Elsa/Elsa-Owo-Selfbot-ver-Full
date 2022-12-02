from information import information
from time import sleep, strftime, localtime
from color import color
from discord_webhook import DiscordWebhook

client = information()


class webhooks:
    def __init__(self, bot):
        self.bot = bot

    def webhookPing(self, message):
        if client.webhook['enable']:
            webhook = DiscordWebhook(url=client.webhook['link'], content=message)
            webhook = webhook.execute()

    # Ping Webhook moded
    def webhookping(self, name, id):
        if client.webhook['enable']:
            if client.casino['enable']:
                if client.casino['cf']['enable'] or client.casino['os']['enable']:
                    self.webhookPing(f"<@{client.webhook['pingid']}> I Found A Captcha In Channel: <#{client.channel}> or <#{client.casino['channelcasinoid']}> . User: {name} <@{id}>")
                else:
                    self.webhookPing(f"<@{client.webhook['pingid']}> I Found A Captcha In Channel: <#{client.channel}>  . User: {name} <@{id}>")
            else:
                self.webhookPing(f"<@{client.webhook['pingid']}> I Found A Captcha In Channel: <#{client.channel}>  . User: {name} <@{id}>")

        else:
            if client.casino['enable']:
                self.webhookPing(f"<@{id}> I Found A Captcha In Channel: <#{client.channel}>  or <#{client.casino['channelcasinoid']}> . User: {name} <@{id}>")
            else:
                self.webhookPing(f"<@{id}> I Found A Captcha In Channel: <#{client.channel}>. User: {name} <@{id}>")
