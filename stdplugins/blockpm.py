# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from telethon import events, functions

WARN_CHATS = {}
WHITE_CHATS = []
MAX_WARNS = 2


@borg.on(events.NewMessage(incoming=True))
async def _(event):
    if event.is_private and not (await event.get_sender()).bot and event.message.from_id not in WHITE_CHATS:
        if event.message.from_id:
            if event.message.from_id in WARN_CHATS:
                if WARN_CHATS[event.message.from_id] == MAX_WARNS:
                    sender = await event.get_sender()
                    await borg(functions.contacts.BlockRequest(sender))
                    del WARN_CHATS[event.message.from_id]
                    me = await borg.get_me()
                    if sender.last_name:
                        l_name = sender.last_name
                    else:
                        l_name = ""
                    await borg.send_message(me, "{} blocked!".format(sender.first_name + " " + l_name))
                else:
                    WARN_CHATS[event.message.from_id] = WARN_CHATS[event.message.from_id] + 1
                    await borg.send_message(event.message.from_id, """
                        Do not message! You have been warned! ({})
                        ~This is an automated message~""".format(WARN_CHATS[event.message.from_id]))
            else:
                if event.message.from_id not in WARN_CHATS:
                    warns_now = 0
                else:
                    warns_now = WARN_CHATS[event.message.from_id]
                await borg.send_message(event.message.from_id, """
                    You can send {} more messages! You have been warned!
                    ~This is an automated message~""".format(MAX_WARNS - warns_now))
                WARN_CHATS[event.message.from_id] = 1


@borg.on(events.NewMessage(outgoing=True))
async def _(event):
    user_id = event.message.to_id.user_id
    if event.is_private and user_id in WARN_CHATS:
        if user_id not in WHITE_CHATS:
            WHITE_CHATS.append(event.message.to_id.user_id)
            if event.message.to_id.user_id in WARN_CHATS:
                del WARN_CHATS[event.message.from_id]
            await borg.send_message(event.message.to_id.user_id, "Free to PM!")
        else:
            pass
