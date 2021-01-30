# bot.py
import os
import random
from dotenv import load_dotenv

# 1
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# 2
bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

@bot.command(name='exercise', hep='Suggests an activity that will make you get up and move!')
async def offer_exercise(ctx):
    exercises=['walk','run','stretch','yoga']
    response = random.choice(exercises)
    await ctx.send(response)

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    elif 'depression' in message.content.lower():
        response = "No"
        await message.channel.send(response)
    await bot.process_commands(message)

bot.run(TOKEN)