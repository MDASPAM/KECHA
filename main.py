from aiogram import Bot
from aiogram import Dispatcher
from aiogram import types
from aiogram import executor
from aiogram.types import InputFile



import markups as nav
import asyncio


API_TOKEN = '6330717475:AAG1Oy3W1WD8H2YQpb07JTPBQJNMuPDv8Q8'
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):

    text = 'ЛОВИ СВОЙ ПОДАРОК БРО 😎\n\n' \
           f'{message.from_user.first_name}, добро пожаловать в интенсив:\n' \
           '💎«On-line знакомства»💎\n' \
           'Предлагаю тебе работающию и еффективную схему' \
           'от тренеров в индустрии соблазнения с опытом более 10 лет по тому как стать успешным в области он-лайн соблазнения.\n\n' \
           '-Наладить поток классных девушек в свою жизнь\n ' \
           'Навсегда забыть про день сурка и перегразуть свои серые бедни яркими эмоциями, инетерсными сваиданиями  и улучшить качество жизни!\n\n' \
           'Курс онснован на психологии соблазнения и написан понятным языком для каждого.\n\n' \
           'Авторы Курса:\n\n ' \
           'Андрей Кеча (финалист шоу «Сердце Ивлеевой» с опытом соблазнения больше 8 лет. 500+ зачетов с он-лайн)\n\n ' \
           'Антон Чесноков (психолог с 12 летним опытом. Помог более 300 мужчинам построить личную жизнь)\n\n ' \
           'Дима Микаэло  (дипломированный психолог и сексолог. мастер сексуальных практик. Автор методики «Соблазнение глазами женщины»\n\n\n' \
           '4 коротких урока которые рекомендуем смотреть за один раз что бы прочуствовать весь вайб на 100%\n' \
           'В конце тебя ждет крутейший сюрприз!\n\n' \
           'ТЫ ГОТОВ НАЧАТЬ ❓❓❓\n\n' \
           'ПОГНАЛИ 💣\n\n'
    await bot.send_message(message.from_user.id, text, reply_markup=nav.mainMenu)
    # set to 86400
    await asyncio.sleep(5.0)
    await bot.send_message(message.from_user.id, text='БЕГОМ ПЕРЕХОДИ ПО ССЫЛКЕ 🎮😎', reply_markup=nav.mainMenuSite)


