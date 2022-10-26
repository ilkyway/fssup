import config
import emoji
from aiogram import executor, types
from dbmanager import DB
class Keyboards:
    def __init__(self):
        self.markup = None

    def set_btn(self,name):
        return types.InlineKeyboardButton(config.KEYBOARD[name]['name'], callback_data=config.KEYBOARD[name]['callback_data'])
    def shop_menu(self):
        self.markup = types.InlineKeyboardMarkup()
        self.markup.add(self.set_btn('REMOVE_WARN'))
        self.markup.add(self.set_btn('CUSTOM_ROLE'))
        self.markup.add(self.set_btn('PIN_MESSAGE'))
        self.markup.add(self.set_btn('FAST_FARM'))
        self.markup.add(self.set_btn('COIN'))
        return self.markup
    def buy_warn(self):
        self.markup = types.InlineKeyboardMarkup()
        self.markup.add(self.set_btn('BUY_WARN'))
        # self.markup.add(self.set_btn('NO_WARN'))
        self.markup.add(self.set_btn('CANCEL'))
        return self.markup
    def buy_role_variants(self):
        self.markup = types.InlineKeyboardMarkup()
        self.markup.add(self.set_btn('CUSTOM_ROLE_1M'))
        self.markup.add(self.set_btn('CUSTOM_ROLE_3M'))
        self.markup.add(self.set_btn('CANCEL'))
        return self.markup
    def buy_role_1m(self):
        self.markup = types.InlineKeyboardMarkup()
        self.markup.add(self.set_btn('CONFIRM_CUSTOM_ROLE_1M_YES'))
        self.markup.add(self.set_btn('CONFIRM_CUSTOM_ROLE_1M_NO'))
        self.markup.add(self.set_btn('CANCEL'))
        return self.markup
    def buy_role_3m(self):
        self.markup = types.InlineKeyboardMarkup()
        self.markup.add(self.set_btn('CONFIRM_CUSTOM_ROLE_3M_YES'))
        self.markup.add(self.set_btn('CONFIRM_CUSTOM_ROLE_3M_NO'))
        self.markup.add(self.set_btn('CANCEL'))
        return self.markup
    def buy_pin_variants(self):
        self.markup = types.InlineKeyboardMarkup()
        self.markup.add(self.set_btn('PIN_1D'))
        self.markup.add(self.set_btn('PIN_7D'))
        self.markup.add(self.set_btn('CANCEL'))
        return self.markup
    def buy_coins(self):
        self.markup = types.InlineKeyboardMarkup()
        self.markup.add(self.set_btn('BUY_COIN_MONEY'))
        self.markup.add(self.set_btn('CANCEL'))
        return self.markup
    def buy_coin_for_money(self):
        self.markup = types.InlineKeyboardMarkup()
        # self.markup.add(self.set_btn('BUY_1000_COIN'))
        # self.markup.add(self.set_btn('BUY_2500_COIN'))
        self.markup.add(self.set_btn('BUY_5000_COIN'))
        self.markup.add(self.set_btn('BUY_10000_COIN'))
        self.markup.add(self.set_btn('BUY_20000_COIN'))
        self.markup.add(self.set_btn('CANCEL'))
        return self.markup
    def buy_cooldown(self):
        self.markup = types.InlineKeyboardMarkup()
        self.markup.add(self.set_btn('BUY_FAST_FARM'))
        self.markup.add(self.set_btn('CANCEL'))
        return self.markup
