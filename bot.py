from flask import Flask, render_template, request, redirect, url_for
import telebot
import random
import json
from telegram import Update, InputFile
from telegram.ext import Updater, CommandHandler, CallbackContext, Dispatcher
import os

WEBHOOK_URL = "https://fornastya-6yps.onrender.com"
bot_token = "7441803509:AAF5YpnS7KKgCWM5TCxpQaMlYPiTo6YmiPA"

bot = Bot(token=bot_token)
updater = Updater(token=bot_token, use_context=True)
dispatcher: Dispatcher = updater.dispatcher
app = Flask(__name__)

def set_webhook():
    webhook_url = f"{WEBHOOK_URL}/{bot_token}"
    response = requests.post(f"https://api.telegram.org/bot{bot_token}/setWebhook", data={"url": webhook_url})
    if response.status_code == 200:
        print("Webhook установлен успешно!")
    else:
        print(f"Не удалось установить webhook: {response.text}")

# Обработчик команды /start
def start_command(update: Update, context: CallbackContext):
    chat_id = update.message.chat_id
    welcome_message = "Привет! Чтобы воспользоваться нашим ботом - запусти приложение!"
    image_url = url_for('static', filename='images/Start_icon.png', _external=True)

    # Отправляем приветственное сообщение
    context.bot.send_message(chat_id=chat_id, text=welcome_message)

    # Отправляем картинку
    context.bot.send_photo(chat_id=chat_id, photo=image_url)

dispatcher.add_handler(CommandHandler("start", start_command))

# Основная функция вебхука
@app.route(f'/{bot_token}', methods=['POST'])
def webhook():
    update = Update.de_json(request.get_json(force=True), updater.bot)
    dispatcher.process_update(update)
    return "ok", 200
