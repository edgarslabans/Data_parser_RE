import telebot

bot = telebot.TeleBot("5001452931:AAGx9oAAOydhDzh-CH9buF5Ot9kVUd0nybQ")


@bot.message_handler(commands=['start'])
def start_command(message):
   bot.send_message(
       message.chat.id,
       'Greetings!XXX I can show you PrivatBank exchange rates.\n' +
       'To get the exchange rates press /exchange.\n' +
       'To get help press /help.'
   )


bot.polling(none_stop=True)
