from .token import bot
from .lib.lurkmore import Lurkmore

a = Lurkmore()
a.url = "https://absurdopedia.net/w/api.php"
a.url2 = "https://absurdopedia.net/"


@bot.message_handler(commands=["absurd"])
def getAbsurd(message, logs=False):
    options = message.text.split(maxsplit=1)
    if len(options) == 1:
        bot.reply_to(message, "Напишите название статьи")
        return

    query = options[1]
    print(f"[Absurdowiki] {query}")

    try:
        try:
            s = a.search(query)
            p = a.getPage(s[0])
            i = a.getImagesList(s[0])
        except:
            p = a.getPage(query)
            i = a.getImagesList(query)
    except Exception as e:
        print(e)
        bot.reply_to(message, "Не найдено")
        return

    # for item in i:
    #     bot.send_photo(message.chat.id, lurk.getImage(item), caption=item)

    if len(i) != 0:
        try:
            image = a.getImage(i[0])
            bot.send_chat_action(message.chat.id, "upload_photo")
            bot.send_photo(message.chat.id,
                           image,
                           caption=a.parse(p)[:1000],
                           reply_to_message_id=message.message_id,
                           parse_mode="HTML")
        except Exception as e:
            bot.send_chat_action(message.chat.id, "typing")
            bot.reply_to(message, e)
            try:
                bot.reply_to(message, a.parse(p)[:4096], parse_mode="HTML")
            except:
                bot.reply_to(message, a.parse(p)[:4096])
    else:
        bot.reply_to(message, a.parse(p)[:4096], parse_mode="HTML")
