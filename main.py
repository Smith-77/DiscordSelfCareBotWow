# bot.py
import os
import random
import privateMethods.negative_patterns as np
from dotenv import load_dotenv
import googlemaps
from datetime import datetime

# 1
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# 2
bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    elif np.contains_depression_traces(message.content.lower()):
        response = np.get_depression_response()
        await message.channel.send(response)
    await bot.process_commands(message)

@bot.command(name='exercise', help='Suggests an activity that will make you get up and move!')
async def offer_exercise(ctx):
    # pick an exercise
    exercises=['walk','run','stretch','yoga']
    response = random.choice(exercises)
    await ctx.send(response)

@bot.command(name='findParks', help='Suggests a local park to exercise in!')
async def offer_park(ctx, location):
    gmaps = googlemaps.Client(key="AIzaSyBAe9LcHsZWFsVrKi5VSZRekrIqxLtv5Ug")
    local_park = gmaps.local_search('park near ' + location)
    park_name = local_park['responseData']['results'][0]['titleNoFormatting']
    await ctx.send(park_name)

bot.run(TOKEN)