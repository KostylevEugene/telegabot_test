import settings
from emoji import emojize
from random import randint, choice
from telegram import ReplyKeyboardMarkup, KeyboardButton

def get_smile(user_data):
    if 'emoji' not in user_data:
        smile = choice(settings.USER_EMOJI)
        return emojize(smile, use_aliases=True)
    return user_data['emoji']


def play_random_numb(user_numb):
    bot_num = randint(user_numb - 10, user_numb + 10)
    if user_numb > bot_num:
        message = f'Your number is {user_numb}, my number is {bot_num}. You win!'
    elif user_numb == bot_num:
        message = f'Your number is {user_numb}, my number is {bot_num}. Draw!'
    else:
        message = f'Your number is {user_numb}, my number is {bot_num}. You lose!'
    return message


def main_keybord():
    return ReplyKeyboardMarkup([['Send me cat', KeyboardButton('Send my coordinates', request_location=True)] ])

