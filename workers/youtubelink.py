"""

███╗░░░███╗░█████╗░░██████╗████████╗███████╗██████╗░███╗░░░███╗██╗███╗░░██╗██████╗░░░░░░░██╗░░░██╗██████╗░████████╗██╗░░██╗
████╗░████║██╔══██╗██╔════╝╚══██╔══╝██╔════╝██╔══██╗████╗░████║██║████╗░██║██╔══██╗░░░░░░██║░░░██║██╔══██╗╚══██╔══╝╚██╗██╔╝
██╔████╔██║███████║╚█████╗░░░░██║░░░█████╗░░██████╔╝██╔████╔██║██║██╔██╗██║██║░░██║█████╗╚██╗░██╔╝██████╔╝░░░██║░░░░╚███╔╝░
██║╚██╔╝██║██╔══██║░╚═══██╗░░░██║░░░██╔══╝░░██╔══██╗██║╚██╔╝██║██║██║╚████║██║░░██║╚════╝░╚████╔╝░██╔══██╗░░░██║░░░░██╔██╗░
██║░╚═╝░██║██║░░██║██████╔╝░░░██║░░░███████╗██║░░██║██║░╚═╝░██║██║██║░╚███║██████╔╝░░░░░░░░╚██╔╝░░██║░░██║░░░██║░░░██╔╝╚██╗
╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═════╝░░░░╚═╝░░░╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝╚═╝╚═╝░░╚══╝╚═════╝░░░░░░░░░░╚═╝░░░╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░╚═╝

"""

from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["youtubelink"]), group=-2)
async def love(client, message):
    # return
    joinButton = InlineKeyboardMarkup([
        [InlineKeyboardButton("⭕ Dldupdates⭕", url="https://t.me/dldupdates")],
        [InlineKeyboardButton("⭕ WebNetwork ⭕", url="https://t.me/dldupdates")],
        [InlineKeyboardButton("⭕ BotsList ⭕", url="https://t.me/dldupdates")],
        [InlineKeyboardButton("⭕ Leech & Mirror ⭕", url="https://t.me/dldupdates")],
        [InlineKeyboardButton("⭕ Movies & Demand ⭕", url="https://t.me/dldupdates")]
    ])
    youtube_ex = f"""
**Some example youtube channels and songs if you don't know then what u want**
- type /github if I helped u in AnyWay. 
```Pʀᴇᴅ∆ᴛᴏʀ``` """

   
    
    await message.reply_text(youtube_ex, reply_markup=joinButton)
    raise StopPropagation






