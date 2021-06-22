from anketa import anketa_start, anketa_name, anketa_rating, anketa_skip, \
    anketa_comment, anketa_dontknow
from handlers import (greet_user, guess_numb, send_cat,
                      user_coordinates, talk_to_me, check_user_photo)
from settings import API_KEY
from telegram.ext import Updater, CommandHandler, ConversationHandler, MessageHandler, Filters
import logging

logging.basicConfig(filename="bot.log", level=logging.DEBUG)

def main():
    mybot = Updater(API_KEY)

    dp = mybot.dispatcher

    anklet = ConversationHandler(
        entry_points=[
            MessageHandler(Filters.regex('^(Fill in the form)$'), anketa_start)
        ],
        states={
            'name': [MessageHandler(Filters.text, anketa_name)],
            'rating': [MessageHandler(Filters.regex('^(1|2|3|4|5)$'), anketa_rating)],
            'comment': [
                CommandHandler('skip', anketa_skip),
                MessageHandler(Filters.text, anketa_comment)
            ]
        },
        fallbacks=[
            MessageHandler(Filters.text | Filters.photo | Filters.location | Filters.video | Filters.document,
                           anketa_dontknow)
        ]
    )

    dp.add_handler(anklet)
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("guess", guess_numb))
    dp.add_handler(CommandHandler("cat", send_cat))
    dp.add_handler(MessageHandler(Filters.location, user_coordinates))
    dp.add_handler(MessageHandler(Filters.photo, check_user_photo))
    dp.add_handler(MessageHandler(Filters.regex('^(Send me cat)$'), send_cat))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))


    logging.info("bot is started")
    mybot.start_polling()
    mybot.idle()


if __name__ == '__main__':
    main()