import telebot
from telebot import types

bot = telebot.TeleBot("YOUR TOKEN HERE!")

@bot.message_handler(commands=["start"])
def start(message):
   app_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
   app_keyboard = types.KeyboardButton(text="Отправить заявку")
   app_markup.add(app_keyboard)
   chat_id = message.chat.id
   first_name = message.chat.first_name
   bot.send_message(chat_id, f"Привет {first_name} !\n"
                             f"Тут вы можете отправить заявку для вступления в группу с майнером. Нажмите на кнопку подать заявку ниже.", reply_markup=app_markup)

@bot.message_handler(content_types=["text"])
def text(message):
   chat_id = message.chat.id
   if message.chat.type == 'private':
      if message.text == 'Отправить заявку':
         bot.send_message(chat_id, "Для чего вы хотите вступить в команду?\nГде вы о нас узнали?\nВаш дискорд/телеграмм\nГотовы ли вы стабильно оплачивать подписку майнера? ")
         bot.register_next_step_handler(message, send_z)

def send_z(message):
   first_name = message.chat.first_name
   chat_id = message.chat.id
   user_name = message.chat.username
   z = message.text
   admin_id = [1234556678, 131414451515 ] #u need to put ur telegram id here
   app_text = []
   app_text.append(z)
   for i in admin_id:
      bot.send_message(i, f"Поступила заявка от {message.chat.first_name} !\n"
                                 f"Его телеграм = @{message.chat.username}\n"
                                 f"Его текст:\n"
                                 f"{app_text}")

   app_text.clear()
   bot.send_message(chat_id, "Заявка отправлена!")

bot.polling(none_stop=True)