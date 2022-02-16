from dis import disco
import os
import time
import requests

import discord
from dotenv import load_dotenv


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')


client = discord.Client()


@client.event
async def on_ready():
    print(f'{client.user.name} has connected to discord')

    activity = discord.Activity(
        type=discord.ActivityType.watching, name="BUD price on png.fi")
    await client.change_presence(activity=activity)

    # Updates price every 30s
    while True:
        response = requests.get('https://api.png.fi/prices/BUD')
        await client.user.edit(username=str(round(response.json()['BUD'], 2)) + ' PAI')
        time.sleep(30)
        print(f"{response.json()['BUD']} PAI @ {time.asctime( time.localtime(time.time()) )}")
     
        

client.run(TOKEN)