@dp.callback_query_handler(text="btnReady")
async def answer1(message: types.Message):
    media = InputFile('images/first.png')
    await bot.send_photo(message.from_user.id, media,
                         caption='УРОК № 1️⃣\n\n'
                                 '«ВАЖНОСТЬ СОБЛАЗНЕНИЯ ИЛИ КАК НЕ ПРОДРОЧИТЬ СВОЮ ЖИЗНЬ»\n\n'
                                 'Салют бро 😎\n'
                                 'На связи Андрей Кеча\n'
                                 'Сегодня мы поговорим о важности соблазнения или как ты в этом году станешь миллионером 💎', reply_markup=nav.mainMenu1)
    # set to 86400
    await asyncio.sleep(86400.0)
    await bot.send_message(message.from_user.id, text='Бро, все 4 видео лучше смотреть за один раз что бы полность прочуствовать вайб. Быстрее переходи ко второму уроку ❗️\n'
                                                      'Девочки сами себя не соблазнят 😎')
    # set to 86400
    await asyncio.sleep(86400.0)
    omega2 = InputFile('videos/vtoroi.mp4')
    await bot.send_video_note(message.from_user.id, video_note=omega2)
    # set to 172800
    await asyncio.sleep(172800.0)
    await bot.send_message(message.from_user.id, text = 'Ты еще не забрал свой подарок? 🎁\n'
                                                        'Бро у нас тут куча полезностей в нашем интенсиве!)\n'
                                                        'Сегодня, самый лучший день что бы начать!) Нет времени объяснять, срочно открывай первый урок!)')


    # set to 86400
    await asyncio.sleep(86400.0)
    await bot.send_message(message.from_user.id, text='ТЫ ЕЩЕ НЕ В ИГРЕ? 🎮😎',reply_markup=nav.mainMenuSite)

    # set to 86400

    await asyncio.sleep(86400.0)
    await bot.send_message(message.from_user.id, text = 'Ты в курсе что есть более 12 площадок для знакомства где девушки САМИ ждут втоего первого шага? 😏\n\n'
                                                        'СМОТРИ ВИДЕО 💎 \n'
                                                        'https://youtu.be/wt8f88xLO3M')
    # set to 86400
    await asyncio.sleep(86400.0)
    await bot.send_message(message.from_user.id, text='Скоро видео сгорит ❗️'
                                                      'https://youtu.be/txhqoRaEuWI')
    # set to 86400
    await asyncio.sleep(86400.0)
    omega1 = InputFile('videos/doc_2023-07-20_18-08-30.mp4')
    await bot.send_video_note(message.from_user.id,video_note=omega1)
   
    # set to 86400
    await asyncio.sleep(86400.0)
    await bot.send_message(message.from_user.id,
                           text='Ты в курсе что есть более 12 площадок для знакомства где девушки САМИ ждут втоего первого шага? 😏\n\n'
                                'СМОТРИ ВИДЕО 💎 \n'
                                'https://youtu.be/wt8f88xLO3M')
    # set to 86400
    await asyncio.sleep(86400.0)
    omega5 = InputFile('videos/5.mp4')
    await bot.send_video_note(message.from_user.id, video_note=omega5)

    # set to 86400
    await asyncio.sleep(86400.0)
    await bot.send_message(message.from_user.id,
                           text='Ты в курсе что есть более 12 площадок для знакомства где девушки САМИ ждут втоего первого шага? 😏\n\n'
                                'СМОТРИ ВИДЕО 💎 \n'
                                'https://youtu.be/wt8f88xLO3M')
    # set to 86400
    await asyncio.sleep(86400.0)
    omega3 = InputFile('videos/tri.mp4')
    await bot.send_video_note(message.from_user.id, video_note=omega3)

    # set to 86400

    await asyncio.sleep(86400.0)
    await bot.send_message(message.from_user.id, text='Скоро видео сгорит ❗️'

                                                      'https://youtu.be/wt8f88xLO3M')
    # set to 86400
    await asyncio.sleep(86400.0)
    await bot.send_message(message.from_user.id, text='ПРОКАЧАЙ СВОЕГО ПЕРСОНАЖА 🎮😎', reply_markup=nav.mainMenuSite)
    #set to 86400
    await asyncio.sleep(86400.0)
    omega6 = InputFile('videos/6.mp4')
    await bot.send_video_note(message.from_user.id, video_note=omega6)

    # set to 86400
    await asyncio.sleep(86400.0)
    await bot.send_message(message.from_user.id, text='Скоро видео сгорит ❗️'
                                                      'https://youtu.be/6JCstcNWsb8')
    #set t0 86400
    await asyncio.sleep(86400.0)
    await bot.send_message(message.from_user.id, text='Я за тобой бегать не буду) Но и на ровном месте слиться тоже не дам 🎮😎\n', reply_markup=nav.mainMenuSpam)

    # set to 86400
    await asyncio.sleep(86400.0)
    omega4 = InputFile('videos/4.mp4')
    await bot.send_video_note(message.from_user.id, video_note=omega4)

    await asyncio.sleep(86400.0)
    await bot.send_message(message.from_user.id, text='Скоро видео сгорит ❗️'

                                                      'https://youtu.be/wt8f88xLO3M')



    #NEXT BLOCK
    # set to 86400
    await asyncio.sleep(172800.0)
    await bot.send_message(message.from_user.id, text='ПРОКАЧАЙ СВОЕГО ПЕРСОНАЖА 🎮😎', reply_markup=nav.mainMenuSite)
    # set to 86400
    await asyncio.sleep(216000.0)
    omega6 = InputFile('videos/6.mp4')
    await bot.send_video_note(message.from_user.id, video_note=omega6)

    # set to 86400
    await asyncio.sleep(259200.0)
    await bot.send_message(message.from_user.id, text='Скоро видео сгорит ❗️'
                                                      'https://youtu.be/6JCstcNWsb8')
    # set t0 86400
    await asyncio.sleep(302400.0)
    await bot.send_message(message.from_user.id,
                           text='Я за тобой бегать не буду) Но и на ровном месте слиться тоже не дам 🎮😎\n',
                           reply_markup=nav.mainMenuSpam)

    # set to 86400
    await asyncio.sleep(345600.0)
    omega4 = InputFile('videos/4.mp4')
    await bot.send_video_note(message.from_user.id, video_note=omega4)
    # set to 86400
    await asyncio.sleep(388800.0)
    omega6 = InputFile('videos/6.mp4')
    await bot.send_video_note(message.from_user.id, video_note=omega6)

    # set to 86400
    await asyncio.sleep(432000.0)
    await bot.send_message(message.from_user.id, text='Скоро видео сгорит ❗️'
                                                      'https://youtu.be/6JCstcNWsb8')
    # set t0 86400
    await asyncio.sleep(86400.0)
    await bot.send_message(message.from_user.id,
                           text='Я за тобой бегать не буду) Но и на ровном месте слиться тоже не дам 🎮😎\n',
                           reply_markup=nav.mainMenuSpam)

    # set to 86400
    await asyncio.sleep(172800.0)
    omega4 = InputFile('videos/4.mp4')
    await bot.send_video_note(message.from_user.id, video_note=omega4)

    await asyncio.sleep(216000.0)
    await bot.send_message(message.from_user.id,
                           text='Бро, все 4 видео лучше смотреть за один раз что бы полность прочуствовать вайб. Быстрее переходи ко второму уроку ❗️\n'
                                'Девочки сами себя не соблазнят 😎')
    # set to 86400
    await asyncio.sleep(86400.0)
    omega2 = InputFile('videos/vtoroi.mp4')
    await bot.send_video_note(message.from_user.id, video_note=omega2)
    # set to 172800
    await asyncio.sleep(388800.0)
    await bot.send_message(message.from_user.id, text='Ты еще не забрал свой подарок? 🎁\n'
                                                      'Бро у нас тут куча полезностей в нашем интенсиве!)\n'
                                                      'Сегодня, самый лучший день что бы начать!) Нет времени объяснять, срочно открывай первый урок!)')

    # set to 86400
    await asyncio.sleep(302400.0)
    await bot.send_message(message.from_user.id, text='ТЫ ЕЩЕ НЕ В ИГРЕ? 🎮😎', reply_markup=nav.mainMenuSite)

    # set to 86400

    await asyncio.sleep(604800.0)
    await bot.send_message(message.from_user.id,
                           text='Ты в курсе что есть более 12 площадок для знакомства где девушки САМИ ждут втоего первого шага? 😏\n\n'
                                'СМОТРИ ВИДЕО 💎 \n'
                                'https://youtu.be/wt8f88xLO3M')
    # set to 86400
    await asyncio.sleep(604800.0)
    await bot.send_message(message.from_user.id, text='Скоро видео сгорит ❗️'
                                                      'https://youtu.be/txhqoRaEuWI')
    # set to 86400
    await asyncio.sleep(172800.0)
    omega1 = InputFile('videos/doc_2023-07-20_18-08-30.mp4')
    await bot.send_video_note(message.from_user.id, video_note=omega1)

    # set to 86400
    await asyncio.sleep(604800.0)
    await bot.send_message(message.from_user.id,
                           text='Ты в курсе что есть более 12 площадок для знакомства где девушки САМИ ждут втоего первого шага? 😏\n\n'
                                'СМОТРИ ВИДЕО 💎 \n'
                                'https://youtu.be/wt8f88xLO3M')


