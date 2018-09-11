# !/usr/bin/env python3
# coding: utf-8

# 6. Написать программу, сравнивающую два списка. Элементы списков могут иметь
#  разный порядок следования. Т.е. если списки содержат одинаковый набор значений,
#  то функция должна возвращать True, иначе - False, независимо от порядка следования элементов в списках.


def comparison(list1, list2):
    list1.sort()
    list2.sort()
    if len(list1) == len(list2):
        for i in range(len(list1)):
            if list1[i] == list2[i]:
                continue
            else:
                return False
        return True
    else:
        return False
