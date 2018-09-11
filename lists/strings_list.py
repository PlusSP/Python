# !/usr/bin/env python3
# coding: utf-8

# 5. Написать программу принимающую от пользователя список строк и число и выводящую
#  новый список из слов, длина которой меньше указанного числа.


def max_length(list1, max_len):
    i = 0
    while i in range(len(list1)):
        if len(list1[i]) > max_len:
            list1.remove(list1[i])
        else:
            i += 1
    return list1


def list_of_strings():
    list1 = list()
    while True:
        user_input = input("enter string to add in list or 'done' to finish: ")
        if user_input == 'done':
            break
        else:
            list1.append(user_input)
    return list1

