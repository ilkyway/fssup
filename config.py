import emoji
TOKEN = "5670214636:AAEaog136vWGrsT7Zy1P5h5vbux43HJDLyU"

KEYBOARD = {"DELETE_PRED": {"name": "Убрать Пред", "callback_data": 'rw'},
            "CUSTOM_ROLE": {"name": "Каст. роль","callback_data": 'cr'},
            "PIN_MESSAGE": {"name": "Закреп. сообщения","callback_data": 'pm'},
            "INC_COOLDOWN": {"name": "Уменьшить КД","callback_data": 'ff'},
            "BUY_COIN": {"name": "Купить Duducoin","callback_data": 'bd'},
            "BUY": {"name": "Купить","callback_data": 'buy_rw'},
            "NO": {"name": "Нет","callback_data": 'no_rw'}}