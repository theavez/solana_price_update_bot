import telebot
from time import sleep
from sol import get_price
import schedule
import threading

BOT_TOKEN = "YOUR BOT TOKEN"
bot = telebot.TeleBot(BOT_TOKEN)

scheduled_jobs = {}

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Howdy, how are you doing?")

@bot.message_handler(commands=['update'])
def update(message):
    bot.reply_to(message, get_price())

@bot.message_handler()
def handle_message(message):
    if message.text.startswith('/frequency'):
        bot.send_message(message.chat.id, 'Enter the frequency time (in minutes): \ne.g 2-2 Minutes, 5-5 Minutes, 10-10 Minutes, 0-STOP')
    elif message.text.startswith('/stop'):
        stop_schedule(message.chat.id)
    else:
        frequency = message.text
        if frequency.replace(" ", "").replace("-", "").isdigit():
            frequency_time = int(frequency.split('-')[0].strip())
            if frequency_time > 0:
                bot.reply_to(message, f"SENDING UPDATES EVERY {frequency_time} MINUTES")
                def send_update(chat_id):
                    bot.send_message(chat_id, get_price())
                job = schedule.every(frequency_time).minutes.do(lambda: send_update(message.chat.id))
                scheduled_jobs[message.chat.id] = job
            elif frequency_time == 0:
                bot.reply_to(message, "STOPPING AUTO UPDATES")
                stop_schedule(message.chat.id)
        else:
            bot.reply_to(message, "WRONG INPUT")

def stop_schedule(chat_id):
    if chat_id in scheduled_jobs:
        schedule.cancel_job(scheduled_jobs[chat_id])
        del scheduled_jobs[chat_id]
        bot.send_message(chat_id, "AUTO UPDATES STOPPED")
    else:
        bot.send_message(chat_id, "NO ACTIVE UPDATES TO STOP")

def run_scheduler():
    while True:
        schedule.run_pending()
        sleep(1)

threading.Thread(target=run_scheduler).start()

bot.infinity_polling()