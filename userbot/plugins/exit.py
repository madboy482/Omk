#### MadBoi
#### MadBoi
#### MadBoi
#### MadBoi

from userbot.utils import admin_cmd

naam = str("Lel")

bot = "@Hexamonbot"

Outside = "Exiting the Safari Zone\n➖➖➖➖➖➖➖➖➖➖➖\n\n"


@borg.on(admin_cmd("exit$"))
async def _(event):
    if event.fwd_from:
        return
    async with borg.conversation(bot) as conv:
        await conv.send_message("/exit")
        audio = await conv.get_response()
        card = audio.text
        a = card.replace("safari zone", "SAFARI ZONE")
        await borg.send_message(event.chat_id, Outside + a)


#### MadBoi
#### MadBoi
#### MadBoi
#### MadBoi
