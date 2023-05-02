from pyrogram import Client, filters, enums
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup 
from config import ADMIN
 

@Client.on_message(filters.command("start") & filters.private)                             
async def start_cmd(bot, msg):
    txt="ᴛʜɪꜱ ɪꜱ ᴘᴇʀꜱᴏɴᴀʟ ᴜꜱᴇ ʙᴏᴛ 🙏"
    if msg.from_user.id != ADMIN:
        return await msg.reply_text(text=txt, reply_markup=btn, disable_web_page_preview = True)
    await start(bot, msg, cb=False)


@Client.on_callback_query(filters.regex("start"))
async def start(bot, msg, cb=True):   
    txt=f"hai {msg.from_user.mention} ɪ ᴀᴍ ꜱɪᴍᴘʟᴇ ʀᴇɴᴀᴍᴇ ʙᴏᴛ ᴡɪᴛʜ ᴘᴇʀꜱᴏɴᴀʟ ᴜꜱᴀɢᴇ. \nʀᴇᴘʟʏ ᴍᴇꜱꜱᴇɢᴇ ᴡɪᴛʜ /ʀᴇɴᴀᴍᴇ ꜰɪʟᴇɴᴀᴍᴇ+.ᴇxᴛᴇɴᴛɪᴏɴ \n👇👇👇"
    if cb:
        await msg.message.edit(text=txt, reply_markup=InlineKeyboardMarkup(button), disable_web_page_preview = True, parse_mode=enums.ParseMode.HTML)
    else:
        await msg.reply_text(text=txt, reply_markup=InlineKeyboardMarkup(button), disable_web_page_preview = True, parse_mode=enums.ParseMode.HTML)

@Client.on_callback_query(filters.regex("del"))
async def closed(bot, msg):
    try:
        await msg.message.delete()
    except:
        return

