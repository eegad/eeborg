## Design

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