from telethon import __version__, events, Button
from config import X1, X2, X3, X4, X5, X6, X7, X8, X9, X10

START_OP = [
    [
        Button.url("Jᴀᴘᴀɴᴇsᴇ 🥀", "https://t.me/Nobitaa_xd"),
        Button.url("ꜱᴜᴘᴘᴏʀᴛ ✨", "https://t.me/Japanese_Userbot_Chat"),
    ],
    [
        Button.url(
            "ᴀᴅᴅ ᴍᴇ ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ 🧸", "https://t.me/Nobitaa_xd?startgroup=true"
        ),
    ],
    [
        Button.url("ꜱᴏᴜʀᴄᴇ ᴄᴏᴅᴇ ❄️", "https://t.me/Nobitaa_xd"),
        Button.url("ᴄʜᴀɴɴᴇʟ ☁️", "https://t.me/Japanese_Userbot"),
    ],
]

@X1.on(events.NewMessage(pattern="/start"))
@X2.on(events.NewMessage(pattern="/start"))
@X3.on(events.NewMessage(pattern="/start"))
@X4.on(events.NewMessage(pattern="/start"))
@X5.on(events.NewMessage(pattern="/start"))
@X6.on(events.NewMessage(pattern="/start"))
@X7.on(events.NewMessage(pattern="/start"))
@X7.on(events.NewMessage(pattern="/start"))
@X8.on(events.NewMessage(pattern="/start"))
@X9.on(events.NewMessage(pattern="/start"))
@X10.on(events.NewMessage(pattern="/start"))
async def start(event):
    if event.is_private:
        AltBot = await event.client.get_me()
        bot_name = AltBot.first_name
        bot_id = AltBot.id
        TEXT = f"**ʜᴇʏ 🥀{event.sender.first_name}❤️\n\n\nɪ ᴀᴍ [{bot_name}](tg://user?id={bot_id})**\n"
        TEXT += f"══════════════════\n"
        TEXT += f"» **ᴅᴇᴠ 🫂: [Nᴏʙɪᴛᴀ Xᴅ](https://t.me/Nobitaa_xd)**\n"
        TEXT += f"» **Jᴀᴘᴀɴᴇsᴇ ⚙️:** `1.0` \n"
        TEXT += f"» **ᴘʏᴛʜᴏɴ 🐍:** `3.11` \n"
        TEXT += f"» **ᴛᴇʟᴇᴛʜᴏɴ 🔰:** `{__version__}`\n══════════════════"
        await event.client.send_file(
            event.chat_id,
            "https://graph.org/file/7c16394971d6205bc4902.jpg",
            caption=TEXT,
            buttons=START_OP
        )