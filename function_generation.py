# -*- config: utf8 -*-

# Генерация функций в зависимости от переданных параметров.
# С помощью функции eval() уменьшился объём кода за счёт уменьшения количества определений функций математических
# операций и уменьшения количества условных выражений
def creating_mathematical_operations(operator):
    all_operators = ['+', '-', '*', '/', '>', '<', '%',
                     '//', '**', '**0.5', '==', '<=', '>=', ]

    if operator in all_operators:
        def mathematical_operation(a, b):
            if operator == '**0.5':
                result = eval(f'{a} {operator}')
                return result
            else:
                result = eval(f'{a} {operator} {b}')
                return result

        return mathematical_operation


# Функция оптимизирующая передачу параметров в функцию ВП и функцию НП
def full_calculation(sign, first_number, second_number):
    mathematical_func = creating_mathematical_operations(sign)
    return mathematical_func(first_number, second_number)


# Имитация пользовательского ввода
input_sign = input('Введите математический символ: ')
if input_sign == '**0.5':
    input_second_number = None
    input_first_number = input('Введите первое число: ')
    value_calculation = full_calculation(sign=input_sign, first_number=input_first_number,
                                         second_number=input_second_number)
    print(value_calculation)
else:
    input_first_number = input('Введите первое число: ')
    input_second_number = input('Введите второе число: ')
    value_calculation = full_calculation(sign=input_sign, first_number=input_first_number,
                                         second_number=input_second_number)
    print(value_calculation)
