#!/usr/bin/env python3

from os import environ
from telegram.ext.filters import BaseFilter, Filters

# * Filter to accept updates only from private chats
PRIVATE_CHAT: BaseFilter = Filters.chat_type.private
PRIVATE_PICTURE: BaseFilter = Filters.document & PRIVATE_CHAT

# * Bot information
BOT_NAME = "ImageGoNordBot"
BOT_DISPLAY_NAME = "❄️  Image Go Nord Bot"
BOT_LINK = '<a href="https://t.me/{}">{}</a>'.format(BOT_NAME, BOT_DISPLAY_NAME)

# * Default arguments for telegram actions
DEFAULT_MESSAGE_PARSER = {"parse_mode": "HTML", "disable_web_page_preview": True}
DEFAULT_CAPTION_PARSER = {"parse_mode": "HTML"}

# * Telegram token
TOKEN_NOT_FOUND = "Environment variable 'TOKEN' not found."
TOKEN = environ.get("TOKEN", None)

# * Log channel info
LOG_CHANEL_NOT_FOUND = "Environment variable 'LOG_CHANNEL' not found."
LOG_CHANNEL = environ.get("LOG_CHANNEL", None)
LOG_CHANNEL_MESSAGE = f"❌ An error occurred in {BOT_LINK}. Please check the log."
LOG_FILE = "server.log"

# * Telegram messages
WELCOME_MESSAGE = (
    "😄  Welcome, please send me the picture you want to convert as a file."
)
ERROR_MESSAGE = "😔  Sorry, something went wrong. Please try again later."
NOT_A_PHOTO_MESSAGE = "❌  I can only convert images."
CONVERTING_PHOTO_MESSAGE = "🔄 Converting the picture..."
SENDING_PHOTO_MESSAGE = "📤 Sending the converted picture..."

# * File conversion parameters
OUTPUT_DIR = "output"
OUTPUT_FILE_NAME = "output.png"
