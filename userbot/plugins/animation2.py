import asyncio
from collections import deque


@bot.on(admin_cmd(pattern="think$", outgoing=True))
@bot.on(sudo_cmd(pattern="think$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    event = await edit_or_reply(event, "think")
    deq = deque(list("đ¤đ§đ¤đ§đ¤đ§"))
    for _ in range(48):
        await asyncio.sleep(0.1)
        await event.edit("".join(deq))
        deq.rotate(1)


@bot.on(admin_cmd(pattern=r"lmao$"))
@bot.on(sudo_cmd(pattern="lmao$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    event = await edit_or_reply(event, "lmao")
    deq = deque(list("đđ¤Ŗđđ¤Ŗđđ¤Ŗ"))
    for _ in range(48):
        await asyncio.sleep(0.1)
        await event.edit("".join(deq))
        deq.rotate(1)


@bot.on(admin_cmd(pattern=r"nothappy$"))
@bot.on(sudo_cmd(pattern="nothappy$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    event = await edit_or_reply(event, "nathappy")
    deq = deque(list("đâšī¸đâšī¸đâšī¸đ"))
    for _ in range(48):
        await asyncio.sleep(0.4)
        await event.edit("".join(deq))
        deq.rotate(1)


@bot.on(admin_cmd(outgoing=True, pattern="clock$"))
@bot.on(sudo_cmd(pattern="clock$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    event = await edit_or_reply(event, "clock")
    deq = deque(list("đđđđđđđđđđđ"))
    for _ in range(48):
        await asyncio.sleep(0.1)
        await event.edit("".join(deq))
        deq.rotate(1)


@bot.on(admin_cmd(pattern=r"muah$"))
@bot.on(sudo_cmd(pattern="muah$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    event = await edit_or_reply(event, "muah")
    deq = deque(list("đđđđđ"))
    for _ in range(48):
        await asyncio.sleep(0.1)
        await event.edit("".join(deq))
        deq.rotate(1)


@bot.on(admin_cmd(pattern="heart$"))
@bot.on(sudo_cmd(pattern="heart$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    event = await edit_or_reply(event, "heart")
    deq = deque(list("â¤ī¸đ§Ąđđđđđ¤"))
    for _ in range(48):
        await asyncio.sleep(0.1)
        await event.edit("".join(deq))
        deq.rotate(1)


@bot.on(admin_cmd(pattern="gym$", outgoing=True))
@bot.on(sudo_cmd(pattern="gym$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    event = await edit_or_reply(event, "gym")
    deq = deque(list("đâđâđ¤¸âđâđâđ¤¸âđâđâđ¤¸â"))
    for _ in range(48):
        await asyncio.sleep(0.1)
        await event.edit("".join(deq))
        deq.rotate(1)


@bot.on(admin_cmd(pattern=f"earth$", outgoing=True))
@bot.on(sudo_cmd(pattern="earth$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    event = await edit_or_reply(event, "earth")
    deq = deque(list("đđđđđđđđ"))
    for _ in range(48):
        await asyncio.sleep(0.1)
        await event.edit("".join(deq))
        deq.rotate(1)


@bot.on(admin_cmd(outgoing=True, pattern="moon$"))
@bot.on(sudo_cmd(pattern="moon$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    event = await edit_or_reply(event, "moon")
    deq = deque(list("đđđđđđđđ"))
    for _ in range(48):
        await asyncio.sleep(0.1)
        await event.edit("".join(deq))
        deq.rotate(1)


@bot.on(admin_cmd(pattern=f"smoon$", outgoing=True))
@bot.on(sudo_cmd(pattern="smoon$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    event = await edit_or_reply(event, "smoon")
    animation_interval = 0.1
    animation_ttl = range(101)
    await event.edit("smoon..")
    animation_chars = [
        "đđđđđ\nđđđđđ\nđđđđđ\nđđđđđ\nđđđđđ",
        "đđđđđ\nđđđđđ\nđđđđđ\nđđđđđ\nđđđđđ",
        "đđđđđ\nđđđđđ\nđđđđđ\nđđđđđ\nđđđđđ",
        "đđđđđ\nđđđđđ\nđđđđđ\nđđđđđ\nđđđđđ",
        "đđđđđ\nđđđđđ\nđđđđđ\nđđđđđ\nđđđđđ",
        "đđđđđ\nđđđđđ\nđđđđđ\nđđđđđ\nđđđđđ",
        "đđđđđ\nđđđđđ\nđđđđđ\nđđđđđ\nđđđđđ",
        "đđđđđ\nđđđđđ\nđđđđđ\nđđđđđ\nđđđđđ",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 8])


@bot.on(admin_cmd(pattern=f"tmoon$", outgoing=True))
@bot.on(sudo_cmd(pattern="tmoon$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    event = await edit_or_reply(event, "tmoon")
    animation_interval = 0.1
    animation_ttl = range(96)
    await event.edit("tmoon..")
    animation_chars = [
        "đ",
        "đ",
        "đ",
        "đ",
        "đ",
        "đ",
        "đ",
        "đ",
        "đ",
        "đ",
        "đ",
        "đ",
        "đ",
        "đ",
        "đ",
        "đ",
        "đ",
        "đ",
        "đ",
        "đ",
        "đ",
        "đ",
        "đ",
        "đ",
        "đ",
        "đ",
        "đ",
        "đ",
        "đ",
        "đ",
        "đ",
        "đ",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 32])


CMD_HELP.update(
    {
        "animation2": "__**PLUGIN NAME :** Animation2__\
\n\n**đ CMD âĨ** `.think` | `.lmao` | `.nothappy` | `.clock` | `.muah` | `.heart` | `.gym` | `.earth` | `.moon` | `.smoon` | `.tmoon` \
\n\n**USAGE   âĨ  **These are animation bruh..Try & check yourself\
"
    }
)
