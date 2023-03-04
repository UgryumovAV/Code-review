from aiogram.types import ReplyKeyboardMarkup, KeyboardButton  # ReplyKeyboardRemove - для удаления клавиатуры


b1 = KeyboardButton(text='/start')
b2 = KeyboardButton(text='/Меню')
b3 = KeyboardButton(text='/Руководители')

b4 = KeyboardButton(text='/Расписание')
b5 = KeyboardButton(text='/Домашки')
b6 = KeyboardButton(text='/Материалы')
b7 = KeyboardButton(text='/Назад')

b8 = KeyboardButton(text='/SQL_3')
b9 = KeyboardButton(text='/Log_4_1')
b10 = KeyboardButton(text='/Data_prep_4_2')
b11 = KeyboardButton(text='/Stat_5')
b12 = KeyboardButton(text='/Classic_CV_6')
b13 = KeyboardButton(text='/PyTorch_7')
b14 = KeyboardButton(text='/Rep_8')


kb_client = ReplyKeyboardMarkup(resize_keyboard=True,
                                )  # one_time_keyboard=True - после действия прячет клаву
kb_client_2 = ReplyKeyboardMarkup(resize_keyboard=True,
                                )
kb_client_3 = ReplyKeyboardMarkup(resize_keyboard=True,
                                )
kb_client.add(b1).add(b2).insert(b3)  # .b2 итд, kb_client.row(b1, b2, b3) - всё в строку

kb_client_2.add(b4).insert(b5).add(b6).insert(b7)

kb_client_3.row(b8, b9, b10).row(b11, b12, b13).row(b14).add(b7)
