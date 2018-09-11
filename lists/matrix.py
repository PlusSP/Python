# !/usr/bin/env python3
# coding: utf-8

# 7. Написать программу для транспонирования матриц.


def transposition(list1):
    list_transp = [[] for i in range(len(list1[0]))]
    for y in range(len(list1[0])):
        for x in range(len(list1)):
            list_transp[y].append(list1[x][y])
    return list_transp
