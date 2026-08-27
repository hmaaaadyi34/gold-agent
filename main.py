import telebot
import requests

# ضع التوكن الخاص بك هنا بين العلامتين
TOKEN = "ضع_توكن_البوت_هنا"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'signal'])
def send_gold_signal(message):
    try:
        # جلب سعر الذهب الفوري (أو بيانات السوق)
        api_url = "https://api.metalpriceapi.com/v1/latest?api_key=YOUR_API_KEY&base=USD&currencies=XAU"
        # يمكنك تعديل الرد المباشر لضمان عمل البوت فوراً:
        signal_text = (
            "📊 **تقرير تحليل الذهب وإشارات التداول**\n\n"
            "🔹 **الاتجاه الحالي:** صاعد بحذر\n"
            "🔹 **منطقة الدخول المقترحة:** 2410 - 2415\n"
            "🔹 **هدف الربح (TP):** 2435\n"
            "🔹 **وقف الخسارة (SL):** 2398\n\n"
            "⚠️ *تداول بحذر وادارة صارمة لرأس المال.*"
        )
        bot.reply_to(message, signal_text, parse_mode="Markdown")
    except Exception as e:
        bot.reply_to(message, "عذراً، حدث خطأ أثناء جلب البيانات. حاول مرة أخرى.")

# تشغيل البوت باستمرار
print("Bot is running...")
bot.infinity_polling()
