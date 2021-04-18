"""
(((((((((((((((((((((((@DYNAMICX22)))))))))))))))))))))))))))
(((((((((((((((((((((((@DYNAMICX22)))))))))))))))))))))))))))
(((((((((((((((((((((((@DYNAMICX22)))))))))))))))))))))))))))
(((((((((((((((((((((((@DYNAMICX22)))))))))))))))))))))))))))


                  made by @DYNAMICX22
                  credits TEAMDYNAMIC
                  idea by @Alain_Champion 
 ((((((((((((((((((((((((( @DYNAMICX22 AND @PROBOYX)))))))))))))))))))))))))))
"""
from telethon.errors.rpcerrorlist import YouBlockedUserError

from DYNAMIC import CMD_HELP
from DYNAMIC.utils import admin_cmd
from DYNAMICX import MASTER
DYNAMIC = MASTER
PROBOY = "@tgscanrobot"
# MADE BY DYNAMICX22 🔥🔥

@borg.on(admin_cmd("ginfo ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    DYNAMICX = event.pattern_match.group(1)
    if "@" in DYNAMICX:
        async with borg.conversation(PROBOY) as conv:
            try:
                
                await event.edit(f"THIS USER DETAILS CHECKING BY {DYNAMIC}")
                await conv.send_message("/start")
                await conv.get_response() #made by DYNAMICX22
                await conv.send_message(f"{DYNAMICX}")
                TEAMX = await conv.get_response()
                await borg.send_message(event.chat_id, TEAMX.text)
                await event.delete() #made by DYNAMICX22
            except YouBlockedUserError:
                await event.edit("Error: @tgscanrobot unblock and retry!")
    elif DYNAMICX == "":
        OP = await event.get_reply_message()
        PRO = OP.sender.id 
        async with borg.conversation(PROBOY) as conv:
            try: #made by DYNAMICX22 🔥
              #made by DYNAMICX22 
                await event.edit(f"THIS USER DETAILS CHECKING BY {DYNAMIC}")
                await conv.send_message("/start")
                await conv.get_response() #made by DYNAMICX22
                await conv.send_message(f"{PRO}")
                TEAMX = await conv.get_response()
                await borg.send_message(event.chat_id, TEAMX.text)
                await event.delete()
            except YouBlockedUserError: #made by DYNAMICX22
                await event.edit("Error: unblock @tgscanrobot and try again!")
    else:
        async with borg.conversation(PROBOY) as conv:
            try: #made by DYNAMICX22 🔥
                
                await event.edit(f"THIS USER DETAILS CHECKING BY {DYNAMIC}") 
                await conv.send_message("/start")
                await conv.get_response()
                await conv.send_message(f"{PRO}")
                TEAMX = await conv.get_response()
                await borg.send_message(event.chat_id, TEAMX.text)
                await event.delete()
            except YouBlockedUserError:
                await event.edit("Error: unblock  @tgscanrobot `and try again!")
CMD_HELP.update({
    "ginfo ":"type .ginfo <@username> or tag a user type .ginfo 🔥"})
