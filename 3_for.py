"""

Домашнее задание №1

Цикл for: Продажи товаров

* Дан список словарей с данными по колличеству проданных телефонов
  [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ]
* Посчитать и вывести суммарное количество продаж для каждого товара
* Посчитать и вывести среднее количество продаж для каждого товара
* Посчитать и вывести суммарное количество продаж всех товаров
* Посчитать и вывести среднее количество продаж всех товаров
"""

def main(lst):

  print(sum (lst[0]['items_sold'])) #суммарное количество продаж для iPhone 12
  print(sum(lst[1]['items_sold'])) #суммарное количество продаж для Xiaomi Mi11
  print(sum(lst[2]['items_sold']))#суммарное количество продаж для Samsung Galaxy 21
  print(sum (lst[0]['items_sold'])/len(lst[0]['items_sold']))#среднее количество продаж для для iPhone 12
  print(sum (lst[1]['items_sold'])/len(lst[1]['items_sold']))#среднее количество продаж для Xiaomi Mi11
  print(sum (lst[2]['items_sold'])/len(lst[2]['items_sold']))#среднее количество продаж для Samsung Galaxy 21
  print(sum (lst[0]['items_sold']) + sum(lst[1]['items_sold']) + sum(lst[2]['items_sold'])) #суммарное количество продаж всех товаров
  print(sum (lst[0]['items_sold']) + sum(lst[1]['items_sold']) + sum(lst[2]['items_sold']) / (len(lst[0]['items_sold'])  + len(lst[1]['items_sold']) + len(lst[2]['items_sold'])))

 
stock = [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ] 

main(stock)