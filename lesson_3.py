import telebot
from telebot import types

bot = telebot.TeleBot('6846039420:AAFppwewq6ea0xPDzaYZ1qmK0EfINFdBs3I')

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Привет! Я бот, который отправляет лучшых немцев в формате jpg, /BMW или /Mercedes. ")


@bot.message_handler(commands=['BMW'])
def send_photo(message):
    chat_id = message.chat.id

    markup = types.InlineKeyboardMarkup()
    item = types.InlineKeyboardButton("Перейти по ссылке", url="https://ru.wikipedia.org/wiki/BMW_E34")
    markup.add(item)

    @bot.message_handler(commands=['BMW'])
    def start(message):
        bot.send_message(message.chat.id, "Нажмите на кнопку для перехода по ссылке:", reply_markup=markup)

        bot.polling()

    photo = open('./img/e34.jpeg', 'rb')
    bot.send_photo(chat_id, photo)



@bot.message_handler(commands=['Mercedes'])
def send_photo1(message):
    chat_id = message.chat.id


    photo1 = open('./img/W210_E55_AMG.jpg', 'rb')
    bot.send_photo(chat_id, photo1)




bot.polling()
