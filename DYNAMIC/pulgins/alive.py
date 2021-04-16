"""Check if DYNAMIC alive. If you change these, you become the gayest gay such that even the gay world will disown you."""
import asyncio
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from platform import uname
from DYNAMIC import ALIVE_NAME
from DYNAMIC.utils import admin_cmd

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "**DYNAMIC USERBOT**"

@command(outgoing=True, pattern="^.alive$")
async def amireallyalive(alive):
    """ For .alive command, check if the bot is running.  """
    await alive.edit(" ◆◆️{BOT}◆◆️  IS ON DUTY SIR
                       "••••••SYSTEM STATUS••••••\
                       ●●Telethon∆Version●●: 1.19.5\n
                       ●●DYNAMIC∆Version●●: 0.0.1\n"
                        f"●●【Uptime】●●: {uptm}\n""
                        "●●My∆Master●●: {DEFAULTUSER} (tg://user?id=%7Btag%7D)\n"
                        "●My∆Group●●: SUPPORT (https://t.me/DARKLON_USERBOT_SUPPORT)\n"
                        "●●My∆Channel●●: CHANNEL (https://t.me/DARKLONXOP)\n"
                        "●●OffTopic∆Group●●: OT (https://t.me/DARKLON_OT)n"
                         "Want to Deploy me??? : [𝙳𝙴𝙿𝙻𝙾𝚈 (https://dashboard.heroku.com/new?button-url=https%3A%2F%2Fgithub.com%2FHACKERBOTTELEGRAM%2FDARKLON-PACK&template=https%3A%2F%2Fgithub.com%2FHACKERBOTTELEGRAM%2FDARKLON-PACK) 𝚈𝙾𝚄𝚁 𝙾𝚆𝙽 𝙾𝙿 {BOT} (https://github.com/HACKERBOTTELEGRAM/HACKERBOTOP)  💠\n"   ")
