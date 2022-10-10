import telebot
import config
import time
import random
import sys
from tcping import Ping
import os
from fun import anekdots
from telebot import types
import datetime
bot = telebot.TeleBot(config.TOKEN)
staff = [5168812451, 1464608585, 1182584762, 1823185825, 1671426989, 5523810980, 5720844448, 1880824191, 848638523]
chats = [-1001726091917, -1001703603450]
inf_mes = 0
mess = None
wait = 0
@bot.message_handler(commands=['coin'])
def coin(message):
    fm = message.from_user.id
    fm = str(fm)
    name = message.from_user.username
    name = str(name)
    print("\n/coin command user from: " + fm + " nickname: " + name)
    id = message.chat.id
    if id in chats:
        id = message.chat.id
        global wait
        if wait == 0:
            global mess
            mess = message.id + 1
            button_1 = types.InlineKeyboardButton('Орёл' , callback_data = '1')
            button_2 = types.InlineKeyboardButton('Решка',callback_data = '2')
            keyboard = types.InlineKeyboardMarkup()
            keyboard.add(button_1)
            keyboard.add(button_2)
            bot.send_message(message.chat.id, '<b>Игра Орёл или Решка!\nВыбери свою ставку</b>',parse_mode='HTML', reply_markup=keyboard)
            wait = 1
            return mess, wait
        else:
            bot.send_message(message.chat.id,'Прошлая игра не закончена\nЕсли игра залагала напишите /creload')
    else:
        bot.send_message(message.chat.id,'Chat invalid')
    
@bot.callback_query_handler(func=lambda call: True)
def coin_sys(call):
    if call.data == "1" or "2":
                global wait
                pon = call.from_user.username
                win1 = random.randint(1,2)
                win1 = str(win1)
                lose = None
                use = None
                if win1 == '1':
                    lose = "Орёл"
                elif win1 == '2':
                    lose = "Решка"
                if call.data == "1":
                    use = "Орёл"
                elif call.data == "2":
                    use = "Решка"
                if call.data == win1:
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=mess, text ="@" + pon+ " Выпал " + lose + " вы выиграли\nВаша ставка: " + use)
                    bot.answer_callback_query(callback_query_id=call.id, text='А вы сегодня везучий!')
                    wait = 0
                    return wait
                else:
                   bot.edit_message_text(chat_id=call.message.chat.id, message_id=mess, text ="@" + pon +" Выпал " + lose + " вы проиграли\nВаша ставка: " + use)
                   bot.answer_callback_query(callback_query_id=call.id, text='Повезёт в следующий раз :(')
                   wait = 0
                   return wait
@bot.message_handler(commands=['creload'])
def creload(message):
    fm = message.from_user.id
    fm = str(fm)
    name = message.from_user.username
    name = str(name)
    print("\n/creload command user from: " + fm + " nickname: " + name)
    id = message.chat.id
    if id in chats:
        bot.send_message(message.chat.id,'Игра перезапущена!')
        global wait
        wait = 0
        return wait
    else:
        bot.send_message(message.chat.id,'Chat invalid')
    
@bot.message_handler(commands=['socmedia'])
def socmedia(message):
    fm = message.from_user.id
    fm = str(fm)
    name = message.from_user.username
    name = str(name)
    print("\n/socmedia command user from: " + fm + " nickname: " + name)
    id = message.chat.id
    if id in chats:    
        button_tt = types.InlineKeyboardButton('⚫ | Tik Tok', url = 'https://www.tiktok.com/@elizzi1' )
        button_yt = types.InlineKeyboardButton('🟥 | YouTube', url = 'https://youtube.com/c/elizzi1')
        button_tw = types.InlineKeyboardButton('🟪 | Twitch', url = 'https://www.twitch.tv/elizzi1?sr=a')
        button_ds = types.InlineKeyboardButton('🟦 | Discord', url = 'https://discord.gg/fukksleep')
        button_tg = types.InlineKeyboardButton('⚪ | Telegram', url = 'https://t.me/fukksleep69')
        button_inst = types.InlineKeyboardButton('🟡 | Instagram', url = 'https://instagram.com/ksenia_elizabeth')
        button_dn = types.InlineKeyboardButton('🔶 | Donation Alerts', url = 'https://www.donationalerts.com/r/elizzi1')
        button_vk = types.InlineKeyboardButton('🔵 | VK', url = 'https://vk.com/ks_eliz')
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(button_tt)
        keyboard.add(button_yt)
        keyboard.add(button_tw)
        keyboard.add(button_ds)
        keyboard.add(button_tg)
        keyboard.add(button_inst)
        keyboard.add(button_dn)
        keyboard.add(button_vk)
        bot.send_message(message.chat.id, '<b>Соц-сети elizzi:</b>',parse_mode='HTML', reply_markup=keyboard)
    else:
        bot.send_message(message.chat.id,'Chat invalid')
    
