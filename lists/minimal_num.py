# !/usr/bin/env python3
# coding: utf-8

# 2. Написать программу находящую минимальный и максимальный элементы в списке.
#  Элементы - числа. Нельзя использовать встроенные функции.


def minimal_num(list1):
    x_max = int(0)
    x_min = int(0)
    for i in range(len(list1)):
        if list1[i] >= x_max:
            x_max = list1[i]
        elif list1[i] <= x_min:
            x_min = list1[i]
    return str("minimal number is: "+ str(x_min) + "\nmaximum nubber is: " + str(x_max))
