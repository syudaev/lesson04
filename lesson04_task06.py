# Реализовать два небольших скрипта:
# - итератор, генерирующий целые числа, начиная с указанного,
# - итератор, повторяющий элементы некоторого списка, определенного заранее
# Подсказка: использовать функцию count() и cycle() модуля itertools
# обратите внимание, что создаваемый цикл не должен быть бесконечным, необходимо предусмотреть условие его завершения
# Например, в первом задании выводим целые числа, начиная с 3, а при достижении числа 10 завершаем цикл
# Во втором также необходимо предусмотреть условие, при котором повторение элементов списка будет прекращено

from itertools import count
from itertools import cycle


def chek_numeric(user_str):
    """
    проверка ввода числа int
    :param user_str: принимает только текствоу строку без input()
    :return: возвращает целое число
    """
    while True:
        user_numeric = input(user_str)
        if user_numeric.isdigit() and int(user_numeric) < 21:
            return int(user_numeric)
        else:
            print("\x1b[31m", 'Ошибка! Только целые положительные числа от 1 до 20!', "\x1b[0m")
            continue


for i in count(chek_numeric('Генерация целых чисел, начиная с указанного до 20 >>> '), 1):
    if i > 20:
        break
    else:
        print('\x1b[34m>>> \x1b[0m', i)

count = 1
my_list = ['Берлога', False, 44.134, 'Тимофей', None, 'L', 'i', 1008, True]
print('\n', my_list)
print('\x1b[34mПовторение элементов списка не более 30 раз:\x1b[0m')
for item in cycle(my_list):
    if count > 30:
        break
    print(item)
    count += 1
