from aiogram.utils import executor
from create_bot import dp
from handlers import client, admin, other

import os, json, string


async def on_starup(_):
    #выполняется при выходе бота в онлайн
    print('Бот вышел в онлайн')


client.register_handlers_client(dp)
other.register_handlers_other(dp)

executor.start_polling(dp, skip_updates=True, on_startup=on_starup)
