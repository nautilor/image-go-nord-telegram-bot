#!/usr/bin/env python3

from telegram import Update, ChatAction
from telegram.ext import CallbackContext


def delete_if_private(fn: callable):
    def wrapper(update: Update, context: CallbackContext):
        if update.effective_message.chat.type == "private":
            update.effective_message.delete()
        fn(update, context)

    return wrapper
