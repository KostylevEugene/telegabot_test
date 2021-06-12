from glob import glob   # module finds all the pathnames matching a specified pattern
from random import randint, choice
from utils import get_smile, play_random_numb, main_keybord

def greet_user(update, context):
    # update - information about user from telegram
    # context - commands from function
    print("Called /start")
    context.user_data['emoji'] = get_smile(context.user_data)
    update.message.reply_text(
        f"Hello user!{context.user_data['emoji']}",
        reply_markup=main_keybord()
    )


def talk_to_me(update, context):
    context.user_data['emoji'] = get_smile(context.user_data)
    text = update.message.text
    print(text)
    update.message.reply_text(f'{text} {context.user_data["emoji"]}', reply_markup=main_keybord())


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
    update.message.reply_text(message, reply_markup=main_keybord())


def send_cat(update, context):
    cat_photo_list = glob('images/cat*.jpg')
    cat_photo_filename = choice(cat_photo_list)
    chat_id = update.effective_chat.id
    context.bot.send_photo(chat_id=chat_id,
                           photo=open(cat_photo_filename, 'rb'),
                           reply_markup=main_keybord()
    )


def user_coordinates(update, context):
    context.user_data['emoji'] = get_smile(context.user_data)
    coords = update.message.location
    update.message.reply_text(
        f'Your coordinates {coords} {context.user_data["emoji"]}!',
        reply_markup=main_keybord()
    )