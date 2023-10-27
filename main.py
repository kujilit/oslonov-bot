import telebot
import threading
from decouple import config
from values import ExchangeRate

bot_key = config('bot_key',default='')

types = telebot.types
bot = telebot.TeleBot(bot_key)

course = ExchangeRate.get_value()

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, 'Введите цену товара в юанях.')


@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, f'{int(message.text) * cource + 2200}')


bot.infinity_polling()