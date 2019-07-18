# eeborg

Pluggable [``asyncio``](https://docs.python.org/3/library/asyncio.html)
[Telegram](https://telegram.org) UserBot based on
[Telethon](https://github.com/LonamiWebs/Telethon).

## Installing

Simply clone the repository and run the main file:
```sh
git clone https://github.com/eegad/eeborg.git
cd eeborg
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python stdborg.py
```

## Internals

The core features offered by the custom `TelegramClient` live under the
[`eeborg/`](https://github.com/eegad/eeborg/tree/master/eeborg)
directory, with some utilities, enhancements and the core plugin.

## Learning

Check out the already-mentioned
[plugins](https://github.com/eegad/eeborg/tree/master/stdplugins)
directory to learn how to write your own, and consider reading
[Telethon's documentation](http://telethon.readthedocs.io/).
