from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

mainMenu = InlineKeyboardMarkup()
btnReady =InlineKeyboardButton(text="Готов? погнали!", callback_data="btnReady")
mainMenu.insert(btnReady)

mainMenu1 = InlineKeyboardMarkup(row_width=2)
btnGo1 = InlineKeyboardButton(text="Погнали дальше!🏎️", callback_data="btnGo1")
btnLink1 = InlineKeyboardButton(text="Посмотреть первый урок👀", callback_data="btnLink1", url="https://youtu.be/txhqoRaEuWI")


mainMenu1.add(btnLink1)
mainMenu1.add(btnGo1)


mainMenu2 = InlineKeyboardMarkup(row_width=2)
btnGo2 = InlineKeyboardButton(text="Погнали дальше!🏎️", callback_data="btnGo2")
btnLink2 = InlineKeyboardButton(text="Посмотреть второй урок👀", callback_data="btnLink2", url="https://youtu.be/wt8f88xLO3M")

mainMenu2.add(btnLink2)
mainMenu2.add(btnGo2)


mainMenu3 = InlineKeyboardMarkup(row_width=2)
btnGo3 = InlineKeyboardButton(text="Погнали дальше!🏎️", callback_data="btnGo3")
btnLink3 = InlineKeyboardButton(text="Посмотреть третий урок👀", callback_data="btnLink3", url="https://youtu.be/6JCstcNWsb8")

mainMenu3.add(btnLink3)
mainMenu3.add(btnGo3)


mainMenu4 = InlineKeyboardMarkup(row_width=2)
btnGo4 = InlineKeyboardButton(text="Поехали дальше!", callback_data="btnGo4")
btnLink4 = InlineKeyboardButton(text="Посмотреть четвёртый урок👀", callback_data="btnLink4", url="https://youtu.be/4deXs6-dyvY")

mainMenu4.add(btnLink4)
mainMenu4.add(btnGo4)

mainMenuSpam = InlineKeyboardMarkup(row_width=2)

btnLinkSpam = InlineKeyboardButton(text="Посмотреть четвёртый урок👀", callback_data="btnLink4", url="https://youtu.be/4deXs6-dyvY")
mainMenuSpam.add(btnLinkSpam)

mainMenuSite = InlineKeyboardMarkup(row_width=2)

btnLinkSite = InlineKeyboardButton(text="Прокачаться💪", callback_data="btnLinkSite", url="on-line-game.ru")
mainMenuSite.add(btnLinkSite)