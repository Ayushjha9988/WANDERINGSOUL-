import asyncio
import heroku3

from config import X1, X2, X3, X4, X5, X6, X7, X8, X9, X10, SUDO_USERS, OWNER_ID, HEROKU_API_KEY, HEROKU_APP_NAME, CMD_HNDLR as hl

from datetime import datetime

from telethon import events
from telethon.errors import ForbiddenError

 
@X1.on(events.NewMessage(incoming=True, pattern=r"\%slogs(?: |$)(.*)" % hl))
@X2.on(events.NewMessage(incoming=True, pattern=r"\%slogs(?: |$)(.*)" % hl))
@X3.on(events.NewMessage(incoming=True, pattern=r"\%slogs(?: |$)(.*)" % hl))
@X4.on(events.NewMessage(incoming=True, pattern=r"\%slogs(?: |$)(.*)" % hl))
@X5.on(events.NewMessage(incoming=True, pattern=r"\%slogs(?: |$)(.*)" % hl))
@X6.on(events.NewMessage(incoming=True, pattern=r"\%slogs(?: |$)(.*)" % hl))
@X7.on(events.NewMessage(incoming=True, pattern=r"\%slogs(?: |$)(.*)" % hl))
@X8.on(events.NewMessage(incoming=True, pattern=r"\%slogs(?: |$)(.*)" % hl))
@X9.on(events.NewMessage(incoming=True, pattern=r"\%slogs(?: |$)(.*)" % hl))
@X10.on(events.NewMessage(incoming=True, pattern=r"\%slogs(?: |$)(.*)" % hl))
async def logs(legend):
    if legend.sender_id == OWNER_ID:
        if (HEROKU_APP_NAME is None) or (HEROKU_API_KEY is None):
            await legend.reply(
                legend.chat_id,
                "𝙵𝙸𝚁𝚂𝚃 𝚂𝙴𝚃 𝚃𝙷𝙴𝚂𝙴 𝚅𝙰𝚁𝚂 :  `HEROKU_API_KEY` And `HEROKU_APP_NAME`.",
            )
            return

        try:
            Heroku = heroku3.from_key(HEROKU_API_KEY)
            app = Heroku.app(HEROKU_APP_NAME)
        except BaseException:
            await legend.reply(
                "𝙼𝙰𝙺𝙴 𝚂𝚄𝚁𝙴 𝚈𝙾𝚄𝚁 𝙷𝙴𝚁𝙾𝙺𝚄 𝙺𝙴𝚈 𝙰𝙽𝙳 𝙰𝙿𝙿 𝙽𝙰𝙼𝙴 𝙰𝚁𝙴 𝙲𝙾𝙽𝙵𝙸𝙶𝙴𝙳 𝙲𝙾𝚁𝚁𝙴𝙲𝚃𝙻𝚈"
            )
            return

        logs = app.get_log()
        start = datetime.now()
        fetch = await legend.reply(f"𝙵𝙴𝚃𝙲𝙷𝙸𝙽𝙶 𝙻𝙾𝙶𝚂 𝙿𝙻𝙴𝙰𝚂𝙴 𝚆𝙰𝙸𝚃 𝙱𝙰𝙱𝚈❤️💋...")
    
        with open("AltLogs.txt", "w") as logfile:
            logfile.write("𝚆𝙰𝙽𝙳𝙴𝚁𝙸𝙽𝙶 𝚇 𝚂𝙿𝙰𝙼𝙱𝙾𝚃 ❤️ [ Bot Logs ]\n\n" + logs)

        end = datetime.now()
        ms = (end-start).seconds
        await asyncio.sleep(1)

        try:
            await X1.send_file(legend.chat_id, "ʟᴏɢꜱ.ᴛxᴛ", caption=f"❤️ **𝚆𝙰𝙽𝙳𝙴𝚁𝙸𝙽𝙶 𝚇 𝚂𝙿𝙰𝙼𝙱𝙾𝚃 𝙱𝙾𝚃 𝙻𝙾𝙶𝚂 ❤️** 🔥\n  » **𝚃𝙸𝙼𝙴 𝚃𝙰𝙺𝙴𝙽  ❤️:** `{ms} 𝘚𝘌𝘊𝘖𝘕𝘋𝘚`")
            await fetch.delete()
        except Exception as e:
            await fetch.edit(f"**𝙴𝚁𝚁𝙾𝚁:** {str(e)}")

    elif legend.sender_id in SUDO_USERS:
        await legend.reply("» 𝙽𝙾𝙿𝙴, 𝙾𝙽𝙻𝚈 𝙾𝚆𝙽𝙴𝚁 𝙲𝙰𝙽 𝙰𝙲𝙲𝙴𝚂𝚂 𝚃𝙷𝙸𝚂 𝙲𝙾𝙼𝙼𝙰𝙽𝙳 💀 ")
