import os
import re
import sys
import json
import time
import asyncio
import requests
import subprocess
from modules import helper
from modules.utils import progress_bar
from modules.vars import api_id, api_hash, bot_token
from aiohttp import ClientSession
from pyromod import listen
from subprocess import getstatusoutput
from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.errors import FloodWait
from pyrogram.errors.exceptions.bad_request_400 import StickerEmojiInvalid
from pyrogram.types.messages_and_media import message
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup


bot = Client(
    "bot",
    api_id=api_id,
    api_hash=api_hash,
    bot_token=bot_token
)


@bot.on_message(filters.command(["start"]))
async def account_login(bot: Client, m: Message):
    await m.reply_text("**✌️ʜᴇʟʟᴏ, ᴍʏ ꜰʀɪᴇɴᴅ🌝.**\n\n**ɪ ᴀᴍ @mradarshr ʙᴏᴛ.**\n**ɪ ᴡɪʟʟ ᴅᴏᴡɴʟᴏᴀᴅ ʏᴏᴜʀ ᴛᴇxᴛ ꜰɪʟᴇ ʟɪɴᴋꜱ.**")


@bot.on_message(filters.command("stop"))
async def restart_handler(_, m: Message):
    await m.reply_text("**Stopped**🚦", True)
    os.execl(sys.executable, sys.executable, *sys.argv)

@bot.on_message(filters.command(["txt"]))
async def account_login(bot: Client, m: Message):
    editable = await m.reply_text('SEND ME TEXT TO CONVERT INTO TXT FILE⚡️')
    input: Message = await bot.listen(editable.chat.id)
    raw_text = input.text
    await input.delete(True)
    
    await editable.edit("Now send the file title")
    input6: Message = await bot.listen(editable.chat.id)
    raw_text0 = input0.text
    await input6.delete(True)
    await editable.delete()

    path = f"./downloads/{m.chat.id}"
    
    file_name = f"{raw_text0}.txt"
    
    with open(file_name, "w") as file:
        file.write(raw_text)
    
    await bot.send_document(chat_id=m.chat.id, document=file_name, caption="TXT File Converted by @mradarshr Bot")
    os.remove(file_name)

