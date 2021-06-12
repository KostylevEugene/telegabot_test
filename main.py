import logging
from handlers import (greet_user, guess_numb, send_cat,
                      user_coordinates, talk_to_me)
from settings import API_KEY
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

logging.basicConfig(filename="bot.log", level=logging.INFO)

def main():
    mybot = Updater(API_KEY)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("guess", guess_numb))
    dp.add_handler(CommandHandler("cat", send_cat))
    dp.add_handler(MessageHandler(Filters.location, user_coordinates))
    dp.add_handler(MessageHandler(Filters.regex('^(Send me cat)$'), send_cat))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))


    logging.info("bot is started")
    mybot.start_polling()
    mybot.idle()

if __name__ == '__main__':
    main()