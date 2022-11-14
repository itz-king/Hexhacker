from hexhacker import *
from telethon import events, Button
from datetime import datetime as dt
from hexhacker.env import *

@hexhacker.on(events.NewMessage(outgoing=True, pattern=r'^.ping$'))
async def ping(slime):
  start = dt.now()
  await slime.edit("`Pinging...`")
  end = dt.now()
  pon = (start - end).microseconds / 1000
  await slime.edit(f'''🏓 `PONG!!`
⚡️ `{pon} ms`''')

@hexhacker.on(events.NewMessage(outgoing=True , pattern=r"^.shutdown$"))
async def shutdown(slime):
    await slime.edit("`Bot Shutdowned Successfully`")
    await hexhacker.disconnect()
