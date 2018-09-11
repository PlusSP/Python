# !/usr/bin/env python3
# coding: utf-8

# 4. Написать программу, которая при запуске при каждом нажатии **ENTER** выводит случайную последовательность
#    символов заданной длины.
import random


def random_string_gen():
    length = 20
    new_string = ""
    for i in range(length):
        new_string += random.choice('ABCDEFGHIKLMNOPQRSTVXYZabcdefghijklmnopqrstuvwxyz1234567890')
    yield new_string


while True:
    user_input = input('нажмите "Enter" или любой символ для завершения:\n')
    if user_input != '':
        break
    else:
        print(next(random_string_gen()))
