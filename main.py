import logging
from emoji import emojize
from glob import glob   # module finds all the pathnames matching a specified pattern
from random import randint, choice

import settings
from settings import API_KEY
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

logging.basicConfig(filename="bot.log", level=logging.INFO)

def greet_user(update, context):
    # update - information about user from telegram
    # context - commands from function
    print("Called /start")
    context.user_data['emoji'] = get_smile(context.user_data)
    update.message.reply_text(f"Hello user!{context.user_data['emoji']}")

def talk_to_me(update, context):
    context.user_data['emoji'] = get_smile(context.user_data)
    text = update.message.text
    print(text)
    update.message.reply_text(f'{text} {context.user_data["emoji"]}')

def get_smile(user_data):
    if 'emoji' not in user_data:
        smile = choice(settings.USER_EMOJI)
        return emojize(smile, use_aliases=True)
    return user_data['emoji']

def guess_numb(update, context):
    print(context.args)
    if context.args:    # context.args - data after calling function
        try:
            user_numb = int(context.args[0])
            message = play_random_numb(user_numb)
        except(TypeError, ValueError):
            message = "Enter an integer number"
    else:
        message = "Enter a number"
    update.message.reply_text(message)

def play_random_numb(user_numb):
    bot_num = randint(user_numb - 10, user_numb + 10)
    if user_numb > bot_num:
        message = f'Your number is {user_numb}, my number is {bot_num}. You win!'
    elif user_numb == bot_num:
        message = f'Your number is {user_numb}, my number is {bot_num}. Draw!'
    else:
        message = f'Your number is {user_numb}, my number is {bot_num}. You lose!'
    return message

def send_cat(update, context):
    cat_photo_list = glob('images/cat*.jpg')
    cat_photo_filename = choice(cat_photo_list)
    chat_id = update.effective_chat.id
    context.bot.send_photo(chat_id=chat_id, photo=open(cat_photo_filename, 'rb'))

def main():
    mybot = Updater(API_KEY)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("guess", guess_numb))
    dp.add_handler(CommandHandler("cat", send_cat))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))


    logging.info("bot is started")
    mybot.start_polling()
    mybot.idle()

if __name__ == '__main__':
    main()