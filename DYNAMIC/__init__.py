#Make BY Aman Pandey 
#Dont Kang Otherwise You Will Get A Bad Gift
import os
import sys
import time
from telethon.sessions import StringSession
from telethon import TelegramClient
from userbot.helpers import functions as simpdef
from userbot.uniborgConfig import Config
from var import Var

StartTime = time.time()
DYNAMICversion = "0.0.1"


DYNAMIC_ID = ["1694874284", "882370987"]

CONSOLE_LOGGER_VERBOSE = sb(os.environ.get("CONSOLE_LOGGER_VERBOSE", "False"))

if CONSOLE_LOGGER_VERBOSE:
    basicConfig(
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        level=DEBUG,
    )
else:
    basicConfig(
        format="[%(asctime)s]- %(name)s- %(levelname)s- %(message)s",
        level=INFO,
        datefmt="%m-%d %H:%M:%S",
    )
LOGS = getlogger(__name__)


try:
    if Config.HEROKU_API_KEY is not None or Config.HEROKU_APP_NAME is not None:
        HEROKU_APP = heroku3.from_key(Config.HEROKU_API_KEY).apps()[
            Config.HEROKU_APP_NAME
        ]
    else:
        HEROKU_APP = None
except Exception:
    HEROKU_APP = None

# Global Configiables
COUNT_MSG = 0
USERS = {}
COUNT_PM = {}
LASTMSG = {}
CMD_HELP = {}
ISAFK = False
AFKREASON = None
CMD_LIST = {}
SUDO_LIST = {}
# for later purposes
INT_PLUG = ""
LOAD_PLUG = {}

if Var.STRING_SESSION:
    session_name = str(Config.STRING_SESSION)
    try:
        if session_name.endswith("="):
            bot = TelegramClient(
                StringSession(session_name), Config.APP_ID, Config.API_HASH
            )
        else:
            bot = TelegramClient(
                "TG_BOT_TOKEN", api_id=Config.APP_ID, api_hash=Config.API_HASH
            ).start(bot_token=Config.STRING_SESSION)
    except Exception as e:
        LOGS.warn(f"STRING_SESSION - {str(e)}")
        sys.exit()
else:
    session_name = "startup"
    bot = TelegramClient(session_name, Config.APP_ID, Config.API_HASH)
