#### MadBoi
#### MadBoi
#### MadBoi
#### MadBoi

from userbot.utils import admin_cmd

naam = str("Lel")

bot = "@Hexamonbot"


@borg.on(admin_cmd("hunt$"))
async def _(event):
    if event.fwd_from:
        return
    async with borg.conversation(bot) as conv:
        await conv.send_message("/hunt")
        audio = await conv.get_response()
        card = audio.text
        a = card.replace("A wild", "")
        b = a.replace("has appeared", "")
        await borg.send_file(event.chat_id, audio, caption=b)


#### MadBoi
#### MadBoi
#### MadBoi
#### MadBoi
