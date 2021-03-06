# Реализовать формирование списка, используя функцию range() и возможности генератора
# В список должны войти четные числа от 100 до 1000 (включая границы)
# Необходимо получить результат вычисления произведения всех элементов списка.
# Подсказка: использовать функцию reduce().

from functools import reduce

print('\n\x1b[34mСписок:\x1b[0m', f'{[x for x in range(100, 1001) if x % 2 == 0]}')
print('\x1b[34mРезультат >>>\x1b[0m', f'{reduce(lambda x, y: x * y, [x for x in range(100, 1001) if x % 2 == 0])}')
