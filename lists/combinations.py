# !/usr/bin/env python3
# coding: utf-8

# 9. Написать программу выводящую все возможные комбинации пар элементов из двух списков.

def all(list1, list2):
    comb = str()
    for i in range(len(list1)):
        for j in range(len(list2)):
            comb += str(list1[i]) + ',' + str(list2[j]) + "; "
    return comb
