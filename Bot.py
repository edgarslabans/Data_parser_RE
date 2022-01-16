import telebot
import config
import random
import atslega
from telebot import types

bot = telebot.TeleBot(atslega.tel_key)

# hosting opportunity
# selectel.ru




@bot.message_handler(commands=['start'])
def start_command(message):
   bot.send_message(
       message.chat.id,
       'Greetings! I can show you PrivatBank exchange rates.\n' +
       'To get the exchange rates press /exchange.\n' +
       'To get help press /help.'
   )


bot.polling(none_stop=True)
