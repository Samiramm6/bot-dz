import telebot
import requests

import buttons
url = "https://cbu.uz/ru/arkhiv-kursov-valyut/json/"


response = requests.get(url)


# Создаем объект бота
bot = telebot.TeleBot('7269209408:AAGej2RkZjEzWtORbYUerWpxZohpgEZ0cew')


# Обработка команды /start
@bot.message_handler(commands=['start'])
def start_message(message):
    user_id = message.from_user.id
    user_name = message.from_user.first_name
    bot.send_message(user_id, f'Здравствуйте, {user_name}! Добро пожаловать в мой бот!',
                     reply_markup=buttons.choice_buttons())


# Обработка текстовых сообщений
@bot.message_handler(content_types=['text'])
def text_message(message):
    user_id = message.from_user.id
    if message.text.lower() == 'usd':
        bot.send_message(user_id, 'Введите сумму')
        # Переход на этап википедии
        bot.register_next_step_handler(message, usd)
    elif message.text.lower() == 'eur':
        bot.send_message(user_id, 'Введите сумму')
        # Переход на этап перевода
        bot.register_next_step_handler(message, eur)





def usd(message):
    user_id = message.from_user.id
    if message.text.isnumeric():
        bot.send_message(user_id, f'{round(float(message.text) / USD,1)}')
        bot.send_message(user_id, 'Готово, что еще?')
    else:
        bot.send_message(user_id, 'Вводите только числа')


def eur(message):
    user_id = message.from_user.id
    if message.text.isnumeric():
        bot.send_message(user_id, f'{round(float(message.text) / EUR,2)}')
        bot.send_message(user_id, 'Готово! Что еще?', reply_markup=buttons.choice_buttons())
    else:
        bot.send_message(user_id, 'Вводите только числа')

# Запуск бота
bot.polling(non_stop=True)