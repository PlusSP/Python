# !/usr/bin/env python3
# coding: utf-8

# 4. Написать аналог метода sort для списка чисел.


def sort(list1):
    for i in range(len(list1)-1, 0, -1):
        for j in range(i):
            if list1[j] > list1[j+1]:
                temp = list1[j]
                list1[j] = list1[j+1]
                list1[j+1] = temp
    return list1

