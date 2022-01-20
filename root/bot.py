#!/usr/bin/env python3

from telegram.ext.updater import Updater
from telegram.ext.dispatcher import Dispatcher
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters
from root.constant.constant import (
    PRIVATE_CHAT,
    PRIVATE_PICTURE,
    TOKEN,
    TOKEN_NOT_FOUND,
)
from root.handler.error_handler import handle_error
from root.handler.start_handler import handle_start
from root.handler.image_handler import handle_image
import root.util.logger as logger


def initialize_bot():
    if not TOKEN:
        logger.error(TOKEN_NOT_FOUND)
        raise ValueError(TOKEN_NOT_FOUND)
    updater: Updater = Updater(token=TOKEN, use_context=True)
    dispatcher: Dispatcher = updater.dispatcher
    dispatcher.add_error_handler(handle_error)
    logger.info("* Adding CommandHandler: '/start'")
    dispatcher.add_handler(CommandHandler("start", handle_start, PRIVATE_CHAT))
    logger.info("* Adding MessageHandler: document")
    dispatcher.add_handler(MessageHandler(PRIVATE_PICTURE, handle_image))
    logger.info("* Listening for incoming updates")
    updater.start_polling(drop_pending_updates=True)
