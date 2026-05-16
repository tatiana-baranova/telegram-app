import os
import telebot
from dotenv import load_dotenv
from telebot import types
load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(TOKEN)
@bot.message_handler(commands=['youtube'])
def open_website(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Відвідати сайт', url="https://music.youtube.com/" ))
    bot.send_message(message.chat.id, 'Чудовий вибір, натискай швидше на кнопку 📻', parse_mode='HTML', reply_markup=markup)


@bot.message_handler(commands=['instagram'])
def instagram(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Відвідати сайт', url="https://www.instagram.com/" ))
    bot.send_message(message.chat.id, 'Чудовий вибір, натискай швидше на кнопку 📩', parse_mode='HTML', reply_markup=markup)

@bot.message_handler(commands=['linkedin'])
def instagram(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Відвідати сайт', url="https://www.linkedin.com/" ))
    bot.send_message(message.chat.id, 'Чудовий вибір, натискай швидше на кнопку 📠', parse_mode='HTML', reply_markup=markup)

# @bot.message_handler(content_types=['text'])
# def mess(message):
#     get_message_bot = message.text.strip().lower()
#     if get_message_bot == 'Створення ігри':
#         markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
#         btn1 = types.KeyboardButton("На мобільний телефон")
#         btn2 = types.KeyboardButton("Комп'ютерні і консоль")
#         btn3 = types.KeyboardButton("Віртуальна реальність")
#         btn4 = types.KeyboardButton("Web ігра")
#         markup.add(btn1, btn2, btn3, btn4)
#         final_message = "Для розробки потрібно зробити вибір"
#     else:
#         markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
#         btn1 = types.KeyboardButton("Створення ігри")
#         btn2 = types.KeyboardButton("Мобільні застосунки")
#         btn3 = types.KeyboardButton("Веб розробка")
#         btn4 = types.KeyboardButton("Створення ШІ")
#         markup.add(btn1, btn2, btn3, btn4)
#         final_message = 'Щось пішло не так, обери краще з кнопок'
#
#     bot.send_message(message.chat.id, final_message, parse_mode='HTML', reply_markup=markup)

@bot.message_handler(commands=['start'])
def start(message):

    name = message.from_user.first_name
    last_name = message.from_user.last_name or ""

    send_mess = (
        f"<b>Привіт {name} {last_name}</b>!\n"
        f"Який напрямок тебе цікавить?"
    )
    bot.send_message(message.chat.id, send_mess, parse_mode='HTML')

bot.polling(none_stop=True)

