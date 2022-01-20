#!/usr/bin/env python3

from telegram import Update, Document
from telegram.ext import CallbackContext
from ImageGoNord import GoNord
from PIL import Image
from pathlib import Path
from os.path import join
from os import remove
from telegram import ChatAction
from root.constant.constant import (
    CONVERTING_PHOTO_MESSAGE,
    NOT_A_PHOTO_MESSAGE,
    OUTPUT_DIR,
    OUTPUT_FILE_NAME,
)
import root.util.logger as logger


def image_go_nord(image: Document, user_id: int):
    """Download the picture from telegram and then convert it to a nord colorscheme"""
    nord: GoNord = GoNord()
    logger.info(f"* Downloading image from telegram user {user_id}")
    filename: str = image.get_file().download()
    # * Loading image into GoNord
    image: Image = nord.open_image(filename)
    # * Building the output file path
    path: str = join(OUTPUT_DIR, str(user_id))
    output_file: str = join(path, OUTPUT_FILE_NAME)
    logger.info("* Checking if the output directory exists and create it if not")
    Path(path).mkdir(parents=True, exist_ok=True)
    # * Loading the default Nord Palette
    nord.set_default_nord_palette()
    logger.info(f"* Converting image to nord colorscheme")
    nord.convert_image(image, output_file)
    # * Removing the original file
    remove(filename)
    return join(output_file)


def handle_image(update: Update, context: CallbackContext):
    """Handle a new update containing the picture to convert"""
    image: Document = update.effective_message.document
    if "image" in image.mime_type:
        update.effective_message.reply_text(CONVERTING_PHOTO_MESSAGE)
        logger.info("* Sending chat action: upload_photo")
        update.effective_message.chat.send_action(action=ChatAction.UPLOAD_PHOTO)
        # * Convert the picture to a nord colorscheme and send it back to the user
        output_file: str = image_go_nord(image, update.effective_user.id)
        logger.info(f"* Sending photo: {output_file}")
        update.effective_message.reply_document(document=open(output_file, "rb"))
        logger.info(f"* Removing file: {output_file}")
        remove(output_file)
    else:
        # * Send a message telling the user that document is not an image
        logger.info("* Sending message: %s" % NOT_A_PHOTO_MESSAGE)
        update.effective_message.reply_text(NOT_A_PHOTO_MESSAGE)
