import discord
import random
import asyncio
import aiohttp
import json
import os


from gtts import gTTS

from discord import Game
from discord.ext import commands
from discord.ext.commands import Bot
from discord.voice_client import VoiceClient

from pynput.keyboard import Key, Controller as KeyboardController
from pynput.mouse import Button, Controller as MouseController
from pynput.keyboard import Listener

import datetime
import time, threading

import json

import pyperclip

import gspread
from oauth2client.service_account import ServiceAccountCredentials


################################# WEB SCRAP
import time
#from selenium import webdriver
#import pandas as pd
#from selenium.webdriver.chrome.options import Options
#driver = webdriver.Chrome('C:/chromeDriver/chromedriver.exe')
################################## TELEGRAM
import telegram
from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters
from telegram.ext.dispatcher import run_async
import logging

## CONFIG DISCORD
TOKEN_DISCORD = 'NzM1ODc2MTQxMzc3NjUwODA3.XxmpHw.zai54Mi-ZUmcpE8EI3NicF428m8'
discordBot = commands.Bot(command_prefix='$')
client = discord.Client()
canalGeneral = client.get_channel(12324234183172)

## CONFIG TELEGRAM
token_bot_telegram = '661519015:AAE93y5F6kcaXkWcWDcLBZTwYACjTP0eloA'
updater = Updater(token=token_bot_telegram, use_context=True)
dispatcher = updater.dispatcher
telegramBot = telegram.Bot(token=token_bot_telegram)
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

######################################################################### TELEGRAM #####################################################
def start(update, context):
    context.telegramBot.send_message(chat_id=update.effective_chat.id, text="Holis!!!")

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

def read(update, context):
arguments = "".join(context.args)
update.message.reply_text("Leyendo: " + arguments)
print("read"+ arguments)

read_handler = CommandHandler('read', read, pass_args=True)
dispatcher.add_handler(read_handler)
updater.start_polling()

@run_async
def toall(update, context):
arguments = "".join(context.args)
update.message.reply_text("Mensaje enviado a DISCORD: " + arguments)
discordBot.event.canalGeneral.send('Mensaje desde Telegram: '+ arguments)

read_handler = CommandHandler('toall', toall, pass_args=True)
dispatcher.add_handler(read_handler)

def leerWeb(arg):
if arg == 'marca':
driver.get('http://www.marca.com/');
time.sleep(5) # Esperamos 5 segundos a que se muetre la web


# search_box = driver.find_element_by_name('q')
# search_box.send_keys('ChromeDriver '+str(n))
# search_box.submit()
# time.sleep(5) # Esperamos 5 segundos a que se muetre la webt
# n+=1

#https://selenium-python.readthedocs.io/locating-elements.html





####################################################################################### DISCORD ##############################################


if not discord.opus.is_loaded():
discord.opus.load_opus('opus')

@discordBot.event
async def on_ready():
    print('-----------------------------')
    print('-----------------------------')
    print('-----------------------------')
    print('Discord bot logged in as '+str(discordBot.user.name))
    print("User id: "+str(discordBot.user.id))
    print('-----------------------------')
    print('-----------------------------')
    print('-----------------------------')



@discordBot.event
async def on_voice_state_update(member, before, after):
if before.channel is None and after.channel is not None:
before.channel.play(discord.FFmpegPCMAudio('music/roger.mp3'), after=lambda e: print('said Hi', e))


'''
@discordBot.event
async def on_message(message):
if message.author == discordBot.user:
return
if message.content.startswith("jarvis ven"):
author = message.author
channel = author.voice_channel
await discordBot.send_message(message.channel, "Ya voy " + author.name + "!")
await discordBot.join_voice_channel(author.voice_channel)
elif "wipe" in message.content:
author = message.author
channel = author.voice_channel
await discordBot.send_message(message.channel, "Quien hablo de WIPEEEEEE?!!"+"\n"+"https://d18lkz4dllo6v2.cloudfront.net/cumulus_uploads/entry/12848/nuclear.jpg?pw=1200")
elif message.content.startswith("jarvis "):
author = message.author
channel = author.voice_channel
await discordBot.send_message(message.channel, author.name + " no te entiendo compadre")
'''

@discordBot.command()
async def entra(ctx):
channel = ctx.message.author.voice.channel
vc = await channel.connect()
vc.play(discord.FFmpegPCMAudio('music/roger.mp3'), after=lambda e: print('said Hi', e))


@discordBot.command()
async def habla(ctx):
saved = "Holis"
tts = gTTS(text=saved, lang='es', slow=False)
with open('music/mensaje.mp3', 'wb') as f:
tts.write_to_fp(f)

channel = ctx.message.author.voice.channel
vc = await channel.connect()
vc.play(discord.FFmpegPCMAudio('music/mensaje.mp3'), after=lambda e: print('said: '+saved, e))


@discordBot.command()
async def tiempo(ctx, arg):
await ctx.send("http://www.aemet.es/es/eltiempo/prediccion/municipios?str="+arg+"&modo=and&orden=n&tipo=sta")


@discordBot.command()
async def follar(ctx, arg):
if arg == "keipaso":
await ctx.send("https://vozlibre.com/wp-content/uploads/2017/07/julio-iglesias.jpg")
else:
await ctx.send("https://cdn.memegenerator.es/imagenes/memes/full/2/7/2070084.jpg")


@discordBot.command()
async def auto(ctx):
user = ctx.message.author
channel = ctx.message.author.voice.channel
msg = await ctx.send("Informacion Clasificada:...")
msgTime = "Este mensaje se autodestruira en... "
timeWait = await ctx.send(msgTime)
for x in range(5, 0,-1):
time.sleep(1)
await timeWait.edit(content=msgTime+str(x))
await timeWait.delete()
await msg.delete()
await ctx.message.delete()


@discordBot.command()
async def invi(ctx):
user = ctx.message.author
channel = ctx.message.author.voice.channel
invitelinknew = await channel.create_invite(destination=channel, xkcd=True, max_uses=100)
await ctx.send(invitelinknew.url)


discordBot.run(TOKEN_DISCORD)