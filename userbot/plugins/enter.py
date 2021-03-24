#### MadBoi
#### MadBoi
#### MadBoi
#### MadBoi

from telethon.errors.rpcerrorlist import YouBlockedUserError
from userbot.utils import admin_cmd
naam = str("Lel")

bot = "@Hexamonbot"

Inside = ("Enter to Safari Zone\n➖➖➖➖➖➖➖➖➖➖➖\n\n")

@borg.on(admin_cmd("enter$"))
async def _(event):
    if event.fwd_from:
        return
    async with borg.conversation(bot) as conv:
                await conv.send_message("/enter")
                audio = await conv.get_response()
                card = audio.text
                a = card.replace(":", "»")
                await borg.send_message(event.chat_id, Inside + a)

#### MadBoi
#### MadBoi
#### MadBoi
#### MadBoi