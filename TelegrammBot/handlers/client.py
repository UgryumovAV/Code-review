from aiogram import types, Dispatcher
from create_bot import bot, dp
from keyboards import kb_client, kb_client_2, kb_client_3
from aiogram.types import ReplyKeyboardRemove


# @dp.message_handler(commands=['start', 'help']) - если писать однофайлового бота
# Старт
async def command_start(message: types.message):
    try:
        await bot.send_message(message.from_user.id,
                               'Привет, этот бот собирает в себе все необходимые '
                               'ссылки на учебные материалы',
                               reply_markup=kb_client)
        await message.delete()
    except:
        await message.reply('Общение с ботом через личные сообщения, напишите ему первым:'
                            '\nhttps://t.me/shift_cft_cv_2023_bot')


# Меню
async def command_menu(message: types.message):
    await bot.send_message(message.from_user.id,
                           'Меню',
                           reply_markup=kb_client_2)
    await message.delete()


# Назад
async def command_back(message: types.message):
    await bot.send_message(message.from_user.id,
                           'Назад',
                           reply_markup=kb_client)
    await message.delete()


# Домашки
async def command_domashki(message: types.message):
    await bot.send_message(message.from_user.id,
                           'Домашки',
                           reply_markup=kb_client_3)
    await message.delete()


# SQL_3
async def command_3_SQL(message: types.message):
    await bot.send_message(message.from_user.id,
                           'SQL_3\n'
                           '\n'
                           '1) Установить PostgreSQL;\n'
                           '2) Создать БД home_credit, исследовать данные, '
                           'определить типы данных и загрузить все таблицы. '
                           'SQL запросы указать либо в ноутбуке, либо отдельными файлами;\n'
                           '3) Сделать упражнения по запросам ниже;\n'
                           '4) Сгенерировать 5 своих признаков для будущего обучения модели;\n'
                           '5) Реализовать их насчет используя ТОЛЬКО SQL-запросы.\n'
                           '\n'
                           'Результат:\n1) Настроенная СУБД с загруженными данными из конкурса'
                           ' Home_Credit;\n2) Сделанные упражнения с выводом данных как в примерах'
                           ' выше;\n3) Описание в ноутбуке 5 сгенерированных признаков;\n'
                           '4) Реализованные в ноутбуке SQL-запросы к базе данных с выводом '
                           'результата по вышеуказанным фичам;\n5) Файл конфигурации в папке '
                           'config, где прописаны параметры коннекта к БД;\n'
                           '6) Папка utils в репозиторий, созданный там скрипт с кодом '
                           'позволяющим обращаться к БД;\n'
                           '\n'
                           '"Бонусные" задания:\n'
                           '1) Сделать класс для операций с БД вместо функций;\n'
                           '2) Проанализировать структуру, назначить в таблицах ключи и '
                           'индексы запросами к БД.\n'
                           '\n'
                           'Руководитель:\n'
                           'Лагуткин Евгений Александрович\n'
                           'e.lagutkin@cft.ru\n'
                           '\n'
                           'Материалы:\n'
                           'https://cloud.mail.ru/public/zy8S/antGvHGTD\n'
                           '\n'
                           'Дедлайн - 14.02',
                           )
    await message.delete()


# Log_4_1
async def command_Log_4_1(message: types.message):
    await bot.send_message(message.from_user.id,
                           'Log_4_1\n'
                           '\n'
                           'Из данных по Home Credit Default Risk | Kaggle было взято 2 файла:\n\n'
                           'POS_CASH_balance.csv\nbureau.csv\n\n'
                           'Из этих двух файлов был составлен один .log файл.\n'
                           'Ссылка на этот .log файл https://drive.google.com/file/d/10B7SLnND'
                           '1k9D3SFZ7Vyno2U33RSOFddq/view?usp=sharing\n\nИспользуя его, а также'
                           ' описание схемы данных из ноутбука, необходимо написать скрипт, на в'
                           'ыходе которого получается два .csv файла, идентичных по наполнению фа'
                           'йлам из Home Credit Default Risk.\nСкрипт должен быть в виде .py фай'
                           'ла\nСоздайте в репозитории папку src/hw_31 и скрипт поместите в нее ('
                           'в отдельной ветке)\nСделайте Merge request этой ветки в мастер, рев'
                           'ьюером тагните @focus-start-ml\nВ МРе, комментарием, укажите приме'
                           'рное время выполнения.\n\nКритерии к ДЗ, схемы данных - смотрит'
                           'е в ноутбуке log_parsing_notebook.ipynb\nКому интересно потыкать '
                           'ячейки из ноутбука - папка с файлами из лекции вот \nhttps://drive.goog'
                           'le.com/drive/folders/1W7u8xBWPtZp6uM23pbo0ypHOPrNd-ImW?usp=sharing\n'
                           '\n'
                           'Руководитель:\n'
                           'Ачоян Артур Араратович\n'
                           'a.achojan@cft.ru\n'
                           '\n'
                           'Материалы:\n'
                           'https://cloud.mail.ru/public/HM93/rZs614VbH\n'
                           '\n'
                           'Дедлайн - 16.02',
                           )
    await message.delete()


