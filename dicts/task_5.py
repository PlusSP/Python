# !/usr/bin/env python3
# coding: utf-8


# 5. Написать программу, которая фильтрует словарь с целыми значениями. Удалять все ключи значения в которы меньше указанного.
def dict_sort_by_value(d1, min):
    d2 = {}
    for key, value in d1.items():
        if value >= min:
            d2[key] = value
        else:
            continue
    return d2
