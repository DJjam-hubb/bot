# -*- coding: utf8 -*-
import telebot
import requests
from datetime import datetime



bot = telebot.TeleBot('1050229554:AAFPkDrue8DnVa3T1ir-nCv3xg3Nq4ww-jA')

@bot.message_handler(content_types=['text'])

def get_text_messages(message):
    if message.text == "Привет":
        bot.send_message(message.from_user.id, "Привет, чем я могу тебе помочь?")




bot.polling(none_stop=True)
