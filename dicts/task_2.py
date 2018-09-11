# !/usr/bin/env python3
# coding: utf-8


# 2. Программа из задания 1, но элементы должны выводится в отсортированном виде (по ключам).
def dict_sort_key_output(d1):
    l_keys = []
    for key, value in d1.items():
        l_keys.append([key, value])
    l_keys.sort()
    i = 0
    for i in range(len(l_keys)):
        print(l_keys[i])
        i += 1
    return "number of pairs: " + str(i)