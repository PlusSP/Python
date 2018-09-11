# !/usr/bin/env python3
# coding: utf-8


# 1. Написать генератор, который генерирует случайные полседовательности сисмволов, случайной длины от 1 до 20.
import random


def random_string_gen():
    length = random.randint(0, 20)
    new_string = ""
    for i in range(length):
        new_string += random.choice('ABCDEFGHIKLMNOPQRSTVXYZabcdefghijklmnopqrstuvwxyz1234567890')
    yield new_string


for i in range(10):
    random_string = next(random_string_gen())
    print(random_string)