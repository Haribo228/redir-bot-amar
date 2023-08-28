import telebot

from telebot import types

TOKEN = '5656830992:AAGr6ZrHy1Acx6LiDzwlxEDemvxs2Z5NXXw'

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def welcome(message):

 # keyboard

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Earn Money")

    markup.add(item1)

    bot.send_message(message.chat.id, "✅Click here,subscribe and get 25.000 now👉http://bets-india.com?gnat=544892657441079"
                     .format(message.from_user, bot.get_me()),
                     parse_mode='html', reply_markup=markup)
#  Добро пожаловать, {0.first_name}!\nЯ - <b>{1.first_name}</b>, бот созданный чтобы быть подопытным кроликом.


@bot.message_handler(content_types=['text'])
def lalala(message):
    if message.text == 'Earn Money':
        bot.send_message(message.chat.id, "http://bets-india.com?gnat=544892657441079
                         .format(message.from_user, bot.get_me()),
                        
                         parse_mode='html')
       #bot.send_message( 'http://redir-2.vercel.app' )


bot.polling(none_stop=True)
