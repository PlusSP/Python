# !/usr/bin/env python3
# coding: utf-8
#
# 1 Написать программу принимающую от пользователя список чисел и суммирующая их.
#   Нельзя использовать встроенную функцию суммирования.


def numbers_sum(list1):
    x = 0
    for i in range(len(list1)):
        x += list1[i]
    return x


def list_input():
    list1 = list()
    while True:
        user_input = input("enter a number in list or 'done' to finish: ")
        try:
            list1.append(int(user_input))
        except ValueError:
            if user_input == 'done':
                break
            else:
                continue
    return list1
