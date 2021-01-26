import telebot
from threading import Thread

TOKEN = "1124654910:AAG3whPcDrG8cCtaA9ESQApYUrRKhVJqJ_8"
bot = telebot.TeleBot(TOKEN)
str = 'hy'
id_chat = 402919227


@bot.message_handler(commands=['start'])
def start(message):
    sent = bot.send_message(message.chat.id, str)
    bot.register_next_step_handler(sent, hello)
    print(message.chat.id)


def hello(message):
    bot.send_message(message.chat.id, 'Привет, {name}. Рад тебя видеть.'.format(name=message.text))


Thread(target=bot.polling, args=(True,)).start()
while True:
    str = input("Write message: ")
    bot.send_message(id_chat, str)

