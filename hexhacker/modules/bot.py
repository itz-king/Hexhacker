from Asuna import *
from telethon import events, Button
from datetime import datetime as dt
from Asuna.env import *

HELP_STR="""✘ Commands Available
• `.alive`
    Check if your bot is working.
    
• `.ping`
    Check Ultroid's response time.
    
• `.shutdown`
    Turn off your bot.
"""

@asunaub.on(events.NewMessage(outgoing=True, pattern=r'^.alive'))
async def alive(slime):
  me = await asunaub.get_me()
  date = dt.now()
  date = date.strftime("%B %d, %Y")
  kek = mention(me.first_name, me.id)
  await slime.delete()
  await asunaub.send_file(slime.chat_id , ALIVE_PIC , caption=f"**「 Asuna Userbot ..」**\n**My Master** : {kek}\n**Date** : {date}")
  await slime.delete()

@asunaub.on(events.NewMessage(outgoing=True, pattern=r'^.ping$'))
async def ping(slime):
  start = dt.now()
  await slime.edit("`Pinging...`")
  end = dt.now()
  pon = (start - end).microseconds / 1000
  await slime.edit(f'''🏓 `PONG!!`
⚡️ `{pon} ms`''')

@asunaub.on(events.NewMessage(outgoing=True , pattern=r"^.shutdown$"))
async def shutdown(slime):
    await slime.edit("`Bot Shutdowned Successfully`")
    await asunaub.disconnect()
    await asuna.disconnect()