@dp.callback_query_handler(text="btnGo1")
async def answer1(message: types.Message):
    media = InputFile('images/second.png')
    await bot.send_photo(message.from_user.id, media,
                         caption='УРОК № 2️⃣\n\n'
                                 '«10 ОШИБОК ПРИ ЗНАКОМСТВЕ ON-LINE»\n\n'
                                 'Меня зовут Антон Чесноков 🤓\n'
                                 'Во втором уроке мы обсудим ошибки при знакомстве с девушками или почему ты теряешь столько энергии? 🤔', reply_markup=nav.mainMenu2)
    # set to 4000
    await asyncio.sleep(4000)
    await bot.send_message(message.from_user.id, text = 'ОПЯТЬ ТУПИШЬ?) 🤔\n\n'
                                                        'РЕКОМЕНДУЮ ПРОЙТИ СЛЕДУЮЩИЙ УРОК КАК МОЖНО БЫСТРЕЕ. ТАМ ВСЕ САМОЕ ИНТЕРЕСНОЕ 🎮\n')


@dp.callback_query_handler(text="btnGo2")
async def answer1(message: types.Message):
    media = InputFile('images/third.png')
    await bot.send_photo(message.from_user.id, media,
                         caption='УРОК № 3️⃣\n\n'
                                 '«ДЕЙТИНГ ГЛАЗАМИ ДЕВУШЕК»\n\n'
                                 'А теперь давай посмотрим на знакомства с другой стороны 😏', reply_markup=nav.mainMenu3)

    # set to 86400
    await asyncio.sleep(5.0)
    await bot.send_message(message.from_user.id, text='ВРЕМЯ ИЗМЕНИТЬ СВОЮ ЖИЗНЬ 🎮😎', reply_markup=nav.mainMenuSite)

