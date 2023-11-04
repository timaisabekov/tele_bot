import telebot
from telebot import types

bot = telebot.TeleBot('6846039420:AAFppwewq6ea0xPDzaYZ1qmK0EfINFdBs3I')
# #############
#
# markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
# item1 = types.KeyboardButton('Button 1')
# item2 = types.KeyboardButton('Button 2')
# markup.add(item1, item2)
#
# @bot.message_handler(commands=['start'])
# def start(message):
#     bot.send_message(message.chat.id, "Выберите опцию:", reply_markup=markup)
#
# bot.polling()


###########
markup = types.InlineKeyboardMarkup()
item = types.InlineKeyboardButton("Перейти по ссылке", url="https://www.youtube.com")
markup.add(item)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Нажмите на кнопку для перехода по ссылке:", reply_markup=markup)

bot.polling()


###########
# markup = types.InlineKeyboardMarkup()
# item1 = types.InlineKeyboardButton("Кнопка 1", callback_data="button1")
# item2 = types.InlineKeyboardButton("Кнопка 2", callback_data="button2")
# markup.add(item1, item2)
#
# @bot.callback_query_handler(func=lambda call: True)
# def handle_callback_query(call):
#     if call.data == "button1":
#         bot.send_message(call.message.chat.id, "Вы нажали на Кнопку 1")
#     elif call.data == "button2":
#         bot.send_message(call.message.chat.id, "Вы нажали на Кнопку 2")
#
# @bot.message_handler(commands=['start'])
# def start(message):
#     bot.send_message(message.chat.id, "Выберите опцию:", reply_markup=markup)
#
# bot.polling()

###########

# Обработчик команды /start
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Привет! Я бот, который может отправлять лучшие машины в 21веке. Используй команды /photo1 или /photo2.")

# Обработчик команды /photo для отправки фото
@bot.message_handler(commands=['photo1'])
def send_photo1(message):
    chat_id = message.chat.id
    photo1 = open('./img/w124.jpg', 'rb')
    bot.send_photo(chat_id, photo1)

@bot.message_handler(commands=['photo2'])
def send_photo2(message):
    chat_id = message.chat.id
    photo2 = open('./img/e34.jpg', 'rb')
    bot.send_photo(chat_id, photo2)



# Обработчик команды /video для отправки видео
@bot.message_handler(commands=['video'])
def send_video(message):
    chat_id = message.chat.id

    # Отправка видео из файла
    video = open('./video/2023-11-02 16.10.15.mp4', 'rb')  # Замените 'video.mp4' на путь к вашему видео
    bot.send_video(chat_id, video)

# Запуск бота
bot.polling()

#
# # Обработчик команды /send_link для отправки ссылки
# @bot.message_handler(commands=['send_link'])
# def send_link(message):
#     chat_id = message.chat.id
#
#     # Текст сообщения с HTML-разметкой, включая ссылку
#     message_text = "Это ссылка на [Google](https://www.google.com/)."
#
#     # Отправка сообщения с разметкой в формате HTML
#     bot.send_message(chat_id, message_text, parse_mode='HTML')
#
# # Запуск бота
# bot.polling()