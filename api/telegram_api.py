import telebot
from telebot import types

from beans.user import User
from constants import TELEGRAM_API_TOKEN

bot = telebot.TeleBot(TELEGRAM_API_TOKEN)


# Send a message to Telegram chat without options
def send_message(user: User, state, response):
    print(f"Sending response '{response}' for user {user.id} state '{state}'")

    return bot.send_message(user.id, response)


# Send a message to Telegram chat with options, with two options in a row by default
def send_message_with_options(user: User, state, response, *options, row_width=2):
    print(f"Sending response '{response}' with options '{options}' for user {user.id} state '{state}'")

    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, row_width=row_width)
    markup.add(*options)

    return bot.send_message(user.id, response, reply_markup=markup)
