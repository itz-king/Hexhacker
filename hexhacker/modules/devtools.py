from hexhacker import *
from . import *
from telethon import events, Button , types
import asyncio
import io
import os
import sys
import traceback


@hexhacker.on(events.NewMessage(outgoing=True , pattern=".eval ?(.*)"))
async def eval(event):
  cmd = "".join(event.message.message.split(maxsplit=1)[1:])
  if not cmd:
    await event.edit("`What should i run ?..`")
  catevent = await event.edit("`Running ...`")
  old_stderr = sys.stderr
  old_stdout = sys.stdout
  redirected_output = sys.stdout = io.StringIO()
  redirected_error = sys.stderr = io.StringIO()
  stdout, stderr, exc = None, None, None
  try:
      await aexec(cmd, event)
  except Exception:
      exc = traceback.format_exc()
  stdout = redirected_output.getvalue()
  stderr = redirected_error.getvalue()
  sys.stdout = old_stdout
  sys.stderr = old_stderr
  evaluation = ""
  if exc:
      evaluation = exc
  elif stderr:
      evaluation = stderr
  elif stdout:
      evaluation = stdout
  else:
      evaluation = "Success"
  final_output = (
        f"**•  Eval : **\n```{cmd}``` \n\n**•  Result : **\n```{evaluation}``` \n"
    )
  await event.edit(final_output)
  
async def aexec(code, smessatatus):
    message = event = smessatatus
    p = lambda _x: print(_format.yaml_format(_x))
    reply = await event.get_reply_message()
    exec(
        (
            "async def __aexec(message, event , reply, client, p, chat): "
            + "".join(f"\n {l}" for l in code.split("\n"))
        )
    )

    return await locals()["__aexec"](
        message, event, reply, message.client, p, message.chat_id
    )
