import telebot

API_TOKEN = '7255176534:AAE9tpWC-3h32_2QLUsdjoybgOTl_JMy4ss'

bot = telebot.TeleBot(API_TOKEN)

Keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
button1 = telebot.types.KeyboardButton(text='akjol')
button2 = telebot.types.KeyboardButton(text='medina')
button3 = telebot.types.KeyboardButton(text='torokul')
button4 = telebot.types.KeyboardButton(text='erbol')
button5 = telebot.types.KeyboardButton(text='kutman')
Keyboard.add(button1,button2,button3,button4,button5)

Keyboard2 = telebot.types.InlineKeyboardMarkup()
button1 = telebot.types.InlineKeyboardButton(text='razrabotchick',callback_data='razrabotchick')

button2 = telebot.types.InlineKeyboardButton(text='Изменить',callback_data='change')
Keyboard2.add(button1,button2)


@bot.message_handler(commands=['start','help'])
def send_welcome(message):
    bot.reply_to(message, 'Hello, how i can assist you?')

@bot.message_handler(func=lambda message: message.text == 'TorokulZhanyshbekov')
def answer_message(message):
    # print(message.text)
    # bot.reply_to(message, message.text)
    bot.send_message(chat_id=message.chat.id, text=message.text,
                     reply_markup=Keyboard2)

@bot.callback_query_handler(func = lambda call: call.data == 'razrabotchick')
def save(call):
    bot.send_message(call.message.chat.id, 'ОО как ты Торо брат? все хорошо у тебя?')

@bot.callback_query_handler(func= lambda call: call.data == 'Изменить' ) 
def change(call):
    bot.send_message(call.message.chat.id, 'Нечего ты не изменишь! Только Торокул сможет изменить!!!') 

bot.infinity_polling()

