# eeborg

Pluggable [``asyncio``](https://docs.python.org/3/library/asyncio.html)
[Telegram](https://telegram.org) UserBot based on
[Telethon](https://github.com/LonamiWebs/Telethon).

## installing

Simply clone the repository and run the main file:
```sh
git clone https://github.com/eegad/eeborg.git
cd eeborg
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python stdborg.py
```

## design

The modular design of the project enhances your Telegram experience
through [plugins](https://github.com/eegad/eeborg/tree/master/stdplugins)
which you can enable or disable on demand.

Each plugin gets the `borg`, `logger` and `storage` magical variables
to ease their use. Thus creating a plugin as easy as adding
a new file under the plugin directory to do the job:

```python
# stdplugins/myplugin.py
from telethon import events

@borg.on(events.NewMessage(pattern='hi'))
async def handler(event):
    await event.reply('hey')
```

## internals

The core features offered by the custom `TelegramClient` live under the
[`eeborg/`](https://github.com/eegad/eeborg/tree/master/eeborg)
directory, with some utilities, enhancements and the core plugin.

## learning

Check out the already-mentioned
[plugins](https://github.com/eegad/eeborg/tree/master/stdplugins)
directory to learn how to write your own, and consider reading
[Telethon's documentation](http://telethon.readthedocs.io/).
