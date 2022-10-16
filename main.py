# -*- coding: utf-8 -*-
import config
import time
import random
import sys
from tcping import Ping
import os
from fun import anekdots
from aiogram import Bot, Dispatcher, executor, types
import datetime
import time
from dbmanager import DB
import logging

staff = [5168812451, 1464608585, 1182584762, 1823185825, 1671426989, 5523810980, 5720844448, 1880824191, 848638523, 1040763170]
chats = [-1001726091917, -1001703603450]
shop_send = [1880824191, 848638523, 5720844448, 1040763170]
inf_mes = 0
mess = None
wait = 0
coin_msg = None
shop_msg = None
shop_reply = None
shop_main = None
shop_keyboard = None
ptime = time.time()
logging.basicConfig(level=logging.INFO)
bot = Bot(token=config.TOKEN)
dp = Dispatcher(bot)
# кулдаун функция (я не знаю как это работает и почему кулдауны не смешиваются, честно)
def timediff(a):
	global ptime
	seconds = time.time() - ptime
	if float(f'{seconds:.1f}') > a:
		ptime = time.time()
		return True
	else: 
		return False
@dp.message_handler(commands=['shop', 'coinshop', 'shopcoin'], commands_prefix='/.')
async def shop(message: types.Message):
	# мануал магазин
	global shop_msg
	global shop_main
	global shop_keyboard
	id = message.chat.id
	shop_msg = message
	#товары, для удобства да
	RemoveWarn = "Убрать Пред"
	CustomRole = "Каст. роль"
	PinMessage = "Закреп. сообщения"
	FastFarm = "Уменьшить КД"
	BuyDudu = "Купить Duducoin"
	if id in chats:
		try:
			#shop_reply = message.reply_to_message
			shop_reply = None
			button_rw = types.InlineKeyboardButton(str(RemoveWarn), callback_data = 'rw')
			button_cr = types.InlineKeyboardButton(str(CustomRole), callback_data = 'cr')
			button_pm = types.InlineKeyboardButton(str(PinMessage), callback_data = 'pm')
			button_ff = types.InlineKeyboardButton(str(FastFarm), callback_data = 'ff')
			button_bd = types.InlineKeyboardButton(str(BuyDudu), callback_data = 'bd')
			shop_keyboard = types.InlineKeyboardMarkup()
			shop_keyboard.add(button_rw, button_cr)
			shop_keyboard.add(button_pm, button_ff)
			shop_keyboard.add(button_bd)
			shop_main = await bot.send_message(message.from_user.id,"<b>МАГАЗИН</b>", reply_markup=shop_keyboard, parse_mode="HTML")
			await message.reply('Товары отправлены вам в ЛС!')
		except:
		   await  message.reply("Пожалуста откройте лс бота")
	else: 
		await message.reply('Chat invalid')
@dp.callback_query_handler(lambda call: True)
async def shop_sys(call: types.CallbackQuery):
	# это тест
	global shop_main
	global shop_keyboard
	global shop_msg
	db = DB()
