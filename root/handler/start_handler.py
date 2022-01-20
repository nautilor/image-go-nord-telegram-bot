#!/usr/bin/env python3
from multiprocessing.sharedctypes import Value
from telegram import Update
from telegram.ext import CallbackContext
from root.constant.constant import WELCOME_MESSAGE
from root.decorator.telegram import delete_if_private
from telegram.error import BadRequest


@delete_if_private
def handle_start(update: Update, context: CallbackContext):
    """Just send a simple message telling the user what to do"""
    update.message.reply_text(WELCOME_MESSAGE)
