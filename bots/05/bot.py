import config
import telebot
import animals
import random

# Импортируем типы из модуля, чтобы создавать кнопки
from telebot import types

bot = telebot.TeleBot(config.token)

# Обработчик нажатий на кнопки
@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
  # Если нажали на одну из 12 кнопок — выводим гороскоп
  if call.data == "oven": 
    # Формируем гороскоп
    msg = "Овен:" + random.choice(animals.first) + ' ' + random.choice(animals.second) + ' ' + random.choice(animals.second_add) + ' ' + random.choice(animals.third)
    # Отправляем текст в Телеграм
    bot.send_message(call.message.chat.id, msg)
  elif call.data == "telec": 
    # Формируем гороскоп
    msg = "Телец:" + random.choice(animals.first) + ' ' + random.choice(animals.second) + ' ' + random.choice(animals.second_add) + ' ' + random.choice(animals.third)
    # Отправляем текст в Телеграм
    bot.send_message(call.message.chat.id, msg)

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
  if message.text == "Привет":
      bot.send_message(message.from_user.id, "Привет, сейчас я расскажу тебе гороскоп на сегодня.")

      # Готовим кнопки
      keyboard = types.InlineKeyboardMarkup()

      # По очереди готовим текст и обработчик для каждого знака зодиака
      key_oven = types.InlineKeyboardButton(text='Овен', callback_data='oven')
      # И добавляем кнопку на экран
      keyboard.add(key_oven)

      key_telec = types.InlineKeyboardButton(text='Телец', callback_data='telec')
      keyboard.add(key_telec)
      
      # Показываем все кнопки сразу и пишем сообщение о выборе
      bot.send_message(message.from_user.id, text='Выбери свой знак зодиака', reply_markup=keyboard)
      
  elif message.text == "/help":
      bot.send_message(message.from_user.id, "Напиши Привет")
  else:
      bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")

if __name__ == '__main__':
     bot.infinity_polling()
