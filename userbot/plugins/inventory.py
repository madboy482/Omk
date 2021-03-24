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
                a = card.replace("Master Balls: 1", "")
                b = a.replace("Master Balls: 2", "")
                c = b.replace("Master Balls: 3", "")
                d = c.replace("Master Balls: 4", "")
                e = d.replace("Master Balls: 5", "")
                f = e.replace("Master Balls: 6", "")
                g = f.replace("Master Balls: 7", "")
                h = g.replace("Master Balls: 8", "")
                i = h.replace("Master Balls: 9", "")
                j = i.replace("Master Balls: 10", "")
                await borg.send_message(event.chat_id, Inventory + j)

#### MadBoi
#### MadBoi
#### MadBoi
#### MadBoi