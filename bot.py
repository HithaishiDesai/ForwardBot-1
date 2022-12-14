import asyncio
from os import environ 
import logging
import logging.config
from pyrogram import Client 

logging.config.fileConfig("logging.conf")
logging.getLogger().setLevel(logging.INFO)
logging.getLogger("pyrogram").setLevel(logging.ERROR)

from info import SESSION, API_ID, API_HASH, BOT_TOKEN 
from pyrogram.raw.all import layer 
from typing import Union, Optional, AsyncGenerator
from pyrogram import types

class Bot(Client):
    
    def __init__(self):
        super().__init__(
            name=SESSION,
            api_id=API_ID, 
            api_hash=API_HASH,
            bot_token=BOT_TOKEN, 
            workers=50,
            plugins={"root": "plugins"},
            sleep_threshold=120,
        ) 
    async def start(self): 
        await super().start()
        me = await self.get_me() 
        self.mention = me.mention 
        self.username = '@' + me.username  
        logging.info(f"{me.first_name} 𝚂𝚃𝙰𝚁𝚃𝙴𝙳 ⚡️⚡️⚡️") 
        
    async def stop(self, *args): 
        await super().stop()
        logging.info("Bot stopped. Bye.")
        
app = Bot()
app.run()
