#### MadBoi
#### MadBoi
#### MadBoi
#### MadBoi

from telethon.errors.rpcerrorlist import YouBlockedUserError
from userbot.utils import admin_cmd
naam = str("Lel")

bot = "@Hexamonbot"

Stats = "➖➖➖➖➖➖➖➖➖➖➖\nHere is your Player Stats"

@borg.on(admin_cmd("mystats$"))
async def _(event):
    if event.fwd_from:
        return
    async with borg.conversation(bot) as conv:
                await conv.send_message("/mystats")
                audio = await conv.get_response()
                card = audio.text
                await borg.send_file(event.chat_id, audio, caption=Stats)
                
#### MadBoi
#### MadBoi
#### MadBoi
#### MadBoi