# Реализовать скрипт, в котором должна быть предусмотрена функция расчета ЗП сотрудника
# В расчете необходимо использовать формулу: (выработка в часах*ставка в час) + премия
# Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами

# Вариант 1  - это расчет с конкретными значениями(168 400.5 35), их необходимо внести заранее
# в Run Configuration

import sys

file, hours, rate, bonus = sys.argv

try:
    hours = float(hours)
    rate = float(rate)
    bonus = float(bonus)
    salary_gross = (hours * rate) + (hours * rate) / 100 * bonus
    print('\n\x1b[34m', f'ЗП сотрудника с конкретными параметрами >>>\x1b[0m  {salary_gross:.2f}', '\n')
except ValueError:
    print('\n\x1b[31mНеобходимо ввести заранее конкретные значения(часы, ставка, %премии) для данного модуля\n\x1b[0m')


# Вариант 2 - это расчет в вводом параметров

def chek_numeric(user_str):
    """
    проверка ввода числа, int и float
    :param user_str: принимает только текствоу строку без input()
    :return: возвращает число

    """
    while True:
        user_numeric = input(user_str)
        if user_numeric.isdigit():
            return int(user_numeric)
        elif not user_numeric.isdigit():
            try:
                return float(user_numeric)
            except ValueError:
                print("\x1b[31m", 'Ошибка! Вводите только числа!', "\x1b[0m")
                continue


def salary_func(product_hours, rate_hour, bonus_month):
    return product_hours * rate_hour + (product_hours * rate_hour) / 100 * bonus_month


user_salary = salary_func(chek_numeric("Введите выработку в часах >>> "),

                          chek_numeric("Введите ставку в час >>> "),
                          chek_numeric("Введите % премии >>> "))
print('\n\x1b[34mЗП сотрудника с вводом параметров >>> \x1b[0m', f'{user_salary:.2f}')
