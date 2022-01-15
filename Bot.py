import telebot
import config
import random

bot = telebot.TeleBot(config.telegram_token)

# hosting opportunity
# selectel.ru

@bot.message_handler(content_types=["text"])
def testfunction(message):
    bot.send_message(message.chat.id, message.text)


#test buttons
markup = types.InlineKeyboardMarkup()

for key, value in stringList.items():
    markup.add(types.InlineKeyboardButton(text=value,
                                          callback_data="['value', '" + value + "', '" + key + "']"),
               types.InlineKeyboardButton(text=crossIcon,
                                          callback_data="['key', '" + key + "']"))


bot.polling(none_stop=True)
