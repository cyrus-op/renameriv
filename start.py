from telethon import TelegramClient, events, Button
    #import requests
#from bs4 import BeautifulSoup as BS
import cryptg
import asyncio
import time

import subprocess

import requests
import shutil

#from headers import headers

#import urls

import os
import subprocess

#import cryptg

#import youtube_dl #import YoutubeDL

#from __future__ import unicode_literals

#from __future__ import unicode_literals



import logging

logging.basicConfig(level=logging.WARNING)

# import request

client = TelegramClient('anfghvygggghbohn',os.getenv("a"),os.getenv("b")).start(bot_token=os.getenv("c"))
   
   
   


             #   fd.write(chunk)

              #  print("hh")

    #links =event.text.split(" ")[1]
                #print("hh")
            
              #  print("hh")

   # with open(f"./Download/{chat.username}/n.jpg", 'wb') as fd:

           # async for chunk in client.iter_download(dw.media):

              #  fd.write(chunk)

              #  print("hh")
    #links =event.text.split(" ")[1]
  #  print(links)
  #  if not os.path.exists("storage/dcim/605/telegram/"+chat.username):
    #os.mkdir("./Download/"+chat.username)
    
 

@client.on(events.NewMessage(pattern='(?i)/thumbnail'))

async def handler(event):

    chat = await event.get_chat()

    

    print(chat.username)

    dw = await event.get_reply_message()

    #links =event.text.split(" ")[1]

  #  print(links)

    if not os.path.exists("storage/dcim/605/telegram/"+chat.username):

        os.mkdir("./Download/"+chat.username)

        with open(f"./Download/{chat.username}/n.jpg", 'wb') as fd:

            async for chunk in client.iter_download(dw.media,chunk_size=128):

                fd.write(chunk)

                print("hh")

@client.on(events.NewMessage(pattern='(?i)/del_thumbnail'))

async def handler(event):

    chat = await event.get_chat()

    

    print(chat.username)

    

    #dw = await event.get_reply_message()

    shutil.rmtree("./Download/"+chat.username)

    await client.send_message(chat,"thumbnail deleted")
@client.on(events.NewMessage(pattern='(?i)/rename'))
async def handler(event):
    chat = await event.get_chat()
    print(chat)
    dw = await event.get_reply_message()
    links =event.text.split(" ")[1]
    if not os.path.exists(chat.username+".jpg"):

        ss=await dw.download_media("filename")

        await client.send_message(chat,ss+"renaming")

        os.rename(ss,links)

        await client.send_file(chat,links)

        os.remove(links)

    if os.path.exists(chat.username+".jpg"):

        ss=await dw.download_media("filename")

        await client.send_message(chat,ss+"renaming")

        os.rename(ss,links)

        await client.send_file(chat,links,thumb=chat.username+".jpg",force_document=True)

        os.remove(links)

        
  #  print(links)
#    ss=await dw.download_media("filename")

   # await client.send_message(chat,ss+"renaming")

    #os.rename(ss,links)
   # await client.send_file(chat,links)
   # os.remove(links)
   # with open("./Download/"+links, 'wb') as fd:

            #async for chunk in client.iter_download(dw.media):

               # fd.write(chunk)

               # print("hh")

               # await client.send_message(chat,links,file="./Download/"+links,force_document=True)
               # time.sleep(50)

             #   await client.send_message(chat,"file uploaded over streaming")

              #  os.remove("./Download/"+links)
    #if not os.path.exists("./Download/"+chat.username+"/n.jpg"):
    # with open("./Download/"+links, 'wb') as fd:
          #  async for chunk in client.iter_download(dw.media):
               # fd.write(chunk)
                #print("hh")
       # await client.send_message(chat,links,file="./Download/"+links,force_document=True)
        #await client.send_message(chat,"file uploaded over streaming")
        #os.remove("./Download/"+links)

        
  #  if os.path.exists("./Download/"+chat.username+"/n.jpg"):
      #  with open("./Download/"+links, 'wb') as fd:
          #  async for chunk in client.iter_download(dw.media):
               # fd.write(chunk)
              #  print("hh")
              #  await client.send_file(chat,file="./Download/"+links,thumb="./Download/"+chat.username+"/n.jpg",force_document=True)
              #  os.remove("./Download/"+links)


client.start()

client.run_until_disconnected()
