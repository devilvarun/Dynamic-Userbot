"""Check if userbot alive. If you change these, you become the gayest gay such that even the gay world will disown you."""
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
    await alive.edit("`BOT IS WORKING FINE!` **ψ(｀∇´)ψ**\n\n"
                     "`Telethon version: 6.9.0\nPython: 3.7.3\n`"
                     "`BOT VERSION : 0.0.1\nPython: 3.9.8\n`"
                    # MAke By AMAN PANDEY
                     "`Bot created by:` [AMAN PANDEY](tg://user?id=1503668700), @AmanPandeyDeveloperIN\n"
                     f"`My  owner`: {DEFAULTUSER}\n\n"
                     "https://github.com/DynamicUserbot/Dynamic-Userbot/")
