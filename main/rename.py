import time, os
from pyrogram import Client, filters, enums
from config import DOWNLOAD_LOCATION, CAPTION, ADMIN, SUDO_USERS
from main.utils import progress_message, humanbytes

@Client.on_message(filters.private & filters.command("rename") & filters.user(SUDO_USERS))             
async def rename_file(bot, msg):
    reply = msg.reply_to_message
    if len(msg.command) < 2 or not reply:
       return await msg.reply_text("ᴘʟᴇᴀꜱᴇ ʀᴇᴘʟʏ ᴛᴏ ᴀɴ ꜰɪʟᴇ ᴏʀ ᴠɪᴅᴇᴏ ᴏʀ ᴀᴜᴅɪᴏ ᴡɪᴛʜ ꜰɪʟᴇɴᴀᴍᴇ + .ᴇxᴛᴇɴꜱɪᴏɴ ᴇɢ:-(`.ᴍᴋᴠ` ᴏʀ `.ᴍᴘ4` ᴏʀ `.ᴢɪᴘ`)")
    media = reply.document or reply.audio or reply.video
    if not media:
       await msg.reply_text("ᴘʟᴇᴀꜱᴇ ʀᴇᴘʟʏ ᴛᴏ ᴀɴ ꜰɪʟᴇ ᴏʀ ᴠɪᴅᴇᴏ ᴏʀ ᴀᴜᴅɪᴏ ᴡɪᴛʜ ꜰɪʟᴇɴᴀᴍᴇ + .ᴇxᴛᴇɴꜱɪᴏɴ ᴇɢ:-(`.ᴍᴋᴠ` ᴏʀ `.ᴍᴘ4` ᴏʀ `.ᴢɪᴘ`)")
    og_media = getattr(reply, reply.media.value)
    new_name = msg.text.split(" ", 1)[1]
    sts = await msg.reply_text("𝓼𝓽𝓪𝓻𝓽 𝘿𝙤𝙬𝙣𝙡𝙤𝙖𝙙......")
    c_time = time.time()
    downloaded = await reply.download(file_name=new_name, progress=progress_message, progress_args=("..𝘿𝙤𝙬𝙣𝙡𝙤𝙖𝙙𝙞𝙣𝙜🪂🪂🪂", sts, c_time)) 
    filesize = humanbytes(og_media.file_size)                
    if CAPTION:
        try:
            cap = CAPTION.format(file_name=new_name, file_size=filesize)
        except Exception as e:            
            return await sts.edit(text=f"ʏᴏᴜʀ ᴄᴀᴘᴛɪᴏɴ ᴇʀʀᴏʀ ᴜɴᴇxᴘᴇᴄᴛᴇᴅ ᴋᴇʏᴡᴏʀᴅ ●> ({e})")           
    else:
        cap = f"{new_name}\n\n💽 size : {filesize} @PilotsGalaxy"

    # this idea's back end is MrMKN brain 🧠

    dir = os.listdir(DOWNLOAD_LOCATION)
    if len(dir) == 0:
        file_thumb = await bot.download_media(og_media.thumbs[0].file_id)
        og_thumbnail = file_thumb
    else:
        try:
            og_thumbnail = f"{DOWNLOAD_LOCATION}/thumbnail.jpg"
        except Exception as e:
            print(e)        
            og_thumbnail = None
        
    await sts.edit("𝓼𝓽𝓪𝓻𝓽 𝙐𝙥𝙡𝙤𝙖𝙙.....")
    c_time = time.time()
    try:
        await bot.send_document(msg.chat.id, document=downloaded, thumb=og_thumbnail, caption=cap, progress=progress_message, progress_args=("𝙐𝙥𝙡𝙤𝙖𝙙𝙞𝙣𝙜🚀🚀🚀", sts, c_time))        
    except Exception as e:  
        return await sts.edit(f"Error {e}")                       
    try:
        if file_thumb:
            os.remove(file_thumb)
        os.remove(downloaded)      
    except:
        pass
    await sts.delete()

