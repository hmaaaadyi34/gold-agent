import os
import telebot
from flask import Flask, request

TOKEN = "8781905942:AAGLTamnVzvtgb1En1K7lWw4LTEbrkw458Y"
bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)

@app.route(f'/{TOKEN}', methods=['POST'])
def webhook():
    json_str = request.get_data().decode('UTF-8')
    update = telebot.types.Update.de_json(json_str)
    bot.process_new_updates([update])
    return '!', 200

@app.route('/')
def index():
    return 'Bot is alive!'

@bot.message_handler(commands=['start', 'signal'])
def send_gold_signal(message):
    signal_text = (
        "📊 **تقرير تحليل الذهب وإشارات التداول**\n\n"
        "🔹 **الاتجاه الحالي:** صاعد بحذر\n"
        "🔹 **منطقة الدخول المقترحة:** 2410 - 2415\n"
        "🔹 **هدف الربح (TP):** 2435\n"
        "🔹 **وقف الخسارة (SL):** 2398\n\n"
        "⚠️ *تداول بحذر وإدارة صارمة لرأس المال.*"
    )
    bot.reply_to(message, signal_text, parse_mode="Markdown")

if __name__ == '__main__':
    # ربط الـ Webhook تلقائيا مع Railway
    railway_url = os.environ.get('RAILWAY_STATIC_URL')
    if railway_url:
        bot.remove_webhook()
        bot.set_webhook(url=f'https://{railway_url}/{TOKEN}')
    
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
