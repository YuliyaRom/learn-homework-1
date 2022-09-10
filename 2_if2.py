"""

Домашнее задание №1

Условный оператор: Сравнение строк

* Написать функцию, которая принимает на вход две строки
* Проверить, является ли то, что передано функции, строками. 
  Если нет - вернуть 0
* Если строки одинаковые, вернуть 1
* Если строки разные и первая длиннее, вернуть 2
* Если строки разные и вторая строка 'learn', возвращает 3
* Вызвать функцию несколько раз, передавая ей разные праметры 
  и выводя на экран результаты"""

def main(a,b):
  if not isinstance(a, str) or not isinstance(b, str):
    return 0
  elif len(a) == len(b):
    return 1
  elif len(a) != len(b) and b.lower() == "learn":
    return 3
  elif len(a) > len(b):
    return 2
  



print(main("cat", 1)) #0
print(main("cat", "lac")) #1
print(main("qwer", "asd")) #2
print(main("zxddddddd","learn")) #3