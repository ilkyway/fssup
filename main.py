import telebot
import config
import time
import random
import sys
from tcping import Ping
import os
from fun import anekdots
bot = telebot.TeleBot(config.TOKEN)
staff = [5168812451, 1464608585, 1182584762, 1823185825, 1671426989, 5523810980, 5720844448, 1880824191, 848638523]
inf_mes = 0
 
@bot.message_handler(commands=['socmedia'])
def socmedia(message):
    fm = message.from_user.id
    fm = str(fm)
    name = message.from_user.username
    name = str(name)
    print("\n/socmedia command user from: " + fm + " nickname: " + name)
    id = message.chat.id
    if id == -1001726091917:    
        media = '<b>Соц-сети elizzi:</b>\n<a href="https://www.tiktok.com/@elizzi1?_t=8WMU4nnSAuw&_r=1">TikTok</a>\n<a href="https://youtube.com/c/elizzi1">Youtube</a>\n<a href="https://www.twitch.tv/elizzi1?sr=a">Twitch</a>\n<a href="https://discord.gg/fukksleep">Discord</a>\n<a href="https://t.me/fukksleep69">Telegram</a>\n<a href="https://instagram.com/ksenia_elizabeth?igshid=YmMyMTA2M2Y=">Instagram</a>\n<a href="https://www.donationalerts.com/r/elizzi1">Donation Alerts</a>\n<a href="https://vk.com/ks_eliz">VK</a>'
        bot.send_message(message.chat.id,media, parse_mode='HTML', disable_web_page_preview = True)
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
    global inf_mes
    fm = message.from_user.id
    fm = str(fm)
    name = message.from_user.username
    name = str(name)
    inf_mes += 1
    print("\n/pon command user from: " + fm + " nickname: " + name)
    id = message.chat.id
    if id == -1001726091917:
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
    if id == -1001726091917 or 1:
        bot.send_message(message.chat.id,"Мои команды:\n/support_help - Команды\n/ruled - Отправка правил\n/sap - Проверка работы\n/mod - Проверка пользователя на модератора\n/report - Подать жалобу на сообщение\n/cm - Включить консоль мод\n/test - Проверить чат\n/anekdot - Рандомный анекдот\n/start - Приветствие бота\n/pon - Рандомный мем\n/ping - Задержка бота\n/socmedia - Соц.сети Элиззи")
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