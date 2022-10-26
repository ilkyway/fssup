import config
import emoji
from aiogram import types
from dbmanager import DB
from markup.markup import Keyboards
class Handler:
    def __init__(self, bot):
        self.markup = None
        self.db = DB()
        self.bot = bot
        self.historyb = Keyboards().shop_menu()
        self.historytxt = '<b>МАГАЗИН</b>'
        self.staff = [5168812451,1464608585,1182584762,1823185825,1671426989,5523810980,5720844448,1880824191,848638523,
                 1040763170]
        self.chats = [-1001726091917,-1001703603450]
        self.shop_send = [1880824191,848638523,5720844448,1040763170]
    # async def invoice_sender(self, ):
    async def handle(self, call, chatid):
        keys = Keyboards()
        if call.data == "rw":
            await self.bot.send_message(chatid, f'Хотите купить "Снятие преда" за <b>800 DuDuCoin’ов?</b>', reply_markup=keys.buy_warn(), parse_mode="HTML")
        elif call.data == "cancel":
            await self.bot.send_message(chatid, self.historytxt, reply_markup=self.historyb, parse_mode="HTML")
        elif call.data == "cr":
            await self.bot.send_message(chatid,
                                   f'Выберите среди вариантов ниже:\nКаст. роль на 1 месяц - <b>3500 DuDuCoin’ов</b>\nКаст. роль 3 месяца - <b>9000 DuDuCoin’ов</b>',
                                   reply_markup=keys.buy_role_variants(),parse_mode="HTML")
        elif call.data == "ch_cr1":
            await self.bot.send_message(chatid,f'Хотите купить "Каст. роль на 1 месяц" за <b>3500 DuDuCoin’ов?</b>',
                                   reply_markup=keys.buy_role_1m(),parse_mode="HTML")
        elif call.data == "ch_cr3":
            await self.bot.send_message(chatid,f'Хотите купить "Каст. роль на 3 месяцa" за <b>9000 DuDuCoin’ов?</b>',
                                   reply_markup=keys.buy_role_3m(),parse_mode="HTML")
        elif call.data == "buy_cr1":
            if self.db.rGoldVal(chatid)[0] < 3500:
                await self.bot.send_message(chatid,f'Не достаточно коинов для покупки')
            else:
                await self.bot.send_message(chatid,
                                       f'Номер заказа: 1\nОт: {call.from_user.full_name}\nЗаказ: Каст. роль 1м\nСтатус: Ожидание')
                self.db.wGoldVal(chatid,-3500)
                buy_send = 0
                while buy_send < len(self.shop_send):
                    await self.bot.send_message(self.shop_send[buy_send],
                                           f'Номер заказа: 1\nОт: {call.from_user.full_name}\nЗаказ: Каст. роль 1м\nСтатус: Ожидание')
                    buy_send += 1
        elif call.data == "pm":
            await self.bot.send_message(chatid,
                                   f'Выберите среди вариантов ниже:\nЗакреп. сообщения на на 1 день - <b>5000 DuDuCoin’ов</b>\nЗакреп. сообщения на на 7 день - <b>12000 DuDuCoin’ов</b>',
                                   reply_markup=keys.buy_pin_variants(),parse_mode="HTML")
        elif call.data == "bd":
            await self.bot.send_message(chatid,
                                        f'Выберите среди вариантов ниже: \n5000 DuduCoin’ов\n10000 DuduCoin’ов\n20000 DuduCoin’ов\n',
                                        reply_markup=keys.buy_coin_for_money(),parse_mode="HTML")
        elif call.data == '1000_coins' or call.data == '2500_coins' or call.data == '5000_coins' or call.data == '10000_coins' or call.data == '20000_coins':
            amount = int(call.data.split('_')[0])
            if amount == 1000:
                await self.bot.send_invoice(chat_id=chatid,
                                            title='Покупка DuduCoin’ов',
                                            description='КУПИ ДУДУКОИНЫ \n\n\n купи дудукоины сука',
                                            provider_token="381764678:TEST:43755",
                                            currency='rub',
                                            is_flexible=False,
                                            prices=[types.labeled_price.LabeledPrice('Цена', 3000)],
                                            payload='payload_1000')
            elif amount == 2500:
                await self.bot.send_invoice(chat_id=chatid,
                                            title='Покупка DuduCoin’ов',
                                            description='КУПИ ДУДУКОИНЫ \n\n\n купи дудукоины сука',
                                            provider_token="381764678:TEST:43755",
                                            currency='rub',
                                            is_flexible=False,
                                            prices=[types.labeled_price.LabeledPrice('Цена', 5000)],
                                            payload='payload_2500')
            elif amount == 5000:
                await self.bot.send_invoice(chat_id=chatid,
                                            title='Покупка DuduCoin’ов',
                                            description='КУПИ ДУДУКОИНЫ \n\n\n купи дудукоины сука',
                                            provider_token="381764678:TEST:43755",
                                            currency='rub',
                                            is_flexible=False,
                                            prices=[types.labeled_price.LabeledPrice('Цена', 8000)],
                                            payload='payload_5000')
            elif amount == 10000:
                await self.bot.send_invoice(chat_id=chatid,
                                            title='Покупка DuduCoin’ов',
                                            description='КУПИ ДУДУКОИНЫ \n\n\n купи дудукоины сука',
                                            provider_token="381764678:TEST:43755",
                                            currency='rub',
                                            is_flexible=False,
                                            prices=[types.labeled_price.LabeledPrice('Цена', 14000)],
                                            payload='payload_10000')
            elif amount == 20000:
                await self.bot.send_invoice(chat_id=chatid,
                                            title='Покупка DuduCoin’ов',
                                            description='КУПИ ДУДУКОИНЫ \n\n\n купи дудукоины сука',
                                            provider_token="381764678:TEST:43755",
                                            currency='rub',
                                            is_flexible=False,
                                            prices=[types.labeled_price.LabeledPrice('Цена', 25000)],
                                            payload='payload_20000')
        if call.data == "buy_rw":
            if self.db.rGoldVal(chatid)[0] < abs(int(800)):
                await self.bot.send_message(chatid,f'Не достаточно коинов для покупки')
            else:
                await self.bot.send_message(chatid,
                    f'Номер заказа: 1\nОт: {call.from_user.full_name}\nЗаказ: Убрать Пред\nСтатус: Ожидание')
                self.db.wGoldVal(chatid,-800)
                buy_send = 0
                send = len(self.shop_send)
                while buy_send < send:
                    await self.bot.send_message(self.shop_send[buy_send],
                                           f'Номер заказа: 1\nОт: {call.from_user.full_name}\nЗаказ: Убрать Пред\nСтатус: Ожидание\n Айди: {call.from_user.id}')
                    buy_send += 1
        elif call.data == "buy_pm7":
            if self.db.rGoldVal(chatid)[0] < abs(int(12000)):
                await self.bot.send_message(chatid,f'Не достаточно коинов для покупки')
            else:
                await self.bot.send_message(chatid,
                                       f'Номер заказа: 1\nОт: {call.from_user.full_name}\nЗаказ: Закреп. сообщения на 7д\nСтатус: Ожидание')
                self.db.wGoldVal(chatid,-12000)
                buy_send = 0
                send = len(self.shop_send)
                while buy_send < send:
                    await self.bot.send_message(self.shop_send[buy_send],
                                           f'Номер заказа: 1\nОт: {call.from_user.full_name}\nЗаказ: Закреп. сообщения на 7д\nСтатус: Ожидание')
                    buy_send += 1
        elif call.data == "buy_ff":
            if self.db.rGoldVal(chatid)[0] < abs(int(15000)):
                await self.bot.send_message(chatid,f'Не достаточно коинов для покупки')
            else:
                await self.bot.send_message(chatid,
                                       f'Номер заказа: 1\nОт: {call.from_user.full_name}\nЗаказ: Минус N часов к кулдауну\nСтатус: Ожидание')
                self.db.wGoldVal(chatid,-15000)
                buy_send = 0
                send = len(self.shop_send)
                while buy_send < send:
                    await self.bot.send_message(self.shop_send[buy_send],
                                           f'Номер заказа: 1\nОт: {call.from_user.full_name}\nЗаказ: Минус N часов к кулдауну\nСтатус: Ожидание')
                    buy_send += 1
        elif call.data == "ff":
            await self.bot.send_message(chatid,
                                   f'Хотите купить "Минус N часов к кулдауну" за <b>15000 DuDuCoin’ов?</b>',
                                   reply_markup=keys.buy_cooldown(),parse_mode="HTML")
        elif call.data == "buy_cr3":
            if self.db.rGoldVal(chatid)[0] < 9000:
                await self.bot.send_message(chatid,f'Не достаточно коинов для покупки')
            else:
                await self.bot.send_message(chatid,
                                       f'Номер заказа: 1\nОт: {call.from_user.full_name}\nЗаказ: Каст. роль 3м\nСтатус: Ожидание')
                self.db.wGoldVal(chatid,-9000)
                buy_send = 0
                while buy_send < len(self.shop_send):
                    await self.bot.send_message(self.shop_send[buy_send],
                                           f'Номер заказа: 1\nОт: {call.from_user.full_name}\nЗаказ: Каст. роль 3м\nСтатус: Ожидание')
                    buy_send += 1
