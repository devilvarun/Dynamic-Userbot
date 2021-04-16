#Make BY Aman Pandey 
#Dont Kang Otherwise You Will Get A Bad Gift
import os
import sys
import time
from telethon.session import StringSession
from telethon import TelegramClient
from var import var
dynamic version = "0.0.1"

os.system("pip install --upgrade pip")
if Var.STRING_SESSION:
    session_name = str(Var.STRING_SESSION)
    bot = TelegramClient(StringSession(session_name), Var.APP_ID, Var.API_HASH)
else:
    session_name = "startup"
    bot = TelegramClient(session_name, Var.APP_ID, Var.API_HASH)

CMD_LIST = {}
# for later purposes
CMD_HELP = {}
INT_PLUG = ""
LOAD_PLUG = {}
