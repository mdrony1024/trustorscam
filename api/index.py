import telebot
from flask import Flask, request

TOKEN = '8276016320:AAH82uoHR6FlWBmyBQTDjnWW7DSpCYt-3fk'
bot = telebot.TeleBot(TOKEN, threaded=False)
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
    markup = telebot.types.InlineKeyboardMarkup()
    web_app_url = "https://trustorscam.vercel.app/" 
    btn = telebot.types.InlineKeyboardButton(text="অ্যাপ ওপেন করুন ✨", web_app=telebot.types.WebAppInfo(url=web_app_url))
    markup.add(btn)
    bot.send_message(message.chat.id, "স্বাগতম! কাজ শুরু করতে নিচের বাটনে ক্লিক করুন।", reply_markup=markup)

# এটি Vercel এর জন্য বাধ্যতামূলক
@app.route('/')
def index():
    return "Bot is running..."