# Data_prep_4_2
async def command_Data_prep_4_2(message: types.message):
    await bot.send_message(message.from_user.id,
                           'Data_prep_4_2\n'
                           '\n'
                           'Нужно сделать:\nПровести разведочный анализ: describe(), '
                           'кол-во пропусков, выбросов, построить boxplot и тп.\nЗаполнить'
                           '(удалить) пропуски, заменить(удалить) выбросы, кратко аргумент'
                           'ировать замены.\nПолучить датафрейм с качественными данными\n\nДат'
                           'асет для домашки HomeWork.csv\nНоутбук с кодом выкладываем в GitLa'
                           'b, в папку src/hw_32, точно так же в виде merge request`а, тагайте '
                           '@focus-start-ml\nНоутбук с лекции FocusStart_Encoders.ipynb\nsales3.'
                           'csv - датафрейм для примера, чтобы ноутбук воспроизвести\n'
                           '\n'
                           'Руководитель:\n'
                           'Ахметов Данияр Маратович\n'
                           'd.akhmetov@cft.ru\n'
                           '\n'
                           'Материалы:\n'
                           'https://cloud.mail.ru/public/HM93/rZs614VbH\n'
                           '\n'
                           'Дедлайн - 16.02',
                           )
    await message.delete()


# Stat_5
async def command_Stat_5(message: types.message):
    await bot.send_message(message.from_user.id,
                           'Stat_5\n'
                           '\n'
                           'Что сделать?\nНаписать скрипт(ы) по проверке признаков '
                           '(любым из способов, озвученных на лекции, можно использовать '
                           'комбинации, можно дополнить чем-то своим) по разли'
                           'чным датасетам из конкурса.\n\nОдин датасет - один скрипт:'
                           '\na. POS_CASH_balance.csv - по желание если останется время\nb. app'
                           'lication_test.csv\nc. application_train.csv\nd. bureau.csv\ne. bur'
                           'eau_balance.csv\nf. credit_card_balance.csv\ng. installments_pay'
                           'ments.csv\nh. previous_application.csv\n\nОбщие требования (упоряд'
                           'очены в порядки убывания важности):\n\na. Скрипт загружен в GitLab, сд'
                           'елан МР с изменениями, предоставлена ссылка на МР\nb. Код является'
                           ' воспроизводимым\nc. Результатом работы каждого скрипта являет'
                           'ся csv файл со значимыми признаками.\nd. Приемлемое время выполн'
                           'ения скрипта.\ne. Скрипт содержит функцию main(), при вызове которой '
                           'выполняется загрузка уже насчитанных признаков и проверка признаков. '
                           'При этом, должна быть реализована возможность задания следующих параметр'
                           'ов:\n\ni. Путь к входному файлу\nii. Путь к результирующему .csv файлу'
                           '\n\nf. Структура и качество кода:\n\ni. Выделение отдельных логических час'
                           'тей в виде функций\nii. Вынесение общей логики в отдельные функции с целью'
                           ' переиспользования\niii. Документирование кода\niv. Осмысленные имена п'
                           'еременных\n'
                           '\n'
                           'Руководитель:\n'
                           'Сергеева София Анатольевна\n'
                           'so.sergeeva@cft.ru\n'
                           '\n'
                           'Материалы:\n'
                           'https://cloud.mail.ru/public/fjtC/BoUEWsTj2\n'
                           'Таблицы csv:\n'
                           'https://cloud.mail.ru/public/Ryfk/HPTnVKdRf\n'
                           '\n'
                           'Дедлайн - 22.02',
                           )
    await message.delete()


