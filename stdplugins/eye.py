"""Emoji

Available Commands:

.emoji shrug

.emoji apple

.emoji :/

.emoji -_-"""

from telethon import events

import asyncio





@borg.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 3

    animation_ttl = range(0, 102)

    input_str = event.pattern_match.group(1)

    if input_str == "eye":

        await event.edit(input_str)

        animation_chars = [

            "👁👁\n  👄  =====> Aye Ja Na Gandu",
            "👁👁\n  👅  =====> Aye Ja Na Madarchod",    
            "👁👁\n  💋  =====> Aye Ja Na Randi",
            "👁👁\n  👄  =====> Aye Ja Na Betichod",
            "👁👁\n  👅  =====> Aye Ja Na Behenchod",    
            "👁👁\n  💋  =====> Aye Ja Na Na Mard",
            "👁👁\n  👄  =====> Aye Ja Na Randi",
            "👁👁\n  👅  =====> Aye Ja Na Bhosdk",    
            "👁👁\n  💋  =====> Aye Ja Na Chutiye"
        ]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 102])
