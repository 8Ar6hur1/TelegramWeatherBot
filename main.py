import telebot
import requests
import json

TOKEN = telebot.TeleBot('7377688530:AAHisaC8NdG0V5Hyt1LTzYdM3XByQzK8hy8')
API = 'aded1408985dd02715b736f41042eb33'

@TOKEN.message_handler(commands=['start'])
def start(message):
    TOKEN.send_message(message.chat.id, 'Наприши назву свого міста')

@TOKEN.message_handler(content_types=['text'])
def get_weather(message):
    city = message.text.strip().lower()
    res = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}&units=metric')
    data = json.loads(res.text)
    temp = data["main"]["temp"]
    TOKEN.reply_to(message, f'Погода зараз: {temp}°C')

    if temp >= 18.0:
        image = 'summer.jpg'
    elif temp <= 17.0:
       image = 'neutral.jpg'
    elif temp <= 8.0:
        image = 'winter.jpg'
    
    file = open(f'./photo/{image}', 'rb')
    TOKEN.send_photo(message.chat.id, file)


TOKEN.polling(non_stop=True)
