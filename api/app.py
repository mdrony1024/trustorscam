import os
from flask import Flask, request
import telebot

# আপনার বোট টোকেন
TOKEN = '8276016320:AAH82uoHR6FlWBmyBQTDjnWW7DSpCYt-3fk'
bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)

@app.route('/api/webhook', methods=['POST'])
def webhook():
    if request.headers.get('content-type') == 'application/json':
        json_string = request.get_data().decode('utf-8')
        update = telebot.types.Update.de_json(json_string)
        bot.process_new_updates([update])
        return "OK", 200
    return "Forbidden", 403

@bot.message_handler(commands=['start'])
def start(message):
    name = message.from_user.first_name
    markup = telebot.types.InlineKeyboardMarkup()
    # আপনার অ্যাপের বর্তমান লিঙ্ক
    web_app_url = "https://trustorscam.vercel.app/" 
    
    btn = telebot.types.InlineKeyboardButton(
        text="অ্যাপ ওপেন করুন ✨", 
        web_app=telebot.types.WebAppInfo(url=web_app_url)
    )
    markup.add(btn)
    
    welcome_text = (
        f"স্বাগতম **{name}**!\n\n"
        "**TrustOrScam Pro**-তে আপনাকে স্বাগতম।\n"
        "নিচের বাটনে ক্লিক করে কাজ শুরু করুন।"
    )
    bot.send_message(message.chat.id, welcome_text, reply_markup=markup, parse_mode="Markdown")
