print("-------------")
def cut_cake(people):
    parts = 1 / people
    print(f'Каждый человек получит {parts} пирога')

cut_cake(5)

print("-------------")

#добавляем исключение деления на "ноль"

def cut_cake(people):
    try:
        parts = 1 / people
        print(f'Каждый человек получит {parts} пирога')
    except ZeroDivisionError:
        print ("Не надо делить на ноль")

cut_cake(0)

print("-------------")

#добавляем исключение деления на "строку"

def cut_cake(people):
    try:
        parts = 1 / people
        print(f'Каждый человек получит {parts} пирога')
    except ZeroDivisionError:
        print ("Не надо делить на ноль")
    except TypeError:
        print("Принимаем только числа")

cut_cake("пять")

print("-------------")

#объединяем все исключения, которые хотим обработать

def cut_cake(people):
    try:
        parts = 1 / people
        print(f'Каждый человек получит {parts} пирога')
    except (ZeroDivisionError, TypeError):
        print ("Не могу поделить")

cut_cake("пять")
cut_cake(0)
cut_cake(2)

print("-------------")

# C помощью while генерим количество людей в функцию
import random

def cut_cake(people):
    try:
        parts = 1 / people
        print(f'Каждый человек получит {parts} пирога')
    except (ZeroDivisionError, TypeError):
        print ("Не могу поделить")
while True:
    people = random.randint(1, 10)
    cut_cake(people)