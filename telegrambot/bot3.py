import telebot
from telebot import types
from kaktusmedia import get_list_news, get_one_new, get_photo 

TOKEN = '7143078698:AAH6-vi9_wvOtNdIDkjqtkZfO-b0Z3kvKZ4'
bot = telebot.TeleBot(TOKEN)

firs_button = types.InlineKeyboardMarkup()
btn1 = types.InlineKeyboardButton('Description', callback_data='description')
btn2 = types.InlineKeyboardButton('Photo', callback_data='photo')
btn3 = types.InlineKeyboardButton('Quit', callback_data='quit')
firs_button.add(btn1, btn2, btn3)


news_menu = types.ReplyKeyboardMarkup()
btn_news = types.KeyboardButton('Все новости')
news_menu.add(btn_news)

num_of_new = 0

@bot.message_handler(commands=['start'])
def start(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, 'Привет, я новостной бот! Нажмите "Все новости", чтобы получить список новостей.', reply_markup=news_menu)

@bot.message_handler(func=lambda message: message.text == 'Все новости')
def list_news(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, get_list_news())
    bot.send_message(chat_id, 'Введите номер новости для получения подробностей: ')

@bot.message_handler(content_types=['text'])
def handle_text(message):
    global num_of_new
    chat_id = message.chat.id
    num_of_new = int(message.text)
    bot.send_message(chat_id, 'Выберите фото или описание какой-либо новости: ', reply_markup=firs_button)

@bot.callback_query_handler(func=lambda c: True)
def get_description_or_photo(c):
    chat_id = c.message.chat.id
    if c.data == 'description':
        bot.send_message(chat_id, get_one_new(num_of_new))
    elif c.data == 'photo':
        bot.send_message(chat_id, get_photo(num_of_new))
    elif c.data == 'quit':
        bot.send_message(chat_id, 'До свидания')

bot.polling()
