from aiogram import types, Dispatcher
from create_bot import bot, dp

import json, string


# @dp.message_handler()
async def cenz_filter(message: types.message):
    if {i.lower().translate(str.maketrans('', '', string.punctuation))
        for i in message.text.split(' ')}\
            .intersection(set(json.load(open('data/cenz.json')))) != set():
        await message.reply('!$&*;%№')
        await message.delete()


def register_handlers_other(dp: Dispatcher):
    dp.register_message_handler(cenz_filter)
