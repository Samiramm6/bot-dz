from telebot import types


def choice_buttons():
    # Создаем пространство
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    # Создаем кнопки
    but1 = types.KeyboardButton('USD')
    but2 = types.KeyboardButton('EUR')
    # Добавляем кнопки в пространство
    kb.add(but1, but2)

    return kb


