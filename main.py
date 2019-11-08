#!/usr/bin/env python
# -*- coding: utf-8 -*-
# This program is dedicated to the public domain under the CC0 license.

"""
Simple Bot to reply to Telegram messages.

First, a few handler functions are defined. Then, those functions are passed to
the Dispatcher and registered at their respective places.
Then, the bot is started and runs until we press Ctrl-C on the command line.

Usage:
Basic Echobot example, repeats messages.
Press Ctrl-C on the command line or send a signal to the process to stop the
bot.
"""

import os
import logging
import requests

from dotenv import load_dotenv

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

import converter

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


def get_usage_message():
    return '''
    Welcome to Tanach Study! This bot allows you to query our system for audio classes and play them right here in Telegram!

    Available commands:

    /help - print this message

    <b>/parasha &lt;program&gt; &lt;parasha&gt;</b>
    Example: /parasha midrash lech lecha

    <b>/nach &lt;sefer&gt; &lt;perek&gt;</b>
    Example: /nach yehoshua 2

    <b>/mishna &lt;masechet&gt; &lt;perek&gt; &lt;mishna&gt;</b>
    Example: /mishna shabbat 1 3
    '''

# Define a few command handlers. These usually take the two arguments update and
# context. Error handlers also receive the raised TelegramError object in error.
def start(update, context):
    send_usage(update)


def help(update, context):
    send_usage(update)


def send_usage(update):
    update.message.reply_html(get_usage_message())


def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update caused error "%s"', context.error)


def test(update, context):
    print(update.message.reply_audio(
        audio = "https://cdn.tanachstudy.com/archives/Ketuvim/Tehillim/recordings/rabbi-shimon-alouf-tehillim-5-teamim.mp3",
        thumb = "https://cdn.tanachstudy.com/assets/images/logo.png"
    ))

# TODO: do some input validation - ensure only letters/numbers, etc
def validate_input(text):
    return True


def parse_message(scheme, text):
    is_valid = validate_input(text)
    if not is_valid:
        return 'invalid'

    split = text.split(' ')

    if scheme == 'parasha':
        if len(split) != 3:
            return 'err'
        return {
            'program': split[1],
            'parasha': split[2]
        }

    if scheme == 'nach':
        if len(split) != 3:
            return 'err' 
        return {
            'sefer': split[1],
            'perek': split[2]
        }

    if scheme == 'mishna':
        if len(split) != 4:
            return 'err' 
        return {
            'masechet': split[1],
            'perek': split[2],
            'mishna': split[3]
        }

    return 'bad_scheme'


def build_query(scheme, parsed):
    query = ''
    i = 0
    base = 'https://api.tanachstudy.com'
    if scheme == 'parasha':
        program = parsed['program']
        parasha = parsed['parasha']
        sefer = converter.get_sefer_from_parasha(parasha)
        query = '{}/parasha-study/{}/{}/{}'.format(base, program, sefer, parasha)

    if scheme == 'nach':
        sefer = parsed['sefer']
        perek = parsed['perek']
        query = '{}/tanach-study/perakim/{}/{}'.format(base, sefer, perek)

    if scheme == 'mishna':
        masechet = parsed['masechet']
        perek = parsed['perek']
        mishna = parsed['mishna']
        i = int(mishna)
        seder = converter.get_seder_from_masechet(masechet)
        query = '{}/mishna-study/perek/{}/{}/{}'.format(base, seder, masechet, perek)

    if query == '':
        return 'err', -1
    return query, i


def get_audio_url(query, i=0):
    resp = requests.get(query)
    data = resp.json()
    data = data[i]
    out = ''
    if data.get('audio_url') is not None:
        audio = data['audio_url']
        if audio.get('host') is not None and audio.get('path') is not None:
            out += audio['host'] + audio['path']
    return out


def handle_audio_request(update, context, scheme):
    ret = parse_message(scheme, update.message.text)
    if ret == 'err' or ret == 'invalid' or ret == 'bad_scheme':
        return send_usage(update)
    query, i = build_query(scheme, ret)
    audio = get_audio_url(query, i)
    print(audio)
    if audio is not '':
        res = update.message.reply_audio(audio=str(audio))
    elif audio is '':
        update.message.reply_text('bot error')

def parasha_handler(update, context):
    handle_audio_request(update, context, 'parasha')
            

def nach_handler(update, context):
    handle_audio_request(update, context, 'nach')
            

def mishna_handler(update, context):
    handle_audio_request(update, context, 'mishna')
    


def main():
    """Load environment variables"""
    load_dotenv()
    TOKEN = os.getenv("TELEGRAM_API_KEY")

    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater(TOKEN, use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("test", test))
    dp.add_handler(CommandHandler("parasha", parasha_handler))
    dp.add_handler(CommandHandler("nach", nach_handler))
    dp.add_handler(CommandHandler("mishna", mishna_handler))

    # on noncommand i.e message - echo the message on Telegram
    dp.add_handler(MessageHandler(Filters.text, help))

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
