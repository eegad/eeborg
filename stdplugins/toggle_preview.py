"""
Reply to a message with .p to toggle the webpage preview of a message
"""
from telethon.errors import MessageNotModifiedError, MessageIdInvalidError
from eeborg import util
from telethon.tl.functions.messages import EditMessageRequest

# from stdplugins.kbass_core import self_reply_cmd
async def get_target_message(borg, event):
    """
    If the event is a reply, returns the reply message if it's from us
    If event is not a reply, then it tries to return the most recent message
    from us
    """
    target = await event.get_reply_message()
    if event.is_reply and target.from_id == borg.uid:
        return target
    if not target:
        return await util.get_recent_self_message(borg, event)

def self_reply_cmd(borg, pattern):
    def wrapper(function):
        @borg.on(util.admin_cmd(pattern))
        async def wrapped(event, *args, **kwargs):
            await event.delete()
            target = await get_target_message(borg, event)
            if not target:
                return
            return await function(event, target, *args, **kwargs)
        return wrapped
    return wrapper


@self_reply_cmd(borg, r"^\.p$")
async def on_edit_preview(event, target):
    try:
        await borg(EditMessageRequest(
            peer=await event.get_input_chat(),
            id=target.id,
            no_webpage=bool(target.media),
            message=target.message,
            entities=target.entities
        ))
    except (MessageNotModifiedError, MessageIdInvalidError):
        # There was no preview to modify
        pass
