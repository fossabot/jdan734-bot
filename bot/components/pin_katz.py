from .token import bot

@bot.message_handler(content_types=['text'])
def pin_kaz(message):
    if message.forward_from_chat is not None:
        if message.forward_from_chat.username == "maximkatz":
            pass
        else:
            return
    else:
        return

    if isinstance(message.text, str):
        return

    do_pin = False

    for entity in message.text:
        if isinstance(entity, str):
            continue

        if "text" not in entity:
            continue

        if "youtu" in entity["text"]:
            do_pin = True

    if do_pin:
        bot.pinChatMessage(message.chat, message.message_id)

