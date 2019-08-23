from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from dotenv import load_dotenv
import os
import logging

def start(bot, update):
    logging.info(f'Start of dialog {update.message.chat_id}')
    update.message.reply_text('Привет, я умная железяка, чем могу помочь?')
    
def echo(bot, update):
    logging.info(f'Message received - ID {update.message.chat_id} MESSAGE {update.message.text}')
    update.message.reply_text(update.message.text)

def reply_to_help(bot, update):
    logging.info(f'Request for help - ID {update.message.chat_id}')
    update.message.reply_text('Я бот, созданный в процессе обучения на dvmn.org')

    
if __name__ == "__main__":

    logging.basicConfig(level=logging.INFO, format='[%(levelname)s] - %(message)s')

    load_dotenv()
    telegram_bot_token = os.getenv('TELEGRAM_BOT_TOKEN')

    updater = Updater(telegram_bot_token)

    dp = updater.dispatcher
    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(MessageHandler(Filters.text, echo))
    dp.add_handler(CommandHandler('help', reply_to_help))

    updater.start_polling()
    updater.idle()