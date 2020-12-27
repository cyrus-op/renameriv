from telethon import TelegramClient, events, Button
    #import requests
from bs4 import BeautifulSoup as BS

import asyncio

import subprocess

import requests

#from headers import headers

#import urls

import os
import subprocess

#import cryptg

import youtube_dl #import YoutubeDL

#from __future__ import unicode_literals

#from __future__ import unicode_literals



import logging

logging.basicConfig(level=logging.WARNING)

#from flask import request
#import os
#from flask import request

client = TelegramClient('anfghohn', int(os.environ.get("APP_ID" )), os.environ.get("API_HASH")).start(bot_token= os.environ.get("TG_BOT_TOKEN"))
@client.on(events.NewMessage(pattern='/start'))
async def handler(event):
#@client.on(events.NewMessage(pattern='/start




    
    
    #await
    
    






# Handle all callback queries and check data inside the handler

    
    
    
    
    #print(f)
   # format= xxx.split(" ")
   # if os.path.exists(event.sender.username):

   # await event.answer("fff")
    #if event.data == b'yes':
        



    #chat = await event.get_media()
    #chat = await event.get_media()
#def callback(current, total):
  #  print('Downloaded', current, 'out of', total,
   #       'bytes: {:.2%}'.format(current / total))
@client.on(events.NewMessage(pattern='(?i)/rename'))

async def handler(event):
    chat = await event.get_chat()
    print(chat)
    dw = await event.get_reply_message()
    links =event.text.split(" ")[1]
    print(links)
  #  print("hi")
    with open("./Download/"+links, 'wb') as fd:
        async for chunk in client.iter_download(dw.media):
            fd.write(chunk)
            print("hh")
    await client.send_message(chat,links,file="./Download/"+links,force_document=True)
    os.remove("./Download/"+links)
   # for x in dw:
        

  #  dw = await event.get_reply_message(med)
    #print(dw)
    #ls = await event.respond("77")
  #  if dw == "True":
      #  await client.download_media()
       # print("gi")
    #if dw in 
   # print(chat)
  #  links =event.text.split(" ")[1]
   # outf = event.sender.username
   # print(event.message)

 #
   # dws = await 
   # print(dw)
    #if os.path.exists(links):
     #   await client.send_file(chat,links,force_document=True)

    #path = await client.download_media(message)
    
   # path = await client.download_media(event.message)
    #await client.download_media(event.message, filename)
    #await client.download_media(event.message)
#async def send(event,)
@client.on(events.NewMessage(pattern='(?i)/ls'))



async def handler(event):


    chat = await event.get_chat()
    links =event.text.split(" ")[1]
    split = links.split("/")[-1]
    print(split)
    link =" https://zee5.tpro.ga/"+split
    print(split)
    outf = event.sender.username
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        Y=ydl.extract_info("https://zee5-player.vercel.app/player?id="+split, download=False)
    X = Y
    for x in range(len(X)):
        #Op=x
        #print (Op)
        
        #print(Op)
        ytdlf= X["entries"][0]["formats"][x]["format"]
        await client.send_message(chat, 'https://www.zee5.com', buttons=
    Button.inline(ytdlf,link+"b"+ytdlf))
    #c = subprocess.getoutput("youtube-dl"+" -F "+link)
    #await client.send_message(chat,c)


    #str1.join(s)



    #print(c)



    #await client.send_message(chat,c.join(e))




client.start()

client.run_until_disconnected()
