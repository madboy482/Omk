#### MadBoi
#### MadBoi
#### MadBoi
#### MadBoi

from userbot.utils import admin_cmd

naam = str("Lel")

bot = "@Hexamonbot"

Store = "Here is the PokeStore\n➖➖➖➖➖➖➖➖➖➖➖\n➖➖➖➖➖➖➖➖➖➖➖\n\n"


@borg.on(admin_cmd("pokestore$"))
async def _(event):
    if event.fwd_from:
        return
    async with borg.conversation(bot) as conv:
        await conv.send_message("/pokestore")
        audio = await conv.get_response()
        card = audio.text
        a = card.replace("-", "»")
        await borg.send_message(event.chat_id, Store + a)


#### MadBoi
#### MadBoi
#### MadBoi
#### MadBoi
