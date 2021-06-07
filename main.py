import logging
from settings import API_KEY
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

logging.basicConfig(filename="bot.log", level=logging.INFO)

def greet_user(update, context):
    # update - information about user from telegram
    # context - commands from function
    print("Called /start")
    update.message.reply_text("Hello user!")

def talk_to_me(update, context):
    text = update.message.text
    print(text)
    update.message.reply_text(text)


def main():
    mybot = Updater(API_KEY)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))


    logging.info("bot is started")
    mybot.start_polling()
    mybot.idle()

if __name__ == '__main__':
    main()