import telebot
import config
import time
import random
import sys
from tcping import Ping
bot = telebot.TeleBot(config.TOKEN)
staff = [5168812451, 1464608585, 1182584762, 1823185825, 1671426989, 5523810980, 5720844448, 1880824191, 848638523]
 
#@bot.message_handler(commands=['mping'])
#def zx(message):
#    #while True:
#        #bot.send_message(848638523,'РАБОТАЙ ДАУН')
#        pass

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
        if id == -1001726091917:
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
    fm = message.from_user.id
    fm = str(fm)
    name = message.from_user.username
    name = str(name)
    print("\n/pon command user from: " + fm + " nickname: " + name)
    id = message.chat.id
    if id == -1001726091917:
        media = random.randint(1,3)
        if media == 1:
            photo = random.randint(1,43)
            photo = str(photo)
            meme_p = 'media/photo/' + photo + '.jpg'
            bot.send_photo(message.chat.id, photo=open(meme_p, 'rb'))
        elif media == 2:
            gif = random.randint(1,30)
            gif = str(gif)
            meme_g = 'media/gif/' + gif + '.gif'
            bot.send_document(message.chat.id, document=open(meme_g,'rb'))
        else:
            video = random.randint(1,44)
            video = str(video)
            meme_v = 'media/video/' + video + '.mp4'
            bot.send_video(message.chat.id, video=open(meme_v, 'rb'))
    else:
        bot.send_message(message.chat.id,'Chat invalid')

@bot.message_handler(commands=['start'])
def start (message):
    fm = message.from_user.id
    fm = str(fm)
    name = message.from_user.username
    name = str(name)
    print("\n/start command user from: " + fm + " nickname: " + name)
    bot.send_message(message.chat.id,'🤵🏻 Вас приветствует бот Fukk Sleep Support!\n\n🧑🏻‍💻 Я - бот-помощник для этого чата. Посмотреть список моих команд можно командой /support_help')
        
@bot.message_handler(commands=['anekdot'])
def anekdot(message):
    fm = message.from_user.id
    fm = str(fm)
    name = message.from_user.username
    name = str(name)
    print("\n/anekdot command user from: " + fm + " nickname: " + name)
    id = message.chat.id
    if id == -1001726091917:
        with open("fun/anekdots.txt") as inp:
            lines = inp.readlines()
            anekdot = random.choice(lines).strip()
            bot.send_message(message.chat.id,anekdot)
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
    if id == -1001726091917:
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
    if id == -1001726091917:
        bot.send_message(message.chat.id,"Мои команды:\n/support_help - Команды\n/ruled - Отправка правил\n/sap - Проверка работы\n/mod - Проверка пользователя на модератора\n/report - Подать жалобу на сообщение\n/cm - Включить консоль мод\n/test - Проверить чат\n/anekdot - Рандомный анекдот\n/start - Приветствие бота\n/pon - Рандомный мем\n/ping - Задержка бота")
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
    if id == -1001726091917:
        if check in staff:
            while True:
                bot.send_message(-1001726091917,"📚 Правила чата:\n@fukksleeppravila\n@fukksleeppravila\n@fukksleeppravila")
                time.sleep(7200)
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
    if id == -1001726091917:
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
    if id == -1001726091917:
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
    if id == -1001726091917:
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