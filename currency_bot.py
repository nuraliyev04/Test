import telebot
import requests
from telebot import types

data = {
    "success": True,
    "request": {
        "from": "USD",
        "to": "UZS",
        "amount": 1
    },
    "meta": {
        "timestamp": 1712902770822,
        "rates": {
            "from": 12668.85781,
            "to": 0.0000789337
        },
        "formated": {
            "from": "1 USD = 12668.85781 UZS",
            "to": "1 UZS = 0.00008 USD"
        }
    },
    "result": 12668.85781
}

token = '7118796659:AAFEDz8_XLojvnZWyCCC025w_xj25zyTCc4'

API = "https://currency-converter-pro1.p.rapidapi.com/convert"

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start(message):
        markup = types.InlineKeyboardMarkup()
        markup.row(
        types.InlineKeyboardButton('GBP', callback_data='GBP'),
        types.InlineKeyboardButton('USD', callback_data='USD'),
        types.InlineKeyboardButton('RUB', callback_data='RUB')
        )
        bot.send_message(message.chat.id, 'Choose a currency', reply_markup=markup)
