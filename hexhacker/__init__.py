import os 
from telethon.sync import TelegramClient 
from telethon.sessions import StringSession 
from hexhacker.env import *

def mention(name, userid):
  return f"[{name}](tg://user?id={userid})"

asunaub = TelegramClient(StringSession(SESSION), API_ID, API_HASH)
