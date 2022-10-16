import config
import emoji
from aiogram import executor, types
from dbmanager import DB
class Keyboards:
    def __init__(self):
        self.markup = None
        self.DB = DB()

    def set_btn(self,name,step=0,quantity=0):
        return types.InlineKeyboardButton(config.KEYBOARD[name]['name'], callback_data=config.KEYBOARD[name]['callback_data'])