from telethon import __version__, events, Button
from config import X1, X2, X3, X4, X5, X6, X7, X8, X9, X10

START_OP = [
    [
        Button.url("𝙹𝙰𝙿𝙰𝙽𝙴𝚂𝙴 𝚇 𝚂𝙿𝙰𝙼𝙱𝙾𝚃 🥀", "https://t.me/Nobitaa_xd"),
        Button.url("𝚂𝚄𝙿𝙿𝙾𝚁𝚃 ✨", "https://t.me/Japanese_Userbot_Chat"),
    ],
    [
        Button.url(
            "𝙰𝙳𝙳 𝙼𝙴 𝙸𝙽 𝚈𝙾𝚄𝚁 𝙶𝚁𝙾𝚄𝙿 🧸", "https://t.me/Nobitaa_xd?startgroup=true"
        ),
    ],
    [
        Button.url("𝚂𝙾𝚄𝚁𝙲𝙴 𝙲𝙾𝙳𝙴 ❄️", "https://github.com/Japanese-Userbots/Japanese-X-Spambot"),
        Button.url("𝙲𝙷𝙰𝙽𝙽𝙴𝙻 ☁️", "https://t.me/Japanese_Userbot"),
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
        TEXT = f"**ʜᴇʏ ✨{event.sender.first_name}❤️\n\n\nɪ ᴀᴍ [{bot_name}](tg://user?id={bot_id})**\n"
        TEXT += f"══════════════════\n"
        TEXT += f"» **ᴅᴇᴠ ❤️: [𝙽𝙾𝙱𝙸𝚃𝙰_𝚇𝙳](https://t.me/Nobitaa_xd)**\n"
        TEXT += f"» **𝙹𝙰𝙿𝙰𝙽𝙴𝚂𝙴 𝚇 𝚂𝙿𝙰𝙼𝙱𝙾𝚃 ✨:** `1.0` \n"
        TEXT += f"» **𝙿𝚈𝚃𝙷𝙾𝙽 𝚅𝙴𝚁𝚂𝙸𝙾𝙽 🔥:** `3.11` \n"
        TEXT += f"» **𝚃𝙴𝙻𝙴𝚃𝙷𝙾𝙽 ❤️:** `{__version__}`\n══════════════════"
        await event.client.send_file(
            event.chat_id,
            "https://graph.org/file/7c16394971d6205bc4902.jpg",
            caption=TEXT,
            buttons=START_OP
        )
