from dis import disco
import os
import time
import requests
import discord
from discord.ext import tasks
from dotenv import load_dotenv


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')


client = discord.Client()


@tasks.loop(seconds=5)
async def fetch_price():
    response = requests.get('https://api.png.fi/prices/BUD')
    await client.user.edit(username=str(round(response.json()['BUD'], 2)) + ' PAI')
    print(
        f"{response.json()['BUD']} PAI @ {time.asctime( time.localtime(time.time()) )}")


@client.event
async def on_ready():
    print(f'{client.user.name} has connected to discord')

    activity = discord.Activity(
        type=discord.ActivityType.watching, name="BUD price on png.fi")
    await client.change_presence(activity=activity)
    fetch_price.start()

client.run(TOKEN)
