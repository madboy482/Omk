#### MadBoi
#### MadBoi
#### MadBoi
#### MadBoi

from telethon.errors.rpcerrorlist import YouBlockedUserError
from userbot.utils import admin_cmd
naam = str("Lel")

bot = "@Hexamonbot"

Inventory = ("Here Is Your Hexa Inventory\n➖➖➖➖➖➖➖➖➖➖➖\n\n")

@borg.on(admin_cmd("myinventory$"))
async def _(event):
    if event.fwd_from:
        return
    async with borg.conversation(bot) as conv:
                await conv.send_message("/myinventory")
                audio = await conv.get_response()
                card = audio.text
                a = card.replace(":", "»")
                await borg.send_message(event.chat_id, Inventory + a)

#### MadBoi
#### MadBoi
#### MadBoi
#### MadBoi
