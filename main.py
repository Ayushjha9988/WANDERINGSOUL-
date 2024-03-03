import sys
import glob
import asyncio
import logging
import importlib
import urllib3
from pathlib import Path
from config import X1, X2, X3, X4, X5, X6, X7, X8, X9, X10


logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s', level=logging.WARNING)

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def load_plugins(plugin_name):
    path = Path(f"Japanese/modules/{plugin_name}.py")
    spec = importlib.util.spec_from_file_location(f"Japanese.modules.{plugin_name}", path)
    load = importlib.util.module_from_spec(spec)
    load.logger = logging.getLogger(plugin_name)
    spec.loader.exec_module(load)
    sys.modules["Japanese.modules." + plugin_name] = load
    print("✥✥ 𝙹𝙰𝙿𝙰𝙽𝙴𝚂𝙴 𝚇 𝚂𝙿𝙰𝙼𝙱𝙾𝚃 𝙷𝙰𝚂 𝙸𝙼𝙿𝙾𝚁𝚃𝙴𝙳 ✥✥" + plugin_name)


files = glob.glob("Japanese/modules/*.py")
for name in files:
    with open(name) as a:
        patt = Path(a.name)
        plugin_name = patt.stem
        load_plugins(plugin_name.replace(".py", ""))

print("\✥✥ 𝙹𝙰𝙿𝙰𝙽𝙴𝚂𝙴 𝚇 𝚂𝙿𝙰𝙼𝙱𝙾𝚃 𝙳𝙴𝙿𝙻𝙾𝚈𝙴𝙳 𝚂𝚄𝙲𝙲𝙴𝚂𝚂𝙵𝚄𝙻𝙻𝚈 ✥✥ ❤️🔥")


async def main():
    await X1.run_until_disconnected()
    await X2.run_until_disconnected()
    await X3.run_until_disconnected()
    await X4.run_until_disconnected()
    await X5.run_until_disconnected()
    await X6.run_until_disconnected()
    await X7.run_until_disconnected()
    await X8.run_until_disconnected()
    await X9.run_until_disconnected()
    await X10.run_until_disconnected()


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
