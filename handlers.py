from db import db, get_or_create_user
from glob import glob   # module finds all the pathnames matching a specified pattern
from random import choice
from utils import play_random_numb, main_keybord
import os

def greet_user(update, context):
    # update - information about user from telegram
    # context - commands from function
    user = get_or_create_user(db, update.effective_user, update.message.chat.id)
    print("Called /start")
    update.message.reply_text(
        f"Hello user!{user['emoji']}",
        reply_markup=main_keybord()
    )


def talk_to_me(update, context):
    user = get_or_create_user(db, update.effective_user, update.message.chat.id)
    text = update.message.text
    print(text)
    update.message.reply_text(f'{text} {user["emoji"]}', reply_markup=main_keybord())


def guess_numb(update, context):
    user = get_or_create_user(db, update.effective_user, update.message.chat.id)
    if context.args:    # context.args - data after calling function
        try:
            user_numb = int(context.args[0])
            message = play_random_numb(user_numb)
        except(TypeError, ValueError):
            message = "Enter an integer number"
    else:
        message = "Enter a number"
    update.message.reply_text(message, reply_markup=main_keybord())


def send_cat(update, context):
    user = get_or_create_user(db, update.effective_user, update.message.chat.id)
    cat_photo_list = glob('images/cat*.jpg')
    cat_photo_filename = choice(cat_photo_list)
    chat_id = update.effective_chat.id
    context.bot.send_photo(chat_id=chat_id,
                           photo=open(cat_photo_filename, 'rb'),
                           reply_markup=main_keybord()
    )


def user_coordinates(update, context):
    user = get_or_create_user(db, update.effective_user, update.message.chat.id)
    coords = update.message.location
    update.message.reply_text(
        f'Your coordinates {coords} {user["emoji"]}!',
        reply_markup=main_keybord()
    )


def check_user_photo(update, context):
    user = get_or_create_user(db, update.effective_user, update.message.chat.id)
    update.message.reply_text("Processing the photo")
    os.makedirs('downloads', exist_ok=True)
    user_photo = context.bot.getFile(update.message.photo[-1].file_id)
    file_name = os.path.join('downloads', f'{user_photo.file_id}.jpg')      #   os.path.join - join folders in
                                                                            #           the path in a right way
    user_photo.download(file_name)

    update.message.reply_text("The photo is saved on disk")

