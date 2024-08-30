import telebot
import random
import time
from threading import Timer

API_TOKEN = '7319489341:AAEdx9cn9zNNB7qSbxPvardcF4s9TOak8Do'
bot = telebot.TeleBot(API_TOKEN)

# Храним идентификатор сообщения и чата для обновления
message_id = None
chat_id = None
callback_message_id = None

def send_delayed_message(chat_id, message_id, text, keyboard):
    def delayed_message():
        bot.edit_message_text(
            text=text,
            chat_id=chat_id,
            message_id=message_id,
            reply_markup=keyboard
        )
    
    # Задержка в 5 секунд
    Timer(8, delayed_message).start()

# Обработка команды /start
@bot.message_handler(commands=['start'])
def send_welcome(message: telebot.types.Message):
    global message_id, chat_id
    chat_id = message.chat.id  # Сохраняем идентификатор чата
    keyboard = telebot.types.InlineKeyboardMarkup()
    button = telebot.types.InlineKeyboardButton("ЖМИ НА КНОПКУ", callback_data='button_click')
    keyboard.add(button)

    # Отправляем приветственное сообщение с эмодзи
    msg = bot.send_message(message.chat.id, 
                           "Привет! Я бот LuckyJet! 🎉\n"
                           "Хули думать - надо зарабатывать! 🚀\n"
                           "Ожидай сигнал и жми на кнопку, Инструкция : \n"
                           "🟩 Зеленый-сигнал который даст больше ,чем 2х \n"
                            "🟥 Красный-сигнал плохого коэффициента",
                           reply_markup=keyboard)
    message_id = msg.message_id  # Сохраняем идентификатор сообщения

# Обработка нажатия на кнопку
@bot.callback_query_handler(func=lambda call: call.data == 'button_click')
def button_click(call: telebot.types.CallbackQuery):
    global callback_message_id
    
    # Создаем клавиатуру с кнопкой для следующего нажатия
    keyboard = telebot.types.InlineKeyboardMarkup()
    button = telebot.types.InlineKeyboardButton("ЖМИ НА КНОПКУ", callback_data='button_click')
    keyboard.add(button)

    # Отправляем сообщение о том, что ожидаем сигнал
    bot.edit_message_text(
        text="Ожидание сигнала...",
        chat_id=call.message.chat.id,
        message_id=call.message.message_id,
        reply_markup=None
    )
    
    # Задержка в 5 секунд перед отправкой результата
    def send_result():
        # Генерация случайного числа от 1 до 100
        number = random.randint(1, 100)
        
        # Определение цвета на основе числа
        if number <= 50:
            color_emoji = "🟥"  # Красный
            color_name = "КРАСНЫЙ"
        else:
            color_emoji = "🟩"  # Зеленый
            color_name = "ЗЕЛЕНЫЙ"
        
        # Форматируем текст сообщения
        text = f"Ваш следующий сигнал ЦВЕТ: {color_name} {color_emoji}\n" \
               "ПРОПУСТИЛ СИГНАЛ? ЖМИ НА КНОПКУ"
        
        bot.edit_message_text(
            text=text,
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            reply_markup=keyboard
        )
    
    Timer(5, send_result).start()

if __name__ == '__main__':
    bot.polling(none_stop=True)
