#### MadBoi
#### MadBoi
#### MadBoi
#### MadBoi

from telethon.errors.rpcerrorlist import YouBlockedUserError
from userbot.utils import admin_cmd
naam = str("Lel")

bot = "@Hexamonbot"

Team = ("Here Is Your Current Active Team\n➖➖➖➖➖➖➖➖➖➖➖\n\n")

@borg.on(admin_cmd("myteam$"))
async def _(event):
    if event.fwd_from:
        return
    async with borg.conversation(bot) as conv:
                await conv.send_message("/myteam")
                audio = await conv.get_response()
                card = audio.text
                a = card.replace("-", "»")
                await borg.send_message(event.chat_id, Team + a)
                

#### MadBoi
#### MadBoi
#### MadBoi
#### MadBoi