import discord
import re

class MyClient(discord.Client):
	async def on_ready(self):
		print('Logged in as')
		print(self.user.name)
		print(self.user.id)
		print('------')

	async def on_message(self, message):
		print(message.channel.id)
		if message.channel.id == 763760059280785409:    #source chanel id
			if message.author.name != self.user.name:
				if (re.search(r'(BTO|STC)\s\w+\s\d+\w\s\d+/\d+\s@\d+.\d+', message.content)) and not (re.search(r'risk|lotto', message.content)):
					channel = self.get_channel(764526822641106955) #destination chanel id
					await channel.send(re.search(r'(BTO|STC)\s\w+\s\d+\w\s\d+/\d+\s@\d+.\d+', message.content)[0])


client = MyClient()
client.run('NzY0NTI1OTE5MzQ3NjcxMDQw.X4HiPw.PjsUinyctJO3jSNDwjFdrCNe66g') #your bot token