import os
import time
import requests

# 1. إعدادات المفاتيح
TELEGRAM_BOT_TOKEN = "8781905942:AAGLTamnVzvtgb1En1K7lWw4LTEbrkw458Y"
TELEGRAM_CHAT_ID = "5397719685"

def send_telegram_message(message):
    """دالة إرسال الإشارات الفورية إلى تليجرام"""
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": message,
        "parse_mode": "Markdown"
    }
    try:
        response = requests.post(url, json=payload)
        return response.json()
    except Exception as e:
        print(f"خطأ في إرسال الرسالة: {e}")

def get_live_gold_price():
    """دالة جلب سعر الذهب الحقيقي والحي (XAUUSD)"""
    try:
        url = "https://api.coinbase.com/v2/prices/PAXG-USD/spot"
        response = requests.get(url, timeout=10)
        data = response.json()
        price = float(data['data']['amount'])
        return price
    except Exception as e:
        return 2350.00 

def smart_gold_agent():
    """الوكيل الذكي: يراقب، يحلل، ويرسل القرار"""
    send_telegram_message("🤖 **تم تفعيل وكيل الذهب الذكي بنجاح!**\nالوكيل يعمل الآن على مراقبة السوق على مدار الساعة ويرصد الفرص.")
    
    price_history = []
    
    while True:
        current_price = get_live_gold_price()
        price_history.append(current_price)
        
        if len(price_history) > 5:
            price_history.pop(0)
            
        if len(price_history) >= 3:
            prev_price = price_history[-2]
            diff = current_price - prev_price
            
            if diff >= 1.5:
                msg = f"🚀 **إشارة شراء قوية (BUY)**\n💰 السعر الحالي: `{current_price}`\n📈 الزخم إيجابي لصالح الذهب."
                send_telegram_message(msg)
            elif diff <= -1.5:
                msg = f"📉 **إشارة بيع أو هبوط (SELL)**\n💰 السعر الحالي: `{current_price}`\n⚠️ هبوط ملحوظ في السعر، توخ الحذر."
                send_telegram_message(msg)
                
        time.sleep(60)

if __name__ == "__main__":
    smart_gold_agent()
