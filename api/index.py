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
        f"Welcome **{message.from_user.first_name}** to **TrustOrScam **! 🛡️\n\n"
        "Verify IDs, report scams, and stay safe in the digital world. "
        "Use our professional tools to check credibility instantly.\n\n"
        "Click the button below to launch the app and start searching!"
    )
    
    bot.send_message(
        message.chat.id, 
        welcome_text, 
        reply_markup=markup, 
        parse_mode="Markdown"
    )
