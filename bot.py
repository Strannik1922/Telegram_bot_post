import telebot
from telebot import types
import json
import requests
import config


bot = telebot.TeleBot(config.token)


@bot.message_handler(commands=['number'])
def phone(message):
    keyboard = types.ReplyKeyboardMarkup(
        row_width=1,
        resize_keyboard=True
    )
    button_phone = types.KeyboardButton(
        text="Отправить номер",
        request_contact=True
    )
    keyboard.add(button_phone)

    bot.send_message(
        message.chat.id,
        'Привет, а дай номер',
        reply_markup=keyboard
    )


@bot.message_handler(content_types=['contact'])
def contact(message):
    if message.contact is not None:
        phone_number = message.contact.phone_number
        login = message.from_user.username

        url = 'https://s1-nova.ru/app/private_test_python/'
        headers = {
            'Content-Type': 'application/json'
        }
        data = {
            'phone': phone_number,
            'login': login
        }

        response = requests.post(url, headers=headers, data=json.dumps(data))
        if response.status_code == 200:
            bot.reply_to(message, "Номер телефона отправлен.")
        else:
            bot.reply_to(message, "Произошла ошибка. Попробуйте еще раз.")


@bot.message_handler(commands=['start'])
def wake_up(message):
    name = message.chat.first_name
    bot.send_message(
        message.chat.id,
        text='Спасибо, что активировал меня, {}! Введите /number'.format(name)
    )


print('Bot started')
bot.polling()