@bot.message_handler(commands=['ping'])
def ping(message):
    fm = message.from_user.id
    fm = str(fm)
    name = message.from_user.username
    name = str(name)
    id = message.chat.id
    adm = 1880824191
    check = message.from_user.id
    if check in staff:
        if id in chats:
            ping = Ping('api.telegram.org', 443, 60)
            try:
                temp = sys.stdout
                sys.stdout = open('ping.txt', "w")
                ping.ping(1)
                sys.stdout = temp
                with open('ping.txt','r') as DataPing:
                    data = DataPing.readline()
                    data = str(data)
                    data = data.replace('Connected to api.telegram.org[:443]: seq=1 time=',' ')
                    info = "Пинг :" + data
                    bot.send_message(message.chat.id,info)
                    DataPing.close()
                    sys.stdout = temp
            except:
                bot.send_message(message.chat.id,'Пинг : Error')
            else:
                sys.stdout = temp
                print("\n/ping command user from: " + fm + " nickname: " + name)
                sys.stdout = temp
        else:
            bot.send_message(message.chat.id,'Chat invalid')
    else:
            bot.send_message(message.chat.id,'Не достаточно прав')
            

@bot.message_handler(commands=['pon'])
def fun(message):
    global inf_mes
    fm = message.from_user.id
    fm = str(fm)
    name = message.from_user.username
    name = str(name)
    inf_mes += 1
    print("\n/pon command user from: " + fm + " nickname: " + name)
    id = message.chat.id
    if id in chats:
        if inf_mes == 10:
            bot.send_message(message.chat.id,'Вы можете так же прислать\nмемы нам, если\nхотите, что бы их\nдобавили в бота\n👇🏻👇🏻👇🏻\nt.me/neol1tic\nt.me/droonka1')
            inf_mes = 0
        else:
            pass
        media = random.randint(1,3)
        if media == 1:
            folder = 'media/photo/'
            files = os.listdir(folder)
            file = random.choice(files)
            meme_p = folder + file
            bot.send_photo(message.chat.id, photo=open(meme_p, 'rb'))
        elif media == 2:
            folder = 'media/gif/'
            files = os.listdir(folder)
            file = random.choice(files)
            meme_g = folder + file
            bot.send_document(message.chat.id, document=open(meme_g,'rb'))
        else:
            folder = 'media/video/'
            files = os.listdir(folder)
            file = random.choice(files)
            meme_v = folder + file
            bot.send_video(message.chat.id, video=open(meme_v, 'rb'))
    else:
        bot.send_message(message.chat.id,'Chat invalid')

@bot.message_handler(commands=['start'])
def start (message):
    name = message.from_user.username
    date =  datetime.datetime.now().hour
    morning = [6,7,8,9,10,11]
    day = [12,13,14,15,16,17]
    subnight = [18,19,20,21,22,23]
    night = [0,1,2,3,4,5]
    if date in morning:
        bot.send_message(message.chat.id,'👋 • Доброе утро, @' + name +'.\n\n🧑🏻‍💼 • Я вспомогательный бот для Fukk Sleep Chat. Пиши команду ниже, что бы узнать список моих команд.\n\n/support_help')
    elif date in day:
        bot.send_message(message.chat.id,'👋 • Добрый день, @' + name+'.\n\n🧑🏻‍💼 • Я вспомогательный бот для Fukk Sleep Chat. Пиши команду ниже, что бы узнать список моих команд.\n\n/support_help')
    elif date in subnight:
        bot.send_message(message.chat.id,'👋 • Добрый вечер, @' + name+'.\n\n🧑🏻‍💼 • Я вспомогательный бот для Fukk Sleep Chat. Пиши команду ниже, что бы узнать список моих команд.\n\n/support_help')
    elif date in night:
        bot.send_message(message.chat.id,'👋 • Доброй ночи, @' + name+'.\n\n🧑🏻‍💼 • Я вспомогательный бот для Fukk Sleep Chat. Пиши команду ниже, что бы узнать список моих команд.\n\n/support_help')
    else:
        bot.send_message(message.chat.id,'👋 • Здравствуйте, @' + name+'.\n\n🧑🏻‍💼 • Я вспомогательный бот для Fukk Sleep Chat. Пиши команду ниже, что бы узнать список моих команд.\n\n/support_help')
        
@bot.message_handler(commands=['anekdot'])
def anekdot(message):
    fm = message.from_user.id
    fm = str(fm)
    name = message.from_user.username
    name = str(name)
    print("\n/anekdot command user from: " + fm + " nickname: " + name)
    id = message.chat.id
    if id in chats:
        rofl = random.choice(anekdots.anekdots)
        bot.send_message(message.chat.id,rofl)
    else:
        bot.send_message(message.chat.id,'Chat invalid')

