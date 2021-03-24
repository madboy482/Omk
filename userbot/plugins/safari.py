#### MadBoi
#### MadBoi
#### MadBoi
#### MadBoi

from telethon.errors.rpcerrorlist import YouBlockedUserError
from userbot.utils import admin_cmd
naam = str("Lel")

bot = "@Hexamonbot"

Safari = ("Safari Zone\n➖➖➖➖➖➖➖➖➖➖➖\n\n")

@borg.on(admin_cmd("safari$"))
async def _(event):
    if event.fwd_from:
        return
    async with borg.conversation(bot) as conv:
                await conv.send_message("/safari")
                audio = await conv.get_response()
                card = audio.text
                a = card.replace("/enter", ".enter")
                b = a.replace("/exit", ".exit")
                await borg.send_message(event.chat_id, Safari + b)

#### MadBoi
#### MadBoi
#### MadBoi
#### MadBoi