# !/usr/bin/env python3
# coding: utf-8

# Задание
# 1. Написать функцию, которая принимает произвольное количество целых чисел и суммирует их.


def int_sum(*args):
    answer = 0
    for arg in args:
        answer += arg
    return answer

# 2 Написать функцию, которая принимает произвольное количество чисел и символ математической операции (+ - / *)
#  и применяет эту операцию к числам.


def int_calc(*args, **kwarg):
    answer = 0
    if '+' in kwarg.values():
        for arg in args:
            answer += arg
        return answer
    elif '-' in kwarg.values():
        for arg in args:
            answer -= arg
        return answer
    elif '/' in kwarg.values():
        for arg in args:
            answer /= arg
        return answer
    elif '*' in kwarg.values():
        for arg in args:
            answer *= arg
        return answer

# 3. Написать функцию, которая принимает выводит словарь с отступами.
# Например print_dict({'one': 1, 'two': 2}), должно вывести:
# {
# 'one': 1,
# 'two': 2
# }


def print_dict(**kwargs):
    output = "{\n"
    for key, val in kwargs.items():
        output += "\"" + str(key) + "\"" + ": " + str(val) + "\n"
    output += "}"
    return output


a = [1, 3, 4, 5, 6, 7, 23, -12]
b = {'q': 1, 'w': 2, 'e': 3}
print(int_sum(*a))
print(int_calc(*a, kwarg='+'))
print(print_dict(**b))

