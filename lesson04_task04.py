# Представлен список чисел, определить элементы списка, не имеющие повторений
# Сформировать итоговый массив чисел, соответствующих требованию. Элементы вывести
# в порядке их следования в исходном списке, для выполнения задания обязательно использовать генератор.
# Пример исходного списка: [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
# Результат: [23, 1, 3, 10, 4, 11]

my_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
print('\n\x1b[34mИсходный список >>>\x1b[0m', f'{my_list}')
print('\x1b[34mЭлементы, не имеющие повторений >>>\x1b[0m',
      f'{[x for x in my_list if my_list.count(x) == 1]}')
