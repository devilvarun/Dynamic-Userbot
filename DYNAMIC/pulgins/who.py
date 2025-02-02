
import html

from telethon import events
from telethon import utils
from telethon.tl import types
from telethon.errors import (BadRequestError, ChatAdminRequiredError,
                             ImageProcessFailedError, PhotoCropSizeSmallError,
                             UserAdminInvalidError)
from DYNAMIC import CMD_HELP


def get_who_string(who):
    who_string = html.escape(utils.get_display_name(who))
    if isinstance(who, (types.User, types.Channel)) and who.username:
        who_string += f" <i>(@{who.username})</i>"
    who_string += f", <a href='tg://user?id={who.id}'>#{who.id}</a>"
    return who_string


@borg.on(events.NewMessage(pattern=r"\.urid", outgoing=True))
async def _(event):
    if not event.message.is_reply:
        who = await event.get_chat()
    else:
        msg = await event.message.get_reply_message()
        if msg.forward:
          	# FIXME forward privacy memes
            who = await borg.get_entity(
                msg.forward.sender_id or msg.forward.channel_id)
        else:
            who = await msg.get_sender()

    await event.edit(get_who_string(who), parse_mode='html')


@borg.on(events.NewMessage(pattern=r"\.members", outgoing=True))
async def _(event):
    members = [
        get_who_string(m) async for m in borg.iter_participants(event.chat_id)
    ]

    await event.edit("\n".join(members), parse_mode='html')
CMD_HELP.update(
    {
        "who": "**Plugin : **`who`\
    \n\n**Syntax : **`.members`\
    \n**Function : **meko khud ni pta khud check krlo 😑"
    }
)

