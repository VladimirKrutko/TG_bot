import telebot
from pulseapi import *

host = "192.168.0.178:8081"
robot = RobotPulse(host)
bot = telebot.TeleBot('1288826859:AAHblZK6uuq4Ezd6dXD7IRrmMIybMjGGcx8')


@bot.message_handler(content_types=['text'])
def test(message):
    if message.text =="zg":
        robot.zg_on()
    bot.send_message(message.chat.id, message.text)


bot.polling(none_stop=True)
