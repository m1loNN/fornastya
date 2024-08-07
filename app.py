# -*- coding: utf-8 -*-
from flask import Flask, render_template, request, redirect, url_for
import telebot
import random
import json
from telegram import Update, InputFile
from telegram.ext import Updater, CommandHandler, CallbackContext, Dispatcher
import os
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from werkzeug.urls import url_quote_plus as url_quote

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/select', methods=['GET', 'POST'])
def select():
    with open('static/json/pictures.json') as f:
        pictures = json.load(f)
    selected_pictures = random.sample(pictures, 3)
    return render_template('select.html', pictures=selected_pictures)

@app.route('/chosen', methods=['POST'])
def chosen():
    chosen_picture = request.form['chosen_picture']
    return render_template('chosen.html', picture=chosen_picture)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Привет! Нажми на /nickname чтобы выбрать прозвище на сегодня.")

@bot.message_handler(commands=['nickname'])
def send_nickname(message):
    bot.send_message(message.chat.id, "Перейди по ссылке, чтобы выбрать прозвище: http://yourdomain.com")

if __name__ == "__main__":
    app.run(debug=True)
    bot.polling()