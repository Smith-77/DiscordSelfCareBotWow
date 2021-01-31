# bot.py
import os
import random
import privateMethods.negative_patterns as np
from dotenv import load_dotenv
from googlemaps import Client
from datetime import datetime
import json

import requests

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
    if np.contains_depression_traces(message.content.lower()):
        response = np.get_depression_response()
        await message.channel.send(response)
    #if np.is_overtly_negative(message.content.lower()):
    #    response = np.get_negative_response() # Really it gets a cheery response 
    #    await message.channel.send(response)
    await bot.process_commands(message)

@bot.command(name='exercise', help='Suggests an activity that will make you get up and move!')
async def offer_exercise(ctx):
    # pick an exercise
    exercises=['Go for a walk!',"How about a run? Don't forget to stretch!",'Stand up, walk around, and streeeeetch!','Try some yoga!','Head outside and explore! The world is your oyster.','Try some pushups. Down, up 1!','Find some friends and throw a frisbee']
    response = random.choice(exercises)
    await ctx.send(response)

@bot.command(name='findMuseums', help='Find local museums to visit! Invoke !findMuseums <location name>')
async def offer_park(ctx, *locations):
    location = ""
    for place in locations:
        location = location + place
    gmaps = Client('AIzaSyA0QJJKbsee6MVN7DAiVSeTUOV2F-V0rRs')
    latitude = gmaps.geocode(location)[0]['geometry']['location']['lat']
    longitude = gmaps.geocode(location)[0]['geometry']['location']['lng']
    results = findPlaces(latitude, longitude, "museum")
    MAX_RESULTS = 5
    curr_result = 0
    for result in results:
        if curr_result == MAX_RESULTS:
            return
        message = str(curr_result + 1) + ". Name: " + result['name'] + "\n\tLocation: " + result['vicinity']
        await ctx.send(message)
        curr_result = curr_result + 1

@bot.command(name='findParks', help='Find local parks to explore! Invoke !findParks <location name>')
async def offer_park(ctx, *locations):
    location = ""
    for place in locations:
        location = location + place
    gmaps = Client('AIzaSyA0QJJKbsee6MVN7DAiVSeTUOV2F-V0rRs')
    latitude = gmaps.geocode(location)[0]['geometry']['location']['lat']
    longitude = gmaps.geocode(location)[0]['geometry']['location']['lng']
    results = findPlaces(latitude, longitude, "park")
    MAX_RESULTS = 5
    curr_result = 0
    for result in results:
        if curr_result == MAX_RESULTS:
            return
        message = str(curr_result + 1) + ". Name: " + result['name'] + "\n\tLocation: " + result['vicinity']
        await ctx.send(message)
        curr_result = curr_result + 1

def findPlaces(lat, lng, tag, radius=4000, pagetoken = None):
   type = tag
   APIKEY='AIzaSyA0QJJKbsee6MVN7DAiVSeTUOV2F-V0rRs'
   url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={lat},{lng}&radius={radius}&type={type}&key={APIKEY}{pagetoken}".format(lat = lat, lng = lng, radius = radius, type = type,APIKEY = APIKEY, pagetoken = "&pagetoken="+pagetoken if pagetoken else "")
   print(url)
   response = requests.get(url)
   res = json.loads(response.text)
   # print(res)
   print("here results ---->>> ", len(res["results"]))
   return res["results"];

   # for result in res["results"]:
   #    info = ";".join(map(str,[result["name"],result["geometry"]["location"]["lat"],result["geometry"]["location"]["lng"],result.get("rating",0),result["place_id"]]))
   #    print(info)
   # pagetoken = res.get("next_page_token",None)

   # print("here -->> ", pagetoken)

   # return pagetoken

@bot.command(name='sendACompliment', help='Send a compliment to another user!')
async def offer_park(ctx):
    compliments = ['You are more fun than bubble wrap',
    'You are the most perfect you there is.',
    'You are enough.',
    'You are one of the smartest people I know.',
    'You look great today.',
    'You have the best smile.',
    'You light up the whole server.']
    response = random.choice(compliments)
    await ctx.send(response)
    await message.author.send(response)

bot.run(TOKEN)