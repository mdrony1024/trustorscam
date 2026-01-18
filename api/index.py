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
    
    # English Button Text
    btn = telebot.types.InlineKeyboardButton(
        text="Open App ✨", 
        web_app=telebot.types.WebAppInfo(url=web_app_url)
    )
    markup.add(btn)
    
    # English Welcome Message
    welcome_text = (
        f"Welcome {message.from_user.first_name}!\n\n"
        "Click the button below to launch the TrustOrScam app and start exploring."
    )
    
    bot.send_message(message.chat.id, welcome_text, reply_markup=markup)

# Mandatory for Vercel
@app.route('/')
def index():
    return "Bot is running..."