#	if call.from_user.id != shop_msg.from_user.id:
#			await bot.answer_callback_query(callback_query_id=call.id, text='Дудкам нельзя!', show_alert=True)
	#suid = int(message.reply_to_message.from_user.id)
	if call.data == "rw":
		buy_rw = types.InlineKeyboardButton("Купить", callback_data = 'buy_rw')
		no_rw = types.InlineKeyboardButton("Нет", callback_data = 'no_rw')
		buy_keyboard = types.InlineKeyboardMarkup()
		buy_keyboard.add(buy_rw,no_rw)
		await bot.send_message(call.from_user.id, f'Хотите купить "Снятие преда" за <b>800 DuDuCoin’ов?</b>', reply_markup=buy_keyboard,parse_mode="HTML")
	elif call.data == "cr":
	    await bot.send_message(call.from_user.id, f'Тут да')
	elif call.data == "pm":
	    await bot.send_message(call.from_user.id, f'Тут да')
	elif call.data == "ff":
	    await bot.send_message(call.from_user.id, f'Тут да')
	elif call.data == "bd":
		await bot.send_message(call.from_user.id, f'Тут да')
	if call.data == "buy_rw":
		if db.rGoldVal(call.from_user.id)[0] < abs(int(800)):
		    await bot.send_message(call.from_user.id, f'Не достаточно коинов для покупки')
		elif db.rGoldVal(call.from_user.id)[0] > abs(int(800)):
		    await bot.send_message(call.from_user.id, f'Номер заказа: 1\nОт: {call.from_user.full_name}\nЗаказ: Убрать Пред\nСтатус: Ожидание')
		    db.wGoldVal(call.from_user.id, -800)
		    global shop_send
		    buy_send = 0
		    send = len(shop_send)
		    while buy_send < send:
		        await bot.send_message(shop_send[buy_send],f'Номер заказа: 1\nОт: {call.from_user.full_name}\nЗаказ: Убрать Пред\nСтатус: Ожидание')
		        buy_send += 1
		#await bot.edit_message_text(chat_id=shop_main.chat.id, message_id=shop_main.message_id, text='Куплено!')
		# проверка является ли юзер нажавший кнопку юзером отправившим команду (защита)
		# await bot.send_message(shop_msg.chat.id, f'Simple message from: {shop_msg.from_user.username}')
			#db.wGoldVal(call.from_user.id, -1)
			#bot.edit_message_text(chat_id=shop_main.chat.id, message_id=shop_main.message_id, text='Куплено!')

@dp.message_handler(commands=['setcoin', 'set'])						
async def setcoin(message: types.Message):
    if message.chat.id in chats:
        if message.from_user.id in shop_send:
            db = DB()
            args = message.get_args()
            suid = int(message.reply_to_message.from_user.id)
            db.waGoldVal(suid, int(args))
            await message.reply("Da")
        else:
            await message.reply("У вас нет прав")
    else:
        await message.reply("Chat invalid")
	
	
@dp.message_handler(commands=['balance', 'bal', 'balancecoin'])
async def balance(message: types.Message):
	id = message.chat.id
	args = message.get_args()
	if id in chats:
		db = DB()
		try:
			suid = int(message.reply_to_message.from_user.id)
			try:
				bal = db.rGoldVal(suid)[0]
				await message.reply(f'Баланс "{message.reply_to_message.from_user.full_name}": <b>{bal}</b>', parse_mode="HTML")
			except TypeError as e:
				await message.reply(f'Баланс "{message.reply_to_message.from_user.full_name}": <b>0</b>', parse_mode="HTML")
		except AttributeError as e:
			try:
				bal = db.rGoldVal(message.from_user.id)[0]
				await message.reply(f'Ваш баланс: <b>{bal}</b>', parse_mode="HTML")
			except TypeError as e:
				await message.reply(f'Ваш баланс: <b>0</b>', parse_mode="HTML")
	else: await message.reply('Chat invalid')
@dp.message_handler(commands=['sendcoin', 'send'])
async def sendcoin(message: types.Message):
	id = message.chat.id
	args = message.get_args()
	if id in chats:
		db = DB()
		try:
			suid = int(message.reply_to_message.from_user.id)
			# ослиная моча
			if int(args) == abs(int(args)):
				if db.rGoldVal(message.from_user.id)[0] < abs(int(args)):
					print(db.rGoldVal(message.from_user.id)[0])
					await message.reply('<b>У вас нет столько DuduCoin’ов!</b>', parse_mode="HTML")
					return
				if message.from_user.id == suid:
					await message.reply('DuduCoin’ы <b>НЕЛЬЗЯ</b> передать самому себе', parse_mode="HTML")
					return
				if db.isUserExist(suid):
					db.rwGoldVal(message.from_user.id, suid, int(args))
					await message.reply(f'<b>{args}</b> DuduCoin’ов <b>успешно переданы</b> {message.reply_to_message.from_user.full_name} от {message.from_user.full_name}!', parse_mode="HTML")
				else: 
					db.createUser(suid)
					db.rwGoldVal(message.from_user.id, suid, int(args))
					await message.reply(f'<b>{args}</b> DuduCoin’ов <b>успешно переданы</b> {message.reply_to_message.from_user.full_name} от {message.from_user.full_name}!', parse_mode="HTML")
			else: await message.reply('<b>НЕЛЬЗЯ</b> передать отрицательное количество DuduCoin’ов!', parse_mode="HTML")
		except AttributeError as e:
			print(e)
			await message.reply('Команда вызывается через <b>ответ на сообщение</b>!', parse_mode="HTML")
	else: await message.reply('Chat invalid')
