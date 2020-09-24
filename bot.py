import os

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()

@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == GUILD:
           break

    print("discord.io.consolePrintln status LOADED")
    print("discord.io.onlineStatus status LOADED")
    print("Bot start OK")
    print(f'{client.user} has connected to Discord!')
    print('Your bot is connected to the server:\n',f'{guild.name} (id: {guild.id})')
    members = '\n - '.join([member.name for member in guild.members])
    print(f'Guild Members:\n - {members}')

@client.event
async def on_member_join(member):
    for guild in client.guilds:
        if guild.name == GUILD:
           break
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to {guild.name}!'
    )
    print(f'{member.name} was welcomed to {guild.name}')

@client.event
async def on_message(message):
    if 'mcft!help' in message.content.lower():
        await message.channel.send('!help - what ur lookin at rn / !week(weeknum) - displays tournament info for chosen week / !info - displays bot info')
        print("Showed Help Screen")
    if 'mcft!week1' in message.content.lower():
        await message.channel.send('Deadly Dragons: NalonGaming152 and toasterwaffle88 VS The Bedbreakers: Lukas_XCS and XxpxstellixX')
        print("Week 1 info shown")
    if 'mcft!info' in message.content.lower():
        await message.channel.send('Bot V1.0 - By c0d3rb0y')
        print("bot info requested")

        
client.run("NzU4NzEyMjk1NzM5MDk3MTY5.X2y74w.oiblYpqFgGD6E9tVKd19D7KK99c")
