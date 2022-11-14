from Asuna import *
from . import *
from telethon import events, Button , types
from datetime import datetime as dt
from telegraph import upload_file as uf
import time 
import asyncio
import os
from datetime import datetime
from pytz import timezone

HELP_STR="""✘ Commands Available
• `.purge`
    Delete All Message From Replied Message
    
• `.id`
    Get Chat Id
    
• `.dc <filename>`
    Pack Into File
    
• `.open`
    Get Contents of File
 
• `.telegraph`
    Upload Replied File to Telegraph
    
• `.when`
    Shows The Date of Forwarded Message

• `.name`
    Get The Files Name And Size
"""

@asunaub.on(events.NewMessage(outgoing=True , pattern=r"^.purge$"))
async def purge(event):
    reply=await event.get_reply_message()
    from_id=reply.id -1
    if not reply:
        await event.edit(f"`Reply...`")
    try:
        p=0
        async for msg in asunaub.iter_messages(
            event.chat_id,
            min_id=from_id,
        ):
            await msg.delete()
            p+=1
        xx=await asunaub.send_message(event.chat_id,f"`Purged {p} Messages !`")
        time.sleep(5)
        await xx.delete()
    except Exception as e:
        pass

@asunaub.on(events.NewMessage(outgoing=True,pattern=r"^.id$"))
async def id(slime):
    if slime.reply_to_msg_id:
        await slime.get_input_chat()
        r_msg = await slime.get_reply_message()
        await slime.edit(f"**User ID:**  `{r_msg.sender_id}`\n**Current Chat ID:**  `{slime.chat_id}`")
    else:
        await slime.edit("**Current Chat ID:**  `{}`".format(str(slime.chat_id)))
        
@asunaub.on(events.NewMessage(outgoing=True,pattern=r"^.dc (.*)"))
async def pp(event):
    input_str = event.pattern_match.group(1)
    if not input_str:
        await event.edit("`Bsdk Give Name.`")
        await asyncio.sleep(3)
        await event.delete()
    if event.reply:
        a = await event.get_reply_message()
        if not a.message:
            return await event.edit("`Reply to a message..`")
        else:
            b = open(input_str, "w+")
            b.write(str(a.message))
            b.close()
            await event.edit(f"Packing into {input_str}")
            await asunaub.send_file(
                event.chat_id, input_str,caption=str(f"""`{input_str}`""")
            )
            await event.delete()
            os.remove(input_str)
            
@asunaub.on(events.NewMessage(outgoing=True , pattern=r"^.open$"))
async def pp(event):
    if event.reply:
        a = await event.get_reply_message()
        if not a:
            return await event.edit("`Reply to a message...`")
        else:
            dl=await a.download_media()
            nm=a.file.name
            b = open(nm, "r")
            data=b.read()
            b.close()
            await event.edit(f"`{data}`")
            os.remove(nm)
            
@asunaub.on(events.NewMessage(outgoing=True , pattern=r"^.telegraph$"))
async def telegraph(event):
    reply=await event.get_reply_message()
    await event.edit("`Pasting to telegraph...`")
    dl=await reply.download_media()
    tt=uf(dl)
    limk="https://telegra.ph" + tt[0]
    await event.edit(f"`Uploaded To Telegraph` : `{limk}`")
    os.remove(dl.file.name)

@asunaub.on(events.NewMessage(outgoing=True , pattern=r"^.when$"))
async def when(event):
    reply = await event.get_reply_message()
    if reply:
        try:
            result = reply.fwd_from.date
        except Exception:
            result = reply.date
    else:
        result = event.date
    format="%d-%m-%Y %H:%M:%S %Z%z"
    op=result.astimezone(timezone('Asia/Kolkata'))
    go= datetime.now(timezone('Asia/Kolkata'))
    diff=go-op
    diff=str(diff)
    args=diff.split(':')
    hrs=args[0]
    min=args[1]
    second=args[2]
    sec=second.split('.')
    second=sec[0]
    result=op.strftime(format)
    await event.edit(str(f"""`This message was posted on : {result} which is {hrs} hours {min} minutes {second} seconds ago   `"""))
    
@asunaub.on(events.NewMessage(outgoing=True,pattern=r'^.name$'))
async def name(event):
    if not event.reply:
        await event.edit(f'''`Please Reply To A Telegram File`''')
    if event.reply:
        a=await event.get_reply_message()
        if a.file:
            nm=a.file.name
            sz=a.file.size 
            zz=''
            if sz<=1024:
                zz+=str(sz)+' B'
            elif sz>1024 and sz<=1048576:
                zz+=str(round(sz/1024,2))+' KB'
            elif sz>1048576 and sz<=1073741824:
                zz+=str(round(sz/1048576,2))+' MB'
            else:
                zz+=str(round(sz/1073741824,2))+' GB'
 
            await event.edit(f'''**FileName** : `{nm}`
**FileSize** : `{zz}`''')
        else:
            await event.edit(f'''`Reply To A File`''')
    else:
        await event.edit(f'''`File Not Recognized`''')
    
