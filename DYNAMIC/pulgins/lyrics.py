"""
command: .lyrics singer name - song name 
by @quiec
"""
from telethon import events
from uniborg.util import admin_cmd
import asyncio
from PyLyrics import *

@borg.on(admin_cmd(pattern="lyrics (.*)"))
async def _(event):
    if event.fwd_from:
        return
    i = 0

    input_str = event.pattern_match.group(1)
    
    try:
        song = input_str.split("-")
        if len(song) == 1:
            await event.edit("Usage: .lyrics Duman - Haberin Yok 脰l眉yorum")
        else:
            await event.edit("馃攳锔嶴earching lyrics By LEGENDBOT")
            lyrics = PyLyrics.getLyrics(song[0].strip(), song[1].strip()).split("\n")
            lyric_message = f"Singing {song[0].strip()} from {song[1].strip()} 馃帣"
            lyric_message += "\n\n" + "\n".join(lyrics)
            try:
                await event.edit(lyric_message)
            except:
                # TODO: send as file
                logger.info(lyric_message)
    except ValueError:
        await event.edit("Song not found")

