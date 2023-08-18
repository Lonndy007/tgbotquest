# -*- coding: utf-8 -*-
import telebot
import requests
import json
from config import TOKEN
from telebot import types
import time
bot = telebot.TeleBot(TOKEN)

class Message:
    def __init__(self,question,answer,btn1,btn2,btn3,btn4):
        self.question = question
        self.answer = answer
        self.btn1 = btn1
        self.btn2 = btn2
        self.btn3 = btn3
        self.btn4 = btn4

        @bot.message_handler(commands=['quest'])
        def start(message):
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            button = types.KeyboardButton('Дальше')
            markup.add(button)
            bot.send_message(message.from_user.id, 'поехали', reply_markup=markup)


        @bot.message_handler(content_types=['text'])
        def send(message):
            kb = types.InlineKeyboardMarkup()
            kb.add(types.InlineKeyboardButton(text=self.btn1, callback_data="1"))
            kb.add(types.InlineKeyboardButton(text=self.btn2, callback_data="2"))
            kb.add(types.InlineKeyboardButton(text=self.btn3, callback_data="3"))
            kb.add(types.InlineKeyboardButton(text=self.btn4, callback_data="4"))
            bot.send_message(message.chat.id, self.question, reply_markup=kb)

            @bot.callback_query_handler(func=lambda call: True)
            def callback_inline(call):
                if call.message:
                    if call.data == "1":
                        bot.send_message(call.message.chat.id, "Правильно!")
                        bot.send_message(call.message.chat.id, self.answer)
                        send(call.message)
                    elif call.data == "2":
                        bot.send_message(call.message.chat.id, "Неправильно")
                        bot.send_message(call.message.chat.id, self.answer)
                        send(call.message)

                    elif call.data == "3":
                        bot.send_message(call.message.chat.id, "Неправильно")
                        bot.send_message(call.message.chat.id, self.answer)
                        send(call.message)

                    elif call.data == "4":
                        bot.send_message(call.message.chat.id, "Неправильно")
                        bot.send_message(call.message.chat.id, self.answer)
                        send(call.message)






question1 = 'why'
answer1 = 'because'
btn1_1 = 'потому что'
btn2_1 = 'зачем'
btn3_1 = 'так'
btn4_1 = 'вот'

question2 = 'зачем'
answer2 = 'because'
btn1_2 = 'поава'
btn2_2 = 'зафыф'
btn3_2 = 'та4'
btn4_2 = 'вот'

q1 = Message(question1,answer1,btn1_1,btn2_1,btn3_1,btn4_1)
q2 = Message(question2,answer2,btn1_2,btn2_2,btn3_2,btn4_2)




bot.polling(none_stop=True)