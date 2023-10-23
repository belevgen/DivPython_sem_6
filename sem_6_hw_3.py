# Задание 4.
# Напишите функцию в шахматный модуль. Используйте генератор случайных чисел для случайной расстановки ферзей в задаче выше.
# Проверяйте различный случайные варианты и выведите 4 успешных расстановки.

import random
from sem_6_hw_2 import validate_queens

def generate_positions():
    positions = list(range(1, 9))              # создаём список с числами от 1 до 8
    for i in range(4):                         # 4 успешные расстановки
        random.shuffle(positions)              # перемешиваем список
        while not validate_queens(positions):  # если расстановка не успешная, перемешиваем ещё раз
            random.shuffle(positions)
        print(positions)                       # выводим успешную расстановку
