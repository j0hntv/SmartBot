from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from dotenv import load_dotenv
import os
import dialogflow_api
import logging
import config


logger = logging.getLogger('Telegram-bot')


def start(bot, update):
    logger.info(f'Start of dialog {update.message.chat_id}')
    update.message.reply_text('Привет, я умная железяка, чем могу помочь?')

def reply_to_help(bot, update):
    logger.info(f'Request for help - ID {update.message.chat_id}')
    update.message.reply_text('Я бот, созданный в процессе обучения на dvmn.org')

def reply(bot, update):
    chat_id = update.message.chat_id
    message = update.message.text

    logger.info(f'Received message from ID {chat_id} - Message: {message}')

    answer = dialogflow_api.get_answer(GOOGLE_PROJECT_ID, chat_id, message, 'ru')
    update.message.reply_text(answer)

    logger.info(f'Message sent to ID {chat_id} - Message: {answer}')


if __name__ == "__main__":
    load_dotenv()
    TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
    GOOGLE_PROJECT_ID = os.getenv('GOOGLE_PROJECT_ID')

    config.setup_logger(logger)
    logger.info('Бот заработал.')

    updater = Updater(TELEGRAM_BOT_TOKEN)

    dp = updater.dispatcher
    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CommandHandler('help', reply_to_help))
    dp.add_handler(MessageHandler(Filters.text, reply))

    updater.start_polling()
    updater.idle()
