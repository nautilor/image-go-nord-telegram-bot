#!/usr/bin/env python3

from telegram import Update
from telegram.ext import CallbackContext
from root.constant.constant import (
    ERROR_MESSAGE,
    LOG_FILE,
    LOG_CHANNEL,
    LOG_CHANNEL_MESSAGE,
    DEFAULT_CAPTION_PARSER,
)
import root.util.logger as logger


def handle_error(update: Update, context: CallbackContext):
    logger.error(context.error)
    update.effective_message.reply_text(ERROR_MESSAGE)
    context.bot.send_document(
        LOG_CHANNEL,
        open(LOG_FILE, "rb"),
        caption=LOG_CHANNEL_MESSAGE,
        **DEFAULT_CAPTION_PARSER,
    )