@dp.callback_query_handler(text="btnGo3")
async def answer1(message: types.Message):
    media = InputFile('images/foth.png')
    await bot.send_photo(message.from_user.id, media,
                         caption='УРОК № 4️⃣\n\n'
                                 '«Твоя точка 🅱️ или как жить жизнь на все 100%»\n\n'
                                 'Сделай глубокий вдох. Ты готов изменить свою жизнь 😎', reply_markup=nav.mainMenu4)


@dp.callback_query_handler(text="btnGo4")
async def answer1(message: types.Message):
    await bot.send_message(message.from_user.id, text=f'😎{message.from_user.first_name}, поздравляю с прохождением ИНТЕНСИВА! Просто красавчик 💪🏿\n\n'
                                'Теперь у тебя есть понимание важнейшей БАЗЫ! В этом боте мы будем постоянно скидывать новую и мощную инфу)\n\n'
                                'Не теряй время и вперед к новым приключениям!)\n\n'
                                'Обязательно будь на связи и задавай вопросы в личку!)\n\n'
                                '🔺Телеграм:\n'
                                '@Blackkuba\n'
                                '@Anton_chesnokov\n'
                                '@Dimitrius_Mikaello\n\n\n'
                                'P.S. Через минуту пришлю тебе очень важную информацию.')
    #set to 60
    await asyncio.sleep(10.0)
    await bot.send_message(message.from_user.id, text = '🎮OG GAME🎮\n\n'
                                                        'Готов к самой интересной игре в своей жизни? \n\n'
                                                        'Упакуй и прокачай своего персонажа 🦸\n\n'
                                                        'OG - это уникальный проект который научит тебя соблазнять девушек онлайн и создать стабильный поток девушек в свою жизнь ❗️\n\n'
                                                        'ЧТО ТЫ ПОЛУЧИШЬ?\n\n'
                                                        '-стабильный поток свиданий из сервисов on-line знакомств.\n'
                                                        '-прокаченный акаунт привлекающий сумасшедшее  количество лайков\n'
                                                        '-простую и понятную структуру переписок\n '
                                                        '-поток заинтересованных в тебе девушек\n'
                                                        '-ты станешь мастером флирта и влюбления в себе\n\n'
                                                        'ПЕРЕХОДИ ПО ССЫЛКЕ И ПРОКАЧИВАЙ СВОЮ ЖИЗНЬ ⬇️⬇️⬇️\n\n'
                                                        'on-line-game.ru')



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)