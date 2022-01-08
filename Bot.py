import telebot
import config
import random

bot = telebot.TeleBot(config.telegram_token)


@bot.message_handler(content_types=["text"])
def testfunction(message):
    bot.send_message(message.chat.id, message.text)


bot.polling(none_stop=True)