# Материалы
async def command_materials(message: types.message):
    await bot.send_message(message.from_user.id,
                           '20230202 занятие 1 общее\n'
                           'https://cloud.mail.ru/public/PSSG/3iEHVgHoP\n'
                           '\n'
                           '20230204 занятие 2 git\n'
                           'https://cloud.mail.ru/public/4bZU/TK3pf5ctb\n'
                           '\n'
                           '20230207 занятие 3 SQL и данные\n'
                           'https://cloud.mail.ru/public/zy8S/antGvHGTD\n'
                           '\n'
                           '20230209 занятие 4 json logs парсинг\n'
                           'https://cloud.mail.ru/public/HM93/rZs614VbH\n'
                           '\n'
                           '20230211 занятие 5 общая CV\n'
                           'https://cloud.mail.ru/public/UnuP/aSDNP29nX\n'
                           '\n'
                           '20230213 занятие 6 адаптация на рабочем месте\n'
                           'https://cloud.mail.ru/public/2jXR/M3dVGHTZB\n'
                           '\n'
                           '20230214 занятие 7 стат бутстрап динамика\n'
                           'https://cloud.mail.ru/public/fjtC/BoUEWsTj2\n'
                           '\n',
                           )
    await message.delete()


# Расписание
async def command_sched(message: types.message):
    await bot.send_message(message.from_user.id,
                           '01.02.2023 среда \n19:00 - 20:30 \nОрг. собрание\n'
                           '\n'
                           '02.02.2023 четверг \n19:00 - 21:00 \nВводное занятие. '
                           'Обзор ML проектов в ЦФТ.\n'
                           '\n'
                           '04.02.2023 суббота \n12:00 - 14:00 \nMS Teams канал \nОбщий_ML_CV-2023-1\n'
                           'Обзор инструментов, которые пригодятся в курсе. '
                           'Gitlab настройка репозитория,IDE, linter. '
                           '\n'
                           '07.02.2023 вторник \n19:00 - 21:00 \nMS Teams канал \nОбщий_ML_CV-2023-1 '
                           '\nРабота с sql подобными базами.Как поднять базу.Синтаксис запросов.'
                           'Основные команды.\n'
                           '\n'
                           '09.02.2023 четверг \n19:00 - 21:00 \nMS Teams канал \nОбщий_ML_CV-2023-1 \n'
                           'Обработка данных. Парсинг логов, json, примеры парсинга объектов. '
                           'Обработка данных для моделей (ohe, le, обработка признаков, '
                           'удаление выбросов, заполнение пропусков).\n'
                           '\n'
                           '11.02.2023 суббота \n14:00 - 16:00 \n'
                           'Обзорная лекция Computer Vision.\n'
                           '\n'
                           '13.02.2023 понедельник \n19:00 - 20:30 \nMS Teams канал \n'
                           'Общий_ML_CV-2023-1 \n'
                           'Лекция от HR-куратора \nАдаптация на новом рабочем месте.\n'
                           '\n'
                           '14.02.2023 вторник \n19:00 - 21:00 \nMS Teams канал \n'
                           'Общий_ML_CV-2023-1 \nПроверка стат. гипотез, бутстрап, '
                           'динамика распределения признаков во времени.\n'
                           '\n'
                           '16.02.2023 четверг \n19:00 - 21:00 \nКлассика CV. \n'
                           'Домашнее задание \nДедлайн 23.02.2023\n'
                           '\n'
                           '18.02.2023 суббота \n12:00 - 14:00 \nMS Teams канал \n'
                           'Общий_ML_CV-2023-1 \nСхемы кроссвалидаций. \n'
                           'Оценка качества моделей, метрики (Accuracy, precision, '
                           'recall, f1, ROC AUC, MSE, RMSE).\n'
                           '\n'
                           '21.02.2023 вторник \n19:00 - 21:00 \nЗадачи Computer vision. \n'
                           'Обзор архитектур: CNN, RNN архитектуры в компьютерном зрении.\n'
                           '\n'
                           '22.02.2023 среда \n19:00 - 21:00 \nМетрики CV.\n'
                           '\n'
                           '25.02.2023 суббота \n12:00 - 14:00 \nОбзор инструментов, пайплайна. \n'
                           'Тензоры в Pytorch Autograd. \nКлассы Dataset и Dataloader в Pytorch '
                           '(на примере классификации). \nДомашнее задание \nДедлайн 04.03.2023\n'
                           '\n'
                           '28.02.2023 вторник \n19:00 - 21:00 \nПродвинутая Классификация: \n'
                           'Бэкбоуны (Resnet, Effnet, ConvNext), лоссы и трюки. \nДомашнее задание \n'
                           'Дедлайн 07.03.2023\n'
                           '\n'
                           '02.03.2023 четверг \n19:00 - 21:00 \nAttention и '
                           'архитектуры трансформеров в CV. \n'
                           '\n'
                           '04.03.2023 суббота \n12:00 - 14:00 \nПродвинутый пайплайн в репозитории. \n'
                           'Бэкбоны, лосы, mixed precision, WandB, git. \n'
                           'Домашнее задание \nДедлайн 11.03.2023\n'
                           '\n'
                           '07.03.2023 вторник \n19:00 - 21:00 \nСегментация.\n'
                           '\n'
                           '09.03.2023 четверг \n19:00 - 21:00 \nДетекция: multishot, single shot.\n'
                           '\n'
                           '11.03.2023 суббота \n12:00 - 14:00 \nСеминар \n'
                           'Сегментация и Детекция \nДомашнее задание \nДедлайн 18.03.2023\n'
                           '\n'
                           '14.03.2023 вторник \n19:00 - 21:00 \nКак искать лица, поиск соседей, '
                           'arcface. \nДомашнее задание \nДедлайн 20.03.2023\n'
                           '\n'
                           '16.03.2023 четверг \n19:00 - 21:00 \nOCR: CRNN, '
                           'трансформеры, CTC loss, beam search, LM-ки для OCR.\n'
                           '\n'
                           '18.03.2023 суббота \n12:00 - 14:00 \nOCR captcha recognition '
                           'RCNN with GRU and CTC loss pipeline Attention and '
                           'Vision Transformer tutorial.\n'
                           '\n'
                           '21.03.2023 вторник \n19:00 - 20:30 \n'
                           'ВЫПУСКНОЙ\n',
                           )
    await message.delete()


