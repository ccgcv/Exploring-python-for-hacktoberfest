import discord
import os
import requests
import json
from replit import db
from discord.ext import commands, tasks
from itertools import cycle
from acti_ve import acti_ve

intents = discord.Intents.default()  
intents.members = True  
client = commands.Bot(command_prefix="//", intents=intents)

status = cycle(['F1 Bot','RMX-3370', 'Made by Liege', 'Use $inspire for inspiration? LOL', 'LMX3370 😎'])

key_words = ['insert the words u wish to block']

starter_prime = [":)"]


if "responding" not in db.keys():
  db["responding"] = True

def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]["q"] + " - " + json_data[0]["a"]
  return (quote)

@client.event
async def on_ready():
    change_status.start()
    print('Bot is ready')

@tasks.loop(seconds=10)
async def change_status():
     await client.change_presence(activity=discord.Game(next(status)))


@client.event
async def on_message(message):
  if message.author == client.user:
    return


  msg = message.content

  if message.content.startswith("$inspire"):
    quote = get_quote()
    await message.delete()
    await message.channel.send(quote, delete_after = 60)

  if msg.startswith('https://discord.gg'):
    await message.delete()
    await message.channel.send('Discord invite links are not allowed in the server {}'.format(message.author.mention)+ ' <@346191126320906242> ' , delete_after=5)

  if msg.startswith('discord.gg'):
    await message.delete()
    await message.channel.send('Discord invite links are not allowed in the server {}'.format(message.author.mention)+ ' <@346191126320906242> ', delete_after=5)  

  if msg.startswith('https://dlscocrdapp.com/nitro'):
    await message.delete()
    await message.channel.send('Want bun? {}'.format(message.author.mention)+ ' <@346191126320906242> ', delete_after=2)

  if message.content.startswith("#2kmax"):
    quote = get_quote()
    await message.delete()
    await message.channel.send('''2000 members completed, signor''' + ' <@346191126320906242> ' + ' 🦾 ')


  if db["responding"]:  
   options = starter_prime
   if "prime" in db.keys():
     options = options + db["prime"]

   if any(word in msg for word in key_words):
     await message.delete()
     await message.channel.send('These words are not allowed in the server {}'.format(message.author.mention)+ ' <@346191126320906242> ')
     
acti_ve()
client.run(os.getenv("TOKEN"))
