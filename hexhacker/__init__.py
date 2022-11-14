import os 
from telethon.sync import TelegramClient 
from telethon.sessions import StringSession 
from Asuna.env import *

def mention(name, userid):
  return f"[{name}](tg://user?id={userid})"

asunaub = TelegramClient(StringSession(SESSION), API_ID, API_HASH)
asuna = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN)
