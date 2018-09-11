# !/usr/bin/env python3
# coding: utf-8


# 6. Написать программу, удаляющую все дублирующиеся значения в словаре.
def dict_repeats_sort_value(d1):
    d2 = {}
    l1 = []
    for key, value in d1.items():
        l1.append(value)
        if l1.count(value) > 1:
            continue
        else:
            d2[key] = value
    return d2
