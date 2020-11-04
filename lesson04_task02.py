# Представлен список чисел, необходимо вывести элементы исходного списка,
# значения которых больше предыдущего элемента
# Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
# Результат: [12, 44, 4, 10, 78, 123]

nums_list = [551, 3200, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 555]
new_nums_list = [nums_list[x] for x in range(len(nums_list)) if nums_list[x - 1] < nums_list[x] if x != 0]
print('\n\x1b[34mИсходный список :\x1b[0m', f'  {nums_list}')
print('\x1b[34mПолученный список :\x1b[0m', f'{new_nums_list}')