@dp.message_handler(commands=['getcoin', 'get'])
async def getGold(message: types.Message):
	id = message.chat.id
	xui = random.randint(0, 20)
	if id in chats:
		db = DB()
		# убери если хочешь или сделать edit message
		await message.reply('<b>Генерируем тебе DuduCoin’ы...</b>', parse_mode="HTML")
		if db.isUserExist(message.from_user.id):
			db.wGoldVal(message.from_user.id, xui)
		else:
			db.createUser(int(message.from_user.id))
			db.wGoldVal(message.from_user.id, xui)
		await message.reply(f'DuduCoin’ы <b>успешно начислены</b> в размере <b>{xui}</b> DuduCoin’ов', parse_mode="HTML")
	else: 
		await message.reply('Chat invalid')
# @dp.message_handler(commands=['getcoin'])
# async def getGold(message: types.Message):
# 	id = message.chat.id
# 	if id in chats:
# 		db = DB()
# 		if db.isUserExist(message.from_user.id):
# 			db.wGoldVal(message.from_user.id, xui)
# 		else:
# 			await message.reply(f'У вас нет DuduCoin’ов')

@dp.message_handler(commands=['botinf'])
async def binf(message: types.Message):
	fm = message.from_user.id
	fm = str(fm)
	name = message.from_user.username
	name = str(name)
	print("\n/botinf command user from: " + fm + " nickname: " + name)
	await message.answer('<b>Fukk Sleep Bot INFO\nЯзык написания: Python\nКодер:</b> <a href = "t.me/neol1tic"><b>neol1tic</b></a>, <a href = "t.me/drpxqq"><b>drpxqq</b></a>\n<b>Помощники:</b> <a href = "t.me/droonka1"><b>droonka1</b></a>, <a href = "t.me/hataB1ch"><b>hataB1ch</b></a>\n<b>Основание: 28.06.22</b>', disable_web_page_preview = True, parse_mode="HTML")
@dp.message_handler(commands=['coin'])
async def coin(message: types.Message):
	if timediff(5.0):
		fm = message.from_user.id
		fm = str(fm)
		name = message.from_user.username
		name = str(name)
		print("\n/coin command user from: " + fm + " nickname: " + name)
		id = message.chat.id
		if id in chats:
			global wait
			if wait == 0:
				global mess
				global coin_msg
				coin_msg = message
				mess = message.message_id + 1
				button_1 = types.InlineKeyboardButton('Орёл' , callback_data = '1')
				button_2 = types.InlineKeyboardButton('Решка',callback_data = '2')
				keyboard = types.InlineKeyboardMarkup()
				keyboard.add(button_1)
				keyboard.add(button_2)
				await message.answer('<b>Игра Орёл или Решка!\nВыбери свою ставку</b>', reply_markup=keyboard, parse_mode="HTML")
				wait = 1
				return mess, wait
			else:
				await message.answer('Прошлая игра не закончена\nЕсли игра залагала напишите /creload')
		else:
			await message.answer('Chat invalid')
	else: await message.reply('Эу даун щас кулдаун')
@dp.callback_query_handler(lambda call: True)
async def coin_sys(call: types.CallbackQuery):
	if call.data == "1" or "2":
				global wait
				global coin_msg
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
				    await bot.edit_message_text(chat_id=coin_msg.chat.id, message_id=mess, text ="@" + str(pon)+ " Выпал " + str(lose) + " вы выиграли\nВаша ставка: " + str(use))
				    await bot.answer_callback_query(callback_query_id=call.id, text='А вы сегодня везучий!')
				    wait = 0
				    return wait
				else:
				   await bot.edit_message_text(chat_id=coin_msg.chat.id, message_id=mess, text ="@" + str(pon) +" Выпал " + str(lose) + " вы проиграли\nВаша ставка: " + str(use))
				   await bot.answer_callback_query(callback_query_id=call.id, text='Повезёт в следующий раз :(')
				   wait = 0
				   return wait