# Руководители
async def give_contact(message: types.message):
    await bot.send_message(message.from_user.id,
                           'Луговая Евгения Александровна\n'
                           'Ведущий менеджер по персоналу\n'
                           'e.lugovaja@cft.ru\n'
                           'Новосибирск\n'
                           '\n'
                           'Обеленец Юлия Викторовна\n'
                           'Менеджер по подбору персонала\n'
                           'j.obelenets@cft.ru\n'
                           'Новосибирск\n'
                           '\n'
                           'Лекомцев Александр Михайлович\n'
                           'Старший специалист по компьютерному зрению\n'
                           'a.lekomtsev@cft.ru\n'
                           'Новосибирск\n'
                           '\n'
                           'Швайковский Виктор Сергеевич\n'
                           'Старший инженер машинного обучения\n'
                           'v.shvajkovskij@cft.ru\n'
                           'Новосибирск\n'
                           '\n'
                           'Лагуткин Евгений Александрович\n'
                           'Дата аналитик\n'
                           'e.lagutkin@cft.ru\n'
                           'Новомосковск\n'
                           '\n'
                           'Литвинчук Михаил Анатольевич\n'
                           'Дата аналитик\n'
                           'm.litvinchuk@cft.ru\n'
                           'Новосибирск\n'
                           '\n'
                           'Ачоян Артур Араратович\n'
                           'Дата аналитик\n'
                           'a.achojan@cft.ru\n'
                           'Томск\n'
                           '\n'
                           'Ахметов Данияр Маратович\n'
                           'Дата аналитик\n'
                           'd.akhmetov@cft.ru\n'
                           'Новосибирск\n'
                           '\n'
                           'Савчук Дмитрий Андреевич\n'
                           'Старший дата аналитик\n'
                           'd.savchuk@cft.ru\n'
                           'Минск\n'
                           '\n'
                           'Сергеева София Анатольевна\n'
                           'Ведущий дата аналитик\n'
                           'so.sergeeva@cft.ru\n'
                           'Новосибирск\n'
                           '\n'
                           )  # reply_markup=ReplyKeyboardRemove - удаляет клавиатуру


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(command_start, commands=['start'])
    dp.register_message_handler(give_contact, commands=['Руководители'])
    dp.register_message_handler(command_menu, commands=['Меню'])
    dp.register_message_handler(command_back, commands=['Назад'])
    dp.register_message_handler(command_sched, commands=['Расписание'])
    dp.register_message_handler(command_materials, commands=['Материалы'])
    dp.register_message_handler(command_domashki, commands=['Домашки'])
    dp.register_message_handler(command_3_SQL, commands=['SQL_3'])
    dp.register_message_handler(command_Log_4_1, commands=['Log_4_1'])
    dp.register_message_handler(command_Data_prep_4_2, commands=['Data_prep_4_2'])
    dp.register_message_handler(command_Stat_5, commands=['Stat_5'])

