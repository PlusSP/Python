# !/usr/bin/env python3
# coding: utf-8

# 2. Используя генератор из задания (1) написать генератор, который принимает список слов и выдаёт только те,
#    длина которых менее заданной.
import task_1


def minimal_len_generator(list_words, min_len):
    new_list = []
    for i in list_words:
        if len(i) < min_len:
            new_list.append(i)
    yield new_list


def random_strings_list():
    old_list = []
    for i in range(10):
        random_string = next(task_1.random_string_gen())
        old_list.append(random_string)
    return old_list


print(next(minimal_len_generator(random_strings_list(), 10)))