@bot.on_message(filters.command(["babu"]))
async def account_login(bot: Client, m: Message):
    editable = await m.reply_text('𝕋𝕆 ᴅᴏᴡɴʟᴏᴀᴅ ᴀ ᴛxᴛ ғɪʟᴇ 𝕤ᴇɴᴅ ʜᴇʀᴇ ⚡️')
    input: Message = await bot.listen(editable.chat.id)
    x = await input.download()
    await input.delete(True)

    path = f"./downloads/{m.chat.id}"

    try:
        with open(x, "r") as f:
            content = f.read().split("\n")
            links = [i.split("://", 1) for i in content]
        os.remove(x)
    except:
        await m.reply_text("**Invalid file input.**")
        os.remove(x)
        return

    await editable.edit(f"**𝕋ᴏᴛᴀʟ ʟɪɴᴋ𝕤 ғᴏᴜɴᴅ ᴀʀᴇ🔗🔗** **{len(links)}**\n\n**𝕊ᴇɴᴅ 𝔽ʀᴏᴍ ᴡʜᴇʀᴇ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ᴅᴏᴡɴʟᴏᴀᴅ ɪɴɪᴛɪᴀʟ ɪ𝕤** **1**")
    input0: Message = await bot.listen(editable.chat.id)
    raw_text = input0.text
    await input0.delete(True)

    await editable.edit("**Now Please Send Me Your Batch Name**")
    input1: Message = await bot.listen(editable.chat.id)
    raw_text0 = input1.text
    await input1.delete(True)

    await editable.edit("**𝔼ɴᴛᴇʀ ʀᴇ𝕤ᴏʟᴜᴛɪᴏɴ📸**\n144,240,360,480,720,1080 please choose quality")
    input2: Message = await bot.listen(editable.chat.id)
    raw_text2 = input2.text
    await input2.delete(True)

    res = {
        "144": "256x144",
        "240": "426x240",
        "360": "640x360",
        "480": "854x480",
        "720": "1280x720",
        "1080": "1920x1080"
    }.get(raw_text2, "UN")

    await editable.edit("Now Enter A Name to mention on Downloaded by")
    input3: Message = await bot.listen(editable.chat.id)
    raw_text3 = input3.text
    await input3.delete(True)

    highlighter = f"️ ⁪⁬⁮⁮⁮"
    MR = highlighter if raw_text3 == 'Robin' else raw_text3

    await editable.edit("Now send the Thumb url for Video\nEg » https://i.ibb.co/yqHF2HK/vedxpw.jpg \n Or if don't want thumbnail send = no")
    input6: Message = await bot.listen(editable.chat.id)
    raw_text6 = input6.text
    await input6.delete(True)
    await editable.delete()

    thumb = raw_text6
    if thumb.startswith("http://") or thumb.startswith("https://"):
        getstatusoutput(f"wget '{thumb}' -O 'thumb.jpg'") 
        thumb = "thumb.jpg"
    else:
        thumb = "no"
    count = int(raw_text) if len(links) > 1 else 1

    for i in range(count - 1, len(links)):
        try:
            V = links[i][1].replace("file/d/", "uc?export=download&id=").replace("www.youtube-nocookie.com/embed", "youtu.be").replace("?modestbranding=1", "").replace("/view?usp=sharing", "")
            url = "https://" + V

            if "visionias" in url:
                async with ClientSession() as session:
                    async with session.get(url, headers={
                        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                        'Accept-Language': 'en-US,en;q=0.9',
                        'Cache-Control': 'no-cache',
                        'Connection': 'keep-alive',
                        'Pragma': 'no-cache',
                        'Referer': 'http://www.visionias.in/',
                        'Sec-Fetch-Dest': 'iframe',
                        'Sec-Fetch-Mode': 'navigate',
                        'Sec-Fetch-Site': 'cross-site',
                        'Upgrade-Insecure-Requests': '1',
                        'User-Agent': 'Mozilla/5.0 (Linux; Android 12; RMX2121) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36',
                        'sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"',
                        'sec-ch-ua-mobile': '?1',
                        'sec-ch-ua-platform': '"Android"',
                    }) as resp:
                        text = await resp.text()
                        url = re.search(r"(https://.*?playlist.m3u8.*?)\"", text).group(1)

            elif 'videos.classplusapp' in url:
                url = requests.get(f'https://api.classplusapp.com/cams/uploader/video/jw-signed-url?url={url}', headers={
                    'x-access-token': 'eyJhbGciOiJIUzM4NCIsInR5cCI6IkpXVCJ9.eyJpZCI6MzgzNjkyMTIsIm9yZ0lkIjoyNjA1LCJ0eXBlIjoxLCJtb2JpbGUiOiI5MTcwODI3NzQyODkiLCJuYW1lIjoiQWNlIiwiZW1haWwiOm51bGwsImlzRmlyc3RMb2dpbiI6dHJ1ZSwiZGVmYXVsdExhbmd1YWdlIjpudWxsLCJjb3VudHJ5Q29kZSI6IklOIiwiaXNJbnRlcm5hdGlvbmFsIjowLCJpYXQiOjE2NDMyODE4NzcsImV4cCI6MTY0Mzg4NjY3N30.hM33P2ai6ivdzxPPfm01LAd4JWv-vnrSxGXqvCirCSpUfhhofpeqyeHPxtstXwe0'
                }).json()['url']

            elif 'cpvod' in url:
                url = requests.get(f'https://api.classplusapp.com/cams/uploader/video/jw-signed-url?url={url}', headers={
                    'x-access-token': 'eyJhbGciOiJIUzM4NCIsInR5cCI6IkpXVCJ9.eyJpZCI6MzgzNjkyMTIsIm9yZ0lkIjoyNjA1LCJ0eXBlIjoxLCJtb2JpbGUiOiI5MTcwODI3NzQyODkiLCJuYW1lIjoiQWNlIiwiZW1haWwiOm51bGwsImlzRmlyc3RMb2dpbiI6dHJ1ZSwiZGVmYXVsdExhbmd1YWdlIjpudWxsLCJjb3VudHJ5Q29kZSI6IklOIiwiaXNJbnRlcm5hdGlvbmFsIjowLCJpYXQiOjE2NDMyODE4NzcsImV4cCI6MTY0Mzg4NjY3N30.hM33P2ai6ivdzxPPfm01LAd4JWv-vnrSxGXqvCirCSpUfhhofpeqyeHPxtstXwe0'
                }).json()['url']
                
            elif 'awebvideos.classplusapp' in url:
                url = requests.get(f'https://api.classplusapp.com/cams/uploader/video/jw-signed-url?url={url}', headers={
                    'x-access-token': 'your-token-here'
                }).json()['url']

            elif '/master.mpd' in url:
                id = url.split("/")[-2]
                url = f"https://pw.pwjarvis.tech?v={id}&quality={raw_text2}"

            elif 'penpencilvod.pc.cdn.bitgravity.com' in url:
                id = url.split("/")[-2]
                url = f"https://pw.pwjarvis.tech?v={id}&quality={raw_text2}"

            name1 = links[i][0].replace("\t", "").replace(":", "").replace("/", "").replace("+", "").replace("#", "").replace("|", "").replace("@", "").replace("*", "").replace(".", "").replace("https", "").replace("http", "").strip()
            name = f'{str(count).zfill(3)}) {name1[:60]}'

            ytf = f"b[height<={raw_text2}][ext=mp4]/bv[height<={raw_text2}][ext=mp4]+ba[ext=m4a]/b[ext=mp4]" if "youtu" in url else f"b[height<={raw_text2}]/bv[height<={raw_text2}]+ba/b/bv+ba"
            cmd = f'yt-dlp -f "{ytf}" "{url}" -o "{name}.mp4"'

            cc = f"**📂 ғɪʟᴇɴᴀᴍᴇ :** {str(count).zfill(3)}) {name1}.mkv\n\n**ʙᴀᴛᴄʜ** » {raw_text0}\n\n**ᴅᴏᴡɴʟᴏᴀᴅᴇᴅ ʙʏ »** {MR}"
            cc1 = f"**📂 ғɪʟᴇɴᴀᴍᴇ :** {str(count).zfill(3)}) {name1}.pdf\n\n**ʙᴀᴛᴄʜ** » {raw_text0}\n\n**ᴅᴏᴡɴʟᴏᴀᴅᴇᴅ ʙʏ »** {MR}"

            if "drive" in url:
                try:
                    ka = await helper.download(url, name)
                    await bot.send_document(chat_id=m.chat.id, document=ka, caption=cc1)
                    count += 1
                    os.remove(ka)
                    time.sleep(1)
                except FloodWait as e:
                    await m.reply_text(str(e))
                    time.sleep(e.x)
                    continue

            elif ".pdf" in url:
                try:
                    cmd = f'yt-dlp -o "{name}.pdf" "{url}"'
                    download_cmd = f"{cmd} -R 25 --fragment-retries 25"
                    os.system(download_cmd)
                    await bot.send_document(chat_id=m.chat.id, document=f'{name}.pdf', caption=cc1)
                    count += 1
                    os.remove(f'{name}.pdf')
                except FloodWait as e:
                    await m.reply_text(str(e))
                    time.sleep(e.x)
                    continue
            else:
                Show = f"**⥥ 🄳🄾🅆🄽🄻🄾🄰🄳🄸🄽🄶⬇️⬇️... »**\n\n**📝Name »** `{name}\n❄Quality » {raw_text2}`\n\n**🔗URL »** @VEDxPW"
                prog = await m.reply_text(Show)
                res_file = await helper.download_video(url, cmd, name)
                filename = res_file
                await prog.delete(True)
                await helper.send_vid(bot, m, cc, filename, thumb, name, prog)
                count += 1
                time.sleep(1)

        except FloodWait as e:
            await m.reply_text(str(e))
            time.sleep(e.x)
            continue
        except Exception as e:
            await m.reply_text(f"**Downloading Interrupted **\n {str(e)}\n**Name** » {name}\n**Link** » `{url}`")
            continue

    await m.reply_text("❚█═ 𝔻𝕆𝕎ℕ𝕃𝕆𝔸𝔻𝕀ℕ𝔾 ℂ𝕆𝕄ℙ𝕃𝔼𝕋𝔼 ═█❚\n▼△▼△▼△ Λᴅᴀʀsʜ ʀᴀᴛʜᴀᴜʀ ▼△▼△▼△")

print("Bot Started Sir")
bot.run()
