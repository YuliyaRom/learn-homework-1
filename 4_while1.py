"""

Домашнее задание №1

Цикл while: hello_user

* Напишите функцию hello_user(), которая с помощью функции input() спрашивает 
  пользователя “Как дела?”, пока он не ответит “Хорошо”
   
"""


def hello_user(a):
  while True:
    user_say = input("Как дела? ")
    if user_say == "Хорошо":
      break


b = input("Как дела?")
hello_user(b)
