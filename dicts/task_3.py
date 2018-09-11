# !/usr/bin/env python3
# coding: utf-8


# 3. Аналогично 2, но сортировать по значениям.
def dict_sort_value_output(d1):
    l_keys = []
    for key, value in d1.items():
        l_keys.append([value, key])
    l_keys.sort()
    i = 0
    for i in range(len(l_keys)):
        l_keys[i].reverse()
        print(l_keys[i])
        i += 1
    return "number of pairs: " + str(i)