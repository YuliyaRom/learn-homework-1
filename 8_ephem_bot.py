"""
Домашнее задание №1

Использование библиотек: ephem

* Установите модуль ephem
* Добавьте в бота команду /planet, которая будет принимать на вход
  название планеты на английском, например /planet Mars
* В функции-обработчике команды из update.message.text получите
  название планеты (подсказка: используйте .split())
* При помощи условного оператора if и ephem.constellation научите
  бота отвечать, в каком созвездии сегодня находится планета.

"""
import logging

import ephem

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

logging.basicConfig(filename = "bot.log", level = logging.INFO)
today = "2022/09/10"
solar_system = {'Sun': ephem.Sun(today), 
                'Moon': ephem.Moon(today), 
                'Mercury': ephem.Mercury(today), 
                'Venus': ephem.Venus(today), 
                'Mars': ephem.Mars(today),
                'Jupiter': ephem.Jupiter(today),
                'Saturn': ephem.Saturn(today), 
                'Uranus': ephem.Uranus(today), 
                'Neptune': ephem.Neptune(today),
                'Pluto': ephem.Pluto(today)}



def greet_user(update, context):
    text = 'Вызван /start'
    print(text)
    update.message.reply_text('Здравствуй, пользователь!')


def talk_to_me(update, context):
    user_text = update.message.text
    print(user_text)
    update.message.reply_text(user_text)




def planet(update, context):
  planet_name = update.message.text.split()[1]
  user_planet = solar_system.get(planet_name,None)
  if user_planet != None:
    const= ephem.constellation(solar_system[planet_name])
    update.message.reply_text(const[1])
  else:
    update.message.reply_text('Такой планеты в солнечной системе нет')

def main():
    mybot = Updater("5608339575:AAH12yxoQsX91ugHBaHrSp2sWw7nBt2ltgo",use_context = True)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(MessageHandler(Filters.text, planet))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":
    main()
