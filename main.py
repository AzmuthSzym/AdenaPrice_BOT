import discord
from price.price import price_request
import os


client = discord.Client()

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('!price'):
    await message.channel.send(price_request())

client.run(os.getenv('TOKEN'))