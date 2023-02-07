#!/usr/bin/python

import telebot
import os
from telebot import types # для указание типов

API_TOKEN = '5554528885:AAF0QdnB1KeUHKsgIhoINp-2XdjGzxv8a6U'

bot = telebot.TeleBot(API_TOKEN)


# # Handle '/start' and '/help'
# @bot.message_handler(commands=['help', 'start'])
# def send_welcome(message):
#     bot.reply_to(message, """\
# Дарова брат\
# """)


@bot.message_handler(content_types=['photo'])
def handle_docs_photo(message):
    chat_id = message.chat.id
    file_info = bot.get_file(message.photo[-1].file_id)
    downloaded_file = bot.download_file(file_info.file_path)
    src = '/Users/valeriazaborovskaya/Desktop/digits_bot/photos/' + message.photo[-1].file_id + '.jpg';
    with open(src, 'wb') as new_file:
        new_file.write(downloaded_file)
    bot.reply_to(message, "Это цифра кек")
    if os.path.isfile(src):
        os.remove(src)


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Поздороваться")
    btn2 = types.KeyboardButton("Сделать что-то")
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id,
                     text="Привет, {0.first_name}!".format(message.from_user), reply_markup=markup)


@bot.message_handler(content_types=['text', 'photo'])
def func(message):
    if (message.text == "Поздороваться"):
        bot.send_message(message.chat.id, text="Eще раз привет 😼")
    elif (message.text == "Сделать что-то"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Распознавание цифр")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn1, back)
        bot.send_message(message.chat.id, text="Вот что я умею:", reply_markup=markup)

    elif (message.text == "Распознавание цифр"):
        bot.send_message(message.chat.id, '''
        Пришлите цифру на однородном фоне, расположенную примерно по центру картинки
        ''')


    elif (message.text == "Вернуться в главное меню"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("Поздороваться")
        button2 = types.KeyboardButton("Сделать что-то")
        markup.add(button1, button2)
        bot.send_message(message.chat.id, text="Вы вернулись в главное меню", reply_markup=markup)
    else:
        bot.send_message(message.chat.id, text=message.text)


# ответ на ;тект; ;текстом;
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, message.text)


bot.infinity_polling()

''' хороший код, возвращает файл айди, может пригодиться если вытаскивать файл по ссылке'''
# @bot.message_handler(content_types=['photo'])
# def photo(message):
#     print('message.photo =', message.photo)
#     fileID = message.photo[-1].file_id
#     print('fileID =', fileID)
#     file = bot.get_file(fileID)
#     print('file.file_path =', file.file_path)


# сохраняем файл
# @bot.message_handler(content_types=['document', 'photo'])
# def handle_docs_photo(message):
#     bot.reply_to(message, "тест")
#     try:
#         chat_id = message.chat.id
#         file_info = bot.get_file(message.document.file_id)
#         downloaded_file = bot.download_file(file_info.file_path)
#         src = '/Users/valeriazaborovskaya/Desktop/digits_bot/photos/' + message.document.file_name;
#         with open(src, 'wb') as new_file:
#             new_file.write(downloaded_file)
#         bot.reply_to(message, "Пожалуй, я сохраню это")
#     except Exception as e:
#         bot.reply_to(message, e)