@dp.message_handler(commands=['creload'])
async def creload(message: types.Message):
	fm = message.from_user.id
	fm = str(fm)
	name = message.from_user.username
	name = str(name)
	print("\n/creload command user from: " + fm + " nickname: " + name)
	id = message.chat.id
	if id in chats:
		await message.send_message('Игра перезапущена!')
		global wait
		wait = 0
		return wait
	else:
		await message.answer('Chat invalid')
	
@dp.message_handler(commands=['socmedia'])
async def socmedia(message: types.Message):
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
		await message.answer('<b>Соц-сети elizzi:</b>', reply_markup=keyboard, parse_mode="HTML")
	else:
		await message.answer('Chat invalid')
	
@dp.message_handler(commands=['ping'])
async def ping(message: types.Message):
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
					await message.answer(info)
					DataPing.close()
					sys.stdout = temp
			except:
				await message.answer('Пинг : Error')
			else:
				sys.stdout = temp
				print("\n/ping command user from: " + fm + " nickname: " + name)
				sys.stdout = temp
		else:
			await message.answer('Chat invalid')
	else:
			await message.answer('Не достаточно прав')
			

@dp.message_handler(commands=['pon'])
async def fun(message: types.Message):
	if timediff(10.0) == True:
		global inf_mes
		fm = message.from_user.id
		fm = str(fm)
		name = message.from_user.username
		name = str(name)
		inf_mes += 1
		print("\n/pon command user from: " + fm + " nickname: " + name)
		id = message.chat.id
		if id in chats:
			if random.randint(0, 18) == 1:
				await message.answer('Вы можете так же прислать\nмемы нам, если\nхотите, что бы их\nдобавили в бота\n👇🏻👇🏻👇🏻\nt.me/neol1tic\nt.me/droonka1', disable_web_page_preview = True)
				inf_mes = 0
			media = random.randint(1,3)
			if media == 1:
				folder = 'media/photo/'
				files = os.listdir(folder)
				file = random.choice(files)
				meme_p = folder + file
				await message.answer_photo(photo=open(meme_p, 'rb'))
			elif media == 2:
				folder = 'media/gif/'
				files = os.listdir(folder)
				file = random.choice(files)
				meme_g = folder + file
				await message.answer_document(document=open(meme_g,'rb'))
			else:
				folder = 'media/video/'
				files = os.listdir(folder)
				file = random.choice(files)
				meme_v = folder + file
				await message.answer_video(video=open(meme_v, 'rb'))
		else:
			await message.answer('Chat invalid')
	else: await message.reply('Эу даун щас кулдаун')
@dp.message_handler(commands=['start'])
async def start (message: types.Message):
	name = message.from_user.username
	date =  datetime.datetime.now().hour
	morning = [6,7,8,9,10,11]
	day = [12,13,14,15,16,17]
	subnight = [18,19,20,21,22,23]
	night = [0,1,2,3,4,5]
	if date in morning:
		await message.answer('👋 • Доброе утро, @' + name +'.\n\n🧑🏻‍💼 • Я вспомогательный бот для Fukk Sleep Chat. Пиши команду ниже, что бы узнать список моих команд.\n\n/support_help')
	elif date in day:
		await message.answer('👋 • Добрый день, @' + str(name)+'.\n\n🧑🏻‍💼 • Я вспомогательный бот для Fukk Sleep Chat. Пиши команду ниже, что бы узнать список моих команд.\n\n/support_help')
	elif date in subnight:
		await message.answer('👋 • Добрый вечер, @' + str(name)+'.\n\n🧑🏻‍💼 • Я вспомогательный бот для Fukk Sleep Chat. Пиши команду ниже, что бы узнать список моих команд.\n\n/support_help')
	elif date in night:
		await message.answer('👋 • Доброй ночи, @' + str(name)+'.\n\n🧑🏻‍💼 • Я вспомогательный бот для Fukk Sleep Chat. Пиши команду ниже, что бы узнать список моих команд.\n\n/support_help')
	else:
		await message.answer('👋 • Здравствуйте, @' + str(name)+'.\n\n🧑🏻‍💼 • Я вспомогательный бот для Fukk Sleep Chat. Пиши команду ниже, что бы узнать список моих команд.\n\n/support_help')
		
