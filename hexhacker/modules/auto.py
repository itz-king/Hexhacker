from hexhacker import *
from telethon import events, Button
from datetime import datetime as dt
from hexhacker.env import *
import asyncio
import random

statss=[]

@hexhacker.on(events.NewMessage(chats=572621020))
async def scam2(event):
    if "Shiny pokemon found!" in event.raw_text:
        await hexhacker.disconnect()

@hexhacker.on(events.NewMessage(chats=572621020,incoming=True))
async def heck(event):
  if len(statss) >0:
    randm=round(random.uniform(5,10),2)
    await asyncio.sleep(randm)
    await hexhacker.send_message()
    
@hexhacker.on(events.NewMessage(outgoing=True, pattern=r"^.hexa ?(.*)"))
async def stats(event):
  args=event.text[6:]
  if args=="on":
    statss.append("True")
  elif args=="off":
    statss.pop()
