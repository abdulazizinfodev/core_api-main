#!/usr/bin/env python
from django.core.management.utils import get_random_secret_key
import requests
import logging
from data.config import BOT_TOKEN, ADDRES
from telegram import ForceReply, Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters


logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

logging.getLogger("httpx").setLevel(logging.WARNING)

logger = logging.getLogger(__name__)


def save_user(message) -> int():
    post_data = {"username": str(message.from_user.id),
                 "first_name": str(message.from_user.first_name),
                 "last_name": str(message.from_user.last_name),
                 "password": str(get_random_secret_key())}
    url = f"{ADDRES}api/register/"
    response = requests.post(url, data=post_data)
    return response


def activate_user(id):
    post_data = {"username": str(id)}
    url = f"{ADDRES}api/register/activate-user/"
    response = requests.post(url, data=post_data)
    return response


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    usr = save_user(update.message)
    if usr.status_code == 201:
        user = update.effective_user
        await update.message.reply_html(
            rf"Salom, xush kelibsiz {user.mention_html()}!")
    else:
        await update.message.reply_html(
            rf"Ushbu hisob allaqachon yaratilgan!")


async def login_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    usr = activate_user(update.message.from_user.id)
    if usr.status_code == 200:
        await update.message.reply_text(f"<b>Kod:</b> {usr.text}")
    elif usr.status_code == 400:
        await update.message.reply_text(f"<b>Xatolik:</b> {usr.text}")
    else:
        await update.message.reply_text("<b>Xolat:</b> siz to'lov qilmagansiz!")


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Kirish kodini olish uchun /login ni bosing!")


def main() -> None:
    application = Application.builder().token(BOT_TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("login", login_command))
    application.add_handler(CommandHandler("help", help_command))

    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()