@dp.message_handler(commands=['anekdot'])
async def anekdot(message):
	fm = message.from_user.id
	fm = str(fm)
	name = message.from_user.username
	name = str(name)
	print("\n/anekdot command user from: " + fm + " nickname: " + name)
	id = message.chat.id
	if id in chats:
		rofl = random.choice(anekdots.anekdots)
		await message.answer(rofl)
	else:
		await message.answer('Chat invalid')
@dp.message_handler(commands=['cm'])
async def gm(message: types.Message):
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
			await message.answer("Console mode activate")
			print("                   Console mode activate\n")
			while console:
				mess = input(">>> ")
				if mess == 'c.off':
					console = False
					print("                    Console mode off\n")
					await message.answer("Console mode off")
				else:
					await message.answer(mess)
		else:
			await message.answer('Не достаточно прав')
	else:
		await message.answer('Chat invalid')
@dp.message_handler(commands=['support_help'])
async def help(message: types.Message):
	fm = message.from_user.id
	fm = str(fm)
	name = message.from_user.username
	name = str(name)
	print("\n/help command user from: " + fm + " nickname: " + name)
	id = message.chat.id
	if id in chats or 1: await message.answer("Мои команды:\n/support_help - Команды\n/ruled - Отправка правил\n/sap - Проверка работы\n/mod - Проверка пользователя на модератора\n/report - Подать жалобу на сообщение\n/cm - Включить консоль мод\n/test - Проверить чат\n/anekdot - Рандомный анекдот\n/start - Приветствие бота\n/pon - Рандомный мем\n/ping - Задержка бота\n/socmedia - Соц.сети Элиззи\n/coin - Орёл или Решка?\n/botinf - Создатели")
	else:
		await message.answer('Chat invalid')
	

@dp.message_handler(commands=['ruled'])
async def rules(message: types.Message):
	fm = message.from_user.id
	fm = str(fm)
	name = message.from_user.username
	name = str(name)
	print("\n/ruled command user from: " + fm + " nickname: " + name)
	check = message.from_user.id
	id = message.chat.id
	if id in chats:
		if check in staff:
				await message.answer("📚 Правила чата:\n@fukksleeppravila\n@fukksleeppravila\n@fukksleeppravila")
		else:
			await message.answer("Недостаточно прав")
	else:
		await message.answer('Chat invalid')

@dp.message_handler(commands=['sap'])
async def ping(message: types.Message):
	fm = message.from_user.id
	fm = str(fm)
	name = message.from_user.username
	name = str(name)
	print("\n/sap command user from: " + fm + " nickname: " + name)
	id = message.chat.id
	if id in chats:
		await message.answer("✅️ Работаю!")
	else:
		await message.answer('Chat invalid')
@dp.message_handler(commands=['mod'])
async def mod(message: types.Message):
	fm = message.from_user.id
	name = message.from_user.username
	name = str(name)
	print("\n/mod command user from: " + str(fm) + " nickname: " + name)
	if fm in staff:
		await message.answer("✅️ Пользователь найден в датабазе как модератор")
	else:
		await message.answer("✅️ Пользователь найден в датабазе как обычный учасник")
					 

@dp.message_handler(commands=['test'])
async def test(message: types.Message):
	fm = message.from_user.id
	fm = str(fm)
	name = message.from_user.username
	name = str(name)
	print("\n/test command user from: " + fm + " nickname: " + name)
	id = message.chat.id
	if id in chats:
		await message.answer('Chat valid')
	else:
		await message.answer('Chat invalid')
		
@dp.message_handler(commands=['report'])
async def report(message: types.Message):
	fm = message.from_user.id
	name = message.from_user.username
	name = str(name)
	print("\n/report command user from: " + str(fm) + " nickname: " + name)
	mlink = message.message_id
	mlink = str(mlink)
	report = message.text
	report = str(report)
	id = message.chat.id
	if id in chats:
		rep = len(staff)
		send = 0
		while send < rep:
			await bot.send_message(staff[send],'REPORT DETECTED\nMESSAGE = .' + "https://t.me/c/1726091917/" + mlink+ "\nREPORT:\n" + report)
			send += 1
		await message.answer('📛 Жалоба на сообщение отправлена модерации.\n\nУчтите! За репорт без причины выдаётся наказание.')
	else:
		await message.answer('📛 Жалоба не отправлена\nЧат не прошел проверку') 
#RUN
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)