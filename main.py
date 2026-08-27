import telebot
import requests

TOKEN = "8781905942:AAGLTamnVzvtgb1En1K7lWw4LTEbrkw458Y"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'signal'])
def send_gold_signal(message):
    try:
        signal_text = (
            "📊 **تقرير تحليل الذهب وإشارات التداول**\n\n"
            "🔹 **الاتجاه الحالي:** صاعد بحذر\n"
            "🔹 **منطقة الدخول المقترحة:** 2410 - 2415\n"
            "🔹 **هدف الربح (TP):** 2435\n"
            "🔹 **وقف الخسارة (SL):** 2398\n\n"
            "⚠️ *تداول بحذر وإدارة صارمة لرأس المال.*"
        )
        bot.reply_to(message, signal_text, parse_mode="Markdown")
    except Exception as e:
        bot.reply_to(message, "عذراً، حدث خطأ أثناء جلب البيانات. حاول مرة أخرى.")

print("Bot is running...")
bot.infinity_polling()
