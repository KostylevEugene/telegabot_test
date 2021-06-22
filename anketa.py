from db import db, get_or_create_user, save_anketa
from telegram import ParseMode, ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import ConversationHandler
from utils import main_keybord

def anketa_start(update, context):
    update.message.reply_text(
        "Hello, what's your name?",
        reply_markup=ReplyKeyboardRemove()
    )
    return "name"

def anketa_name(update, context):
    user_name = update.message.text
    if len(user_name.split()) < 2:
        update.message.reply_text("Please enter your name and second name")
        return "name"
    else:
        context.user_data['anketa'] = {"name": user_name}
        reply_keyboard = [['1', '2', '3', '4', '5']]
        update.message.reply_text(
            "Please rate our bot from 0 to 5",
            reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
        )
        return 'rating'

def anketa_rating(update, context):
    context.user_data['anketa']['rating'] = int(update.message.text)
    update.message.reply_text("write down a comment or push /skip ")
    return 'comment'

def anketa_comment(update, context):
    context.user_data['anketa']['comment'] = update.message.text
    user = get_or_create_user(db, update.effective_user, update.message.chat.id)
    save_anketa(db, user['user_id'], context.user_data['anketa'])
    user_text = format_anketa(context.user_data['anketa'])
    update.message.reply_text(user_text, parse_mode=ParseMode.HTML, reply_markup=main_keybord())
    return ConversationHandler.END

def anketa_skip(update, context):
    user = get_or_create_user(db, update.effective_user, update.message.chat.id)
    save_anketa(db, user['user_id'], context.user_data['anketa'])
    user_text = format_anketa(context.user_data['anketa'])
    update.message.reply_text(user_text, parse_mode=ParseMode.HTML, reply_markup=main_keybord())
    return ConversationHandler.END

def format_anketa(anketa):
    user_text = f'''<b>First Name and Second name</b>: {anketa['name']}
            <b>Rating</b>: {anketa['rating']}
    '''
    if 'comment' in anketa:
        user_text += f"\n<b>Comment</b>: {anketa['anketa']['comment']}"

    return user_text

def anketa_dontknow(update, context):
    update.message.reply_text("I don't understand you")