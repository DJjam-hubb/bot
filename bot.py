# -*- coding: utf8 -*-
import telebot
import requests
from datetime import datetime

bot = telebot.TeleBot('1050229554:AAFPkDrue8DnVa3T1ir-nCv3xg3Nq4ww-jA')


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "/start":
        bot.send_message(message.from_user.id, "Привет,я Шпипс отправь мне любое сообщение и получи расписание.")
        user_id = message.from_user.id
        bot.send_message(815652307, user_id)
    else:
        user_id = message.from_user.id
        if user_id == 972959464:
            bot.send_message(815652307, message.text)
        keyboard = telebot.types.InlineKeyboardMarkup()
        key_1 = telebot.types.InlineKeyboardButton(text='Расписание 11 а', callback_data='rasp')
        keyboard.add(key_1)
        key_1_1 = telebot.types.InlineKeyboardButton(text='Расписание 11 б', callback_data='rasp1')
        keyboard.add(key_1_1)
        key_3 = telebot.types.InlineKeyboardButton(text='До ЕГЭ...', callback_data='ege')
        keyboard.add(key_3)
        bot.send_message(message.from_user.id, text="Привет :)", reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == "rasp":

        res = requests.get('http://brgi.ucoz.ru/index/raspisanie_urokov/0-65', timeout=30.0)
        res.encoding = 'cp1251'
        urll = res.text
        z = urll.index("http://brgi.ucoz.ru/raspisanie/")
        urll = urll[z:]
        z = urll.index('"')
        x = urll[:z]
        date = x[31:36] + ".2020"
        result = requests.get(x, timeout=30.0)
        result.encoding = 'cp1251'
        page = result.text
        l1 = page.index('09:15')
        l2 = page.index('10:10')
        l3 = page.index('11:15')
        l4 = page.index('12:20')
        l5 = page.index('13:15')
        l6 = page.index('14:15')
        l7 = page.index('15:10')
        l8 = page.index('16:05')

        page1 = page[l1:l2].split(
            "<td class=T1 style=';border-top:2 solid #707070;text-align:left;border-top:2 solid #707070")
        page1 = page1[21].split(">")

        page1 = "".join(page1)
        page1 = [word for word in page1 if 1039 < ord(word[0])]
        page1 = "".join(page1)
        if "Б" in page1[5:]:
            page1 = page1.replace("Б", " / Б")
        elif "Х" in page1[5:]:
            page1 = page1.replace("Х", " / Х")
        elif "И" in page1[5:]:
            page1 = page1.replace("И", " / И")
        elif "Ф" in page1[5:]:
            page1 = page1.replace("Ф", " / Ф")
        if len(page1) != 0:
            page1 = "1) " + page1

        page2 = page[l2:l3].split(" <td class=T1 style=';text-align:left'><table cellspacing=0 border=0")
        page2 = page2[21].split(">")
        page2 = "".join(page2)
        page2 = [word for word in page2 if 1039 < ord(word[0])]
        page2 = "".join(page2)
        if "Б" in page2[5:]:
            page2 = page2.replace("Б", " / Б")
        elif "Х" in page2[5:]:
            page2 = page2.replace("Х", " / Х")
        elif "И" in page2[5:]:
            page2 = page2.replace("И", " / И")
        elif "Ф" in page2[5:]:
            page2 = page2.replace("Ф", " / Ф")
        if len(page2) != 0:
            page2 = "2) " + page2

        page3 = page[l3:l4].split("<td class=T1 style=';text-align:left'><table cellspacing=0 border=0")
        page3 = page3[21]
        page3 = "".join(page3)
        page3 = [word for word in page3 if 1039 < ord(word[0])]
        page3 = "".join(page3)
        if "Б" in page3[5:]:
            page3 = page3.replace("Б", " / Б")
        elif "Х" in page3[5:]:
            page3 = page3.replace("Х", " / Х")
        elif "И" in page3[5:]:
            page3 = page3.replace("И", " / И")
        elif "Ф" in page3[5:]:
            page3 = page3.replace("Ф", " / Ф")
        if len(page3) != 0:
            page3 = "3) " + page3

        page4 = page[l4:l5].split("<td class=T1 style=';text-align:left'><table cellspacing=0 border=0")
        page4 = page4[21]
        page4 = [word for word in page4 if 1039 < ord(word[0])]
        page4 = "".join(page4)
        if "Б" in page4[5:]:
            page4 = page4.replace("Б", " / Б")
        elif "Х" in page4[5:]:
            page4 = page4.replace("Х", " / Х")
        elif "И" in page4[5:]:
            page4 = page4.replace("И", " / И")
        elif "Ф" in page4[5:]:
            page4 = page4.replace("Ф", " / Ф")
        if len(page4) != 0:
            page4 = "4) " + page4

        page5 = page[l5:l6].split(" <td class=T1 style=';text-align:left'><table cellspacing=0 border=0")
        page5 = page5[21]
        page5 = [word for word in page5 if 1039 < ord(word[0])]
        page5 = "".join(page5)
        if "Б" in page5[5:]:
            page5 = page5.replace("Б", " / Б")
        elif "Х" in page5[5:]:
            page5 = page5.replace("Х", " / Х")
        elif "И" in page5[5:]:
            page5 = page5.replace("И", " / И")
        elif "Ф" in page5[5:]:
            page5 = page5.replace("Ф", " / Ф")
        if len(page5) != 0:
            page5 = "5) " + page5

        page6 = page[l6:l7].split("<td class=T1 style=';text-align:left'><table cellspacing=0 border=0")
        page6 = page6[21]
        page6 = [word for word in page6 if 1039 < ord(word[0])]
        page6 = "".join(page6)
        if "Б" in page6[5:]:
            page6 = page6.replace("Б", " / Б")
        elif "Х" in page6[5:]:
            page6 = page6.replace("Х", " / Х")
        elif "И" in page6[5:]:
            page6 = page6.replace("И", " / И")
        elif "Ф" in page6[5:]:
            page6 = page6.replace("Ф", " / Ф")
        if len(page6) != 0:
            page6 = "6) " + page6

        page7 = page[l7:l8].split("<td class=T1 style=';text-align:left'>")
        page7 = page7[21]
        page7 = [word for word in page7 if 1039 < ord(word[0])]
        page7 = "".join(page7)
        if "Б" in page7[5:]:
            page7 = page7.replace("Б", " / Б")
        elif "Х" in page7[5:]:
            page7 = page7.replace("Х", " / Х")
        elif "И" in page7[5:]:
            page7 = page7.replace("И", " / И")
        elif "Ф" in page7[5:]:
            page7 = page7.replace("Ф", " / Ф")

        if len(page7) != 0:
            page7 = "7) " + page7

        page8 = page[l8:-1].split("<td class=T1 style=';text-align:left'>")
        page8 = page8[21]
        page8 = [word for word in page8 if 1039 < ord(word[0])]
        page8 = "".join(page8)
        if "Б" in page8[5:]:
            page8 = page8.replace("Б", " / Б")
        elif "Х" in page8[5:]:
            page8 = page8.replace("Х", " / Х")
        elif "И" in page8[5:]:
            page8 = page8.replace("И", " / И")
        elif "Ф" in page8[5:]:
            page8 = page8.replace("Ф", " / Ф")

        if len(page8) != 0:
            page8 = "8) " + page8

        a = "Расписание 11а на " + date + "\n" + "\n"
        a += page1 + "\n" + page2 + "\n" + page3 + "\n" + page4 + "\n" + page5 + "\n" + page6 + "\n" + page7 + "\n"

        if "язык" in a:
            a = a.replace("язык", " язык")
        if "литература" in a:
            a = a.replace("литература", " литература")
        if "культура" in a:
            a = a.replace("культура", " культура")
        if "актзал" in a:
            a = a.replace("актзал", " акт.зал")
        if "Алгебраиначалаанализа" in a:
            a = a.replace("Алгебраиначалаанализа", "Алгебра")

        bot.send_message(call.from_user.id, a)

    if call.data == "rasp1":
        res = requests.get('http://brgi.ucoz.ru/index/raspisanie_urokov/0-65', timeout=30.0)
        res.encoding = 'cp1251'
        urll = res.text
        z = urll.index("http://brgi.ucoz.ru/raspisanie/")
        urll = urll[z:]
        z = urll.index('"')
        x = urll[:z]
        date = x[31:36] + ".2020"
        result = requests.get(x, timeout=30.0)
        result.encoding = 'cp1251'
        page = result.text
        l1 = page.index('09:15')
        l2 = page.index('10:10')
        l3 = page.index('11:15')
        l4 = page.index('12:20')
        l5 = page.index('13:15')
        l6 = page.index('14:15')
        l7 = page.index('15:10')
        l8 = page.index('16:05')

        page1 = page[l1:l2].split(
            "<td class=T1 style=';border-top:2 solid #707070;text-align:left;border-top:2 solid #707070")
        page1 = page1[22].split(">")

        page1 = "".join(page1)
        page1 = [word for word in page1 if 1039 < ord(word[0])]
        page1 = "".join(page1)
        if "Б" in page1[5:]:
            page1 = page1.replace("Б", " / Б")
        elif "Х" in page1[5:]:
            page1 = page1.replace("Х", " / Х")
        elif "И" in page1[5:]:
            page1 = page1.replace("И", " / И")
        elif "Ф" in page1[5:]:
            page1 = page1.replace("Ф", " / Ф")
        if len(page1) != 0:
            page1 = "1) " + page1

        page2 = page[l2:l3].split(" <td class=T1 style=';text-align:left'><table cellspacing=0 border=0")
        page2 = page2[22].split(">")
        page2 = "".join(page2)
        page2 = [word for word in page2 if 1039 < ord(word[0])]
        page2 = "".join(page2)
        if "Б" in page2[5:]:
            page2 = page2.replace("Б", " / Б")
        elif "Х" in page2[5:]:
            page2 = page2.replace("Х", " / Х")
        elif "И" in page2[5:]:
            page2 = page2.replace("И", " / И")
        elif "Ф" in page2[5:]:
            page2 = page2.replace("Ф", " / Ф")
        if len(page2) != 0:
            page2 = "2) " + page2

        page3 = page[l3:l4].split("<td class=T1 style=';text-align:left'><table cellspacing=0 border=0")
        page3 = page3[22]
        page3 = "".join(page3)
        page3 = [word for word in page3 if 1039 < ord(word[0])]
        page3 = "".join(page3)
        if "Б" in page3[5:]:
            page3 = page3.replace("Б", " / Б")
        elif "Х" in page3[5:]:
            page3 = page3.replace("Х", " / Х")
        elif "И" in page3[5:]:
            page3 = page3.replace("И", " / И")
        elif "Ф" in page3[5:]:
            page3 = page3.replace("Ф", " / Ф")
        if len(page3) != 0:
            page3 = "3) " + page3

        page4 = page[l4:l5].split("<td class=T1 style=';text-align:left'><table cellspacing=0 border=0")
        page4 = page4[22]
        page4 = [word for word in page4 if 1039 < ord(word[0])]
        page4 = "".join(page4)
        if "Б" in page4[5:]:
            page4 = page4.replace("Б", " / Б")
        elif "Х" in page4[5:]:
            page4 = page4.replace("Х", " / Х")
        elif "И" in page4[5:]:
            page4 = page4.replace("И", " / И")
        elif "Ф" in page4[5:]:
            page4 = page4.replace("Ф", " / Ф")
        if len(page4) != 0:
            page4 = "4) " + page4

        page5 = page[l5:l6].split(" <td class=T1 style=';text-align:left'><table cellspacing=0 border=0")
        page5 = page5[22]
        page5 = [word for word in page5 if 1039 < ord(word[0])]
        page5 = "".join(page5)
        if "Б" in page5[5:]:
            page5 = page5.replace("Б", " / Б")
        elif "Х" in page5[5:]:
            page5 = page5.replace("Х", " / Х")
        elif "И" in page5[5:]:
            page5 = page5.replace("И", " / И")
        elif "Ф" in page5[5:]:
            page5 = page5.replace("Ф", " / Ф")
        if len(page5) != 0:
            page5 = "5) " + page5

        page6 = page[l6:l7].split("<td class=T1 style=';text-align:left'><table cellspacing=0 border=0")
        page6 = page6[22]
        page6 = [word for word in page6 if 1039 < ord(word[0])]
        page6 = "".join(page6)
        if "Б" in page6[5:]:
            page6 = page6.replace("Б", " / Б")
        elif "Х" in page6[5:]:
            page6 = page6.replace("Х", " / Х")
        elif "И" in page6[5:]:
            page6 = page6.replace("И", " / И")
        elif "Ф" in page6[5:]:
            page6 = page6.replace("Ф", " / Ф")
        if len(page6) != 0:
            page6 = "6) " + page6

        page7 = page[l7:l8].split("<td class=T1 style=';text-align:left'>")
        page7 = page7[22]
        page7 = [word for word in page7 if 1039 < ord(word[0])]
        page7 = "".join(page7)
        if "Б" in page7[5:]:
            page7 = page7.replace("Б", " / Б")
        elif "Х" in page7[5:]:
            page7 = page7.replace("Х", " / Х")
        elif "И" in page7[5:]:
            page7 = page7.replace("И", " / И")
        elif "Ф" in page7[5:]:
            page7 = page7.replace("Ф", " / Ф")

        if len(page7) != 0:
            page7 = "7) " + page7

        page8 = page[l8:-1].split("<td class=T1 style=';text-align:left'>")
        page8 = page8[22]
        page8 = [word for word in page8 if 1039 < ord(word[0])]
        page8 = "".join(page8)
        if "Б" in page8[5:]:
            page8 = page8.replace("Б", " / Б")
        elif "Х" in page8[5:]:
            page8 = page8.replace("Х", " / Х")
        elif "И" in page8[5:]:
            page8 = page8.replace("И", " / И")
        elif "Ф" in page8[5:]:
            page8 = page8.replace("Ф", " / Ф")

        if len(page8) != 0:
            page8 = "8) " + page8

        a = "Расписание 11б на " + date + "\n" + "\n"
        a += page1 + "\n" + page2 + "\n" + page3 + "\n" + page4 + "\n" + page5 + "\n" + page6 + "\n" + page7 + "\n"

        if "язык" in a:
            a = a.replace("язык", " язык")
        if "литература" in a:
            a = a.replace("литература", " литература")
        if "культура" in a:
            a = a.replace("культура", " культура")
        if "актзал" in a:
            a = a.replace("актзал", " акт.зал")
        if "Алгебраиначалаанализа" in a:
            a = a.replace("Алгебраиначалаанализа", "Алгебра")

        bot.send_message(call.from_user.id, a)


    if call.data == "ege":
        q = str(datetime.now())
        q = q[:10]
        q = q[-2:] + "." + q[-5:-3] + "." + "2020"
        d1 = datetime.strptime(q, "%d.%m.%Y")
        d2 = datetime.strptime("25.05.2020", "%d.%m.%Y")
        q = str((d2 - d1).days) + " дн. (до 25 мая)"
        bot.send_message(call.from_user.id, q)

bot.polling(none_stop=True)