@bot.message_handler(commands=['cm'])
def gm(message):
    fm = message.from_user.id
    cM = False
    if fm in staff:
        cM = True
    else:
        cM = False
    fm = str(fm)
    name = message.from_user.username
    name = str(name)
    print("\n/cm command user from: " + fm + " nickname: " + name)
    console = True
    id = message.chat.id
    if id in chats:
        if cM == True:
            bot.send_message(-1001726091917,"Console mode activate")
            print("                   Console mode activate\n")
            while console:
                mess = input(">>> ")
                if mess == 'c.off':
                    console = False
                    print("                    Console mode off\n")
                    bot.send_message(-1001726091917,"Console mode off")
                else:
                    bot.send_message(-1001726091917,mess)
        else:
            bot.send_message(message.chat.id,'Не достаточно прав')
    else:
        bot.send_message(message.chat.id,'Chat invalid')
@bot.message_handler(commands=['support_help'])
def help(message):
    fm = message.from_user.id
    fm = str(fm)
    name = message.from_user.username
    name = str(name)
    print("\n/help command user from: " + fm + " nickname: " + name)
    id = message.chat.id
    if id in chats or 1:
        bot.send_message(message.chat.id,"Мои команды:\n/support_help - Команды\n/ruled - Отправка правил\n/sap - Проверка работы\n/mod - Проверка пользователя на модератора\n/report - Подать жалобу на сообщение\n/cm - Включить консоль мод\n/test - Проверить чат\n/anekdot - Рандомный анекдот\n/start - Приветствие бота\n/pon - Рандомный мем\n/ping - Задержка бота\n/socmedia - Соц.сети Элиззи\n/coin - Орёл или Решка?")
    else:
        bot.send_message(message.chat.id,'Chat invalid')
    

@bot.message_handler(commands=['ruled'])
def rules(message):
    fm = message.from_user.id
    fm = str(fm)
    name = message.from_user.username
    name = str(name)
    print("\n/ruled command user from: " + fm + " nickname: " + name)
    check = message.from_user.id
    id = message.chat.id
    if id in chats:
        if check in staff:
                bot.send_message(-1001726091917,"📚 Правила чата:\n@fukksleeppravila\n@fukksleeppravila\n@fukksleeppravila")
        else:
            bot.send_message(-1001726091917,"Недостаточно прав")
    else:
        bot.send_message(message.chat.id,'Chat invalid')

@bot.message_handler(commands=['sap'])
def ping(message):
    fm = message.from_user.id
    fm = str(fm)
    name = message.from_user.username
    name = str(name)
    print("\n/sap command user from: " + fm + " nickname: " + name)
    id = message.chat.id
    if id in chats:
        bot.send_message(message.chat.id,"✅️ Работаю!")
    else:
        bot.send_message(message.chat.id,'Chat invalid')
@bot.message_handler(commands=['mod'])
def mod(message):
    fm = message.from_user.id
    name = message.from_user.username
    name = str(name)
    print("\n/mod command user from: " + str(fm) + " nickname: " + name)
    if fm in staff:
            bot.send_message(message.chat.id,"✅️ Пользователь найден в датабазе как модератор")
    else:
                     bot.send_message(message.chat.id,"✅️ Пользователь найден в датабазе как обычный учасник")
                     

@bot.message_handler(commands=['test'])
def test(message):
    fm = message.from_user.id
    fm = str(fm)
    name = message.from_user.username
    name = str(name)
    print("\n/test command user from: " + fm + " nickname: " + name)
    id = message.chat.id
    if id in chats:
        bot.send_message(message.chat.id,'Chat valid')
    else:
        bot.send_message(message.chat.id,'Chat invalid')
        
@bot.message_handler(commands=['report'])
def report(message):
    fm = message.from_user.id
    name = message.from_user.username
    name = str(name)
    print("\n/report command user from: " + str(fm) + " nickname: " + name)
    mlink = message.id
    mlink = str(mlink)
    report = message.text
    report = str(report)
    id = message.chat.id
    if id in chats:
        rep = len(staff)
        send = 0
        while send < rep:
            bot.send_message(staff[send],'REPORT DETECTED\nMESSAGE = .' + "https://t.me/c/1726091917/" + mlink+ "\nREPORT:\n" + report)
            send += 1
        bot.send_message(message.chat.id,'📛 Жалоба на сообщение отправлена модерации.\n\nУчтите! За репорт без причины выдаётся наказание.')
    else:
        bot.send_message(message.chat.id,'📛 Жалоба не отправлена\nЧат не прошел проверку') 
#RUN
bot.polling(none_stop=True)