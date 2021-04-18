# COPYRIGHT (C) 2021-2022 © BY DYNAMICX22 AND PROBOYX 🔥
"""
(((((((((((((((((((((((@DYNAMICX22)))))))))))))))))))))))))))
(((((((((((((((((((((((@DYNAMICX22)))))))))))))))))))))))))))
(((((((((((((((((((((((@DYNAMICX22)))))))))))))))))))))))))))
(((((((((((((((((((((((@DYNAMICX22)))))))))))))))))))))))))))
               MADE BY DYNAMICX22 AND PROBOYX
                 CREDITS TEAMDYNAMIC
               DONT REMOVE THIS LINES
"""
from DYNAMIC.utils import admin_cmd
from DYNAMICX import xbot, NAME
from telethon import Button
@borg.on(admin_cmd(pattern="button (.*)"))
async def Buttons(event):
  await event.edit("making your button")
  DYNAMICX = Var.TG_BOT_USER_NAME_BF_HER
  pro = event.text[7:]
  pro, boy = pro.split("|")
  if "DYNAMICX" == "PROBOYX":
    await xbot.send_message(event.chat_id, "buttons")
  else:
    try:
      async with bot.conversation(DYNAMICX) as proboyx:
        await proboyx.send_message("/start")
        await proboyx.get_response()
        await proboyx.send_message("my button 🥺")
        await xbot.send_message(bot.me.id, f"{NAME}", buttons=[[Button.url(f"{pro}", f"{boy}")]])
        pro = await proboyx.get_response()
        await pro.forward_to(event.chat_id)
        await event.delete()
    except:
        await event.edit("example:\n.button b<button name>|<link>\n`.button DYNAMICX|https://t.me/DYNAMICX22`\nmake sure your name and link no have Useless spece ", link_preview=False)
