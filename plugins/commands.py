

import os
from pyrogram import Client,filters 
from telegraph import upload_file



@Client.on_message(filters.command(["start"]))
async def start(client, message):
    await client.send_message(
        chat_id=message.chat.id,
        text=f"𝗛𝗲𝗹𝗹𝗼 {message.from_user.first_name},\n<b>𝗜'𝗺 𝗮 𝗧𝗲𝗹𝗲𝗴𝗿𝗮𝗺 𝗧𝗼 Telegra.ph 𝗜𝗺𝗮𝗴𝗲/𝗩𝗶𝗱𝗲𝗼 𝗨𝗽𝗹𝗼𝗮𝗱𝗲𝗿 𝗕𝗼𝘁. \n 𝗢𝘄𝗻𝗲𝗿 By @HydraLivegrambot</b> \n  Do /help 𝗙𝗼𝗿 𝗺𝗼𝗿𝗲",
        reply_to_message_id=message.message_id
    )

@Client.on_message(filters.command(["help"]))
async def help(client, message):
    await client.send_message(
        chat_id=message.chat.id,
        text=f"<b> 𝗦𝗲𝗻𝗱 𝗠𝗲 𝗔𝗻𝘆 𝗩𝗶𝗱𝗲𝗼 𝗢𝗿 𝗣𝗵𝗼𝘁𝗼 𝗜'𝗹𝗹 𝗨𝗽𝗹𝗼𝗮𝗱 𝗜𝘁 𝗜𝗻𝘁𝗼 Telegra.ph. \n 𝗢𝘄𝗻𝗲𝗿 By @HydraLivegrambot</b>",
        reply_to_message_id=message.message_id
    )
    
@Client.on_message(filters.photo)
async def getimage(client, message):
    location = "./FILES"
    if not os.path.isdir(location):
        os.makedirs(location)
    imgdir = location + "/" + str(message.chat.id) + "/" + str(message.message_id) +".jpg"
    dwn = await client.send_message(
          text="<b>𝗗𝗼𝘄𝗻𝗹𝗼𝗮𝗱𝗶𝗻𝗴...</b>",
          chat_id = message.chat.id,
          reply_to_message_id=message.message_id
          )          
    await client.download_media(
            message=message,
            file_name=imgdir
        )
    await dwn.edit_text("<b>𝗨𝗽𝗹𝗼𝗮𝗱𝗶𝗻𝗴...</b>")
    try:
        response = upload_file(imgdir)
    except Exception as error:
        await dwn.edit_text(f"𝗢𝗼𝗽𝘀 𝗦𝗼𝗺𝗲𝘁𝗵𝗶𝗻𝗴 𝗪𝗲𝗻𝘁 𝗪𝗿𝗼𝗻𝗴\n{error} Contact @HydraLivegrambot")
        return
    await dwn.edit_text(f"https://telegra.ph{response[0]}")
    try:
        os.remove(imgdir)
    except:
        pass

@Client.on_message(filters.video)
async def getvideo(client, message):
    location = "./FILES"
    if not os.path.isdir(location):
        os.makedirs(location)
    viddir = location + "/" + str(message.chat.id) + "/" + str(message.message_id) +".mp4"
    dwn = await client.send_message(
          text="<b>𝗗𝗼𝘄𝗻𝗹𝗼𝗮𝗱𝗶𝗻𝗴...</b>",
          chat_id = message.chat.id,
          reply_to_message_id=message.message_id
          )          
    await client.download_media(
            message=message,
            file_name=viddir
        )
    await dwn.edit_text("<b>𝗨𝗽𝗹𝗼𝗮𝗱𝗶𝗻𝗴...</b>")
    try:
        response = upload_file(viddir)
    except Exception as error:
        await dwn.edit_text(f"𝗢𝗼𝗽𝘀 𝗦𝗼𝗺𝗲𝘁𝗵𝗶𝗻𝗴 𝗪𝗲𝗻𝘁 𝗪𝗿𝗼𝗻𝗴\n{error} Contact @HydraLivegrambot")
        return
    await dwn.edit_text(f"https://telegra.ph{response[0]}")
    try:
        os.remove(viddir)
    except:
        pass

