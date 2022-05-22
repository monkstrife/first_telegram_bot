import telebot

bot = telebot.TeleBot('5345333077:AAHUh_1S0z_jGcikUlFO1lIVZTl574hVBYQ')


@bot.message_handler(commands=['start'])
def start(message):
    mess = f'<b>Мяу, {message.from_user.first_name}.\nЯ твой новый бот.\nПоцелуй зайку, что слева)</b>'
    bot.send_message(message.chat.id, mess, parse_mode='html')


@bot.message_handler(commands=['+'])
def get_mess(message):
    bot.send_message(message.chat.id, '<b>Отлично, на выбор введи /число от <u>1 до 3</u>, которое скажет тебе, что нужно сделать</b>', parse_mode='html')

@bot.message_handler(commands=['1', '2', '3'])
def you_must_do_it(message):
    if(message.text == '/1'):
        bot.send_message(message.chat.id, '<b>Поставь чайник, пж</b>', parse_mode='html')
    elif(message.text == '/2'):
        bot.send_message(message.chat.id, '<b>Сходишь со мной в подземелье?</b>', parse_mode='html')
    elif(message.text == '/3'):
        bot.send_message(message.chat.id, '<b><u>Сегодня вечером у нас должен быть...!</u></b>', parse_mode='html')


@bot.message_handler()
def start(message):
    bot.send_message(message.chat.id, '<b>Хм, хорошо.\nТеперь введи /+ для продолжения</b>', parse_mode='html')


bot.polling(non_stop=True)
