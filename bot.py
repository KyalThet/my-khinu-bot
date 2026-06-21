import telebot

# အောက်က နေရာနှစ်ခုမှာ မိမိရဲ့ Token နဲ့ ID အစားထိုးပါ
BOT_TOKEN = "အဆင့်၁ကရလာတဲ့_BOT_TOKEN_စာတန်းရှည်ကြီးကို_ဒီမျက်တောင်ကွင်းထဲထည့်ပါ"
ADMIN_ID = 123456789  # အဆင့်၁ကရလာတဲ့_Id_ဂဏန်းတွေကို_ဒီမှာအစားထိုးပါ (မျက်တောင်ကွင်းမလိုပါ)

bot = telebot.TeleBot(8758739646:AAEi58FJvXCfecuw0TKopHfteCnLqcP-jqw)

# User က /start နှိပ်လျှင် ပြသမည့်စာသား
@bot.message_handler(commands=['start'])
def send_welcome(message):
    welcome_text = "🙏 မင်္ဂလာပါခင်ဗျာ 🙏\nသတင်းများပေးပို့နိုင်ပါပြီခင်ဗျာ ✅"
    bot.reply_to(message, welcome_text)

# User ဆီမှ စာများကို Admin ဆီသို့ Forward လုပ်ခြင်းနှင့် User ကို Auto-Reply ပြန်ခြင်း
@bot.message_handler(func=lambda message: message.chat.id != 5934620185)
def forward_to_admin(message):
    try:
        # ၁။ Admin ဆီသို့ User ပို့လိုက်တဲ့ Message ကို လှမ်းပို့ပေးခြင်း
        bot.forward_message(5934620185, message.chat.id, message.message_id)
        bot.send_message(5934620185, f"📩 စာပို့သူ - {message.from_user.first_name} (ID: {message.chat.id})")
        
        # ၂။ စာပို့လိုက်တဲ့ User ဆီသို့ ကျေးဇူးတင်စကား ချက်ချင်း အလိုအလျောက် ပြန်ပေးခြင်း
        thanks_text = "သတင်းပေးပို့မှုအတွက်ကျေးဇူးတင်ပါတယ်ခမျာ🙏🏻☺️✨"
        bot.reply_to(message, thanks_text)
        
    except Exception as e:
        print(f"Error: {e}")

# Admin က Reply ပြန်လျှင် သက်ဆိုင်ရာ User ဆီသို့ စာပြန်ပို့ခြင်း
@bot.message_handler(func=lambda message: message.chat.id == 5934620185 andြန်ပို့ခြင်း message.reply_to_message is not None)
def reply_to_user(message):
    try:
        if message.reply_to_message.forward_from:
            user_id = message.reply_to_message.forward_from.id
            bot.send_message(user_id, message.text)
            bot.send_message(5934620185, "✅ စာပြန်ပို့ပြီးပါပြီ။")
        else:
            bot.send_message(5934620185Privacyer က Privacy ပိတ်ထားသဖြင့် စာပြန်၍မရပါ။")
    except Exception as e:
        bot.send_message(5934620185, f"❌ Error: {str(e)}")

print("Bot is running...")
bot.infinity_polling()
          
