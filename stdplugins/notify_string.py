# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from telethon import events

NOTIFY_LIST = {}
COMMAND = '.notify '


@borg.on(events.NewMessage(outgoing=True, pattern=r'^{}(.+)'.format(COMMAND)))
async def trigger_add(event):
    me = await borg.get_me()
    chat = await event.get_chat()
    trigger = event.message.message.replace(COMMAND, '').lower()
    if chat.id in NOTIFY_LIST:
        if trigger in NOTIFY_LIST[chat.id]:
            await borg.send_message(me, f'{trigger}:{chat.id} already in notify list')
        else:
            NOTIFY_LIST[chat.id].append(trigger)
            await borg.send_message(me, f'Added {trigger}:{chat.id} to notify list')
    else:
        NOTIFY_LIST[chat.id] = []
        NOTIFY_LIST[chat.id].append(trigger)
        await borg.send_message(me, f'Added {trigger}:{chat.id} to notify list')

    await borg.delete_messages(chat, event.message.id)


@borg.on(events.NewMessage(incoming=True))
async def trigger_get(event):
    chat = await event.get_chat()
    if chat.id in NOTIFY_LIST:
        for msg in NOTIFY_LIST[chat.id]:
            if msg in event.message.message.lower():
                me = await borg.get_me()
                await borg.forward_messages(me, event.message)
                NOTIFY_LIST[chat.id].remove(msg)
