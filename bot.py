from pyrogram import Client
from config import *
import os

class Bot(Client):
    if not os.path.isdir(DOWNLOAD_LOCATION):
        os.makedirs(DOWNLOAD_LOCATION)

    def __init__(self):
        super().__init__(
            name="simple-renamer",
            api_id=API_ID,
            api_hash=API_HASH,
            bot_token=BOT_TOKEN,
            workers=100,
            plugins={"root": "main"},
            sleep_threshold=10,
        )
    async def start(self):
        await super().start()
        me = await self.get_me()      
        print(f"{me.first_name} | @{me.username} 🔥🔥ʙᴏᴛ ꜱᴛᴀʀᴛᴇᴅ🔥🔥")
       
    async def stop(self, *args):
       await super().stop()      
       print("ʙᴏᴛ ʀᴇꜱᴛᴀʀᴛɪɴɢ..♻️")


bot = Bot()
bot.run()
