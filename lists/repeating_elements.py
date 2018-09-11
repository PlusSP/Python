# !/usr/bin/env python3
# coding: utf-8

# 3. Написать программу, которая принимает список чисел и выводит оригинальный список
#  и список из неповторяющихся элементов исходного списка. Нельзя использовать set.


def repeat(list1):
    list2 = list1[:]
    i = 0
    list1.reverse()
    while i in range(len(list1)):
        if list1.count(list1[i]) > 1:
            list1.remove(list1[i])
        else:
            i += 1
    list1.reverse()
    return 'original list: ' + str(list2) + "\nnew list: " + str(list1)

