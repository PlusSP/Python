# !/usr/bin/env python3
# coding: utf-8

# 8. 8. Реализовать операции с множествами используя только списки.
# обьединение, пересечение, разность, симметричная разность.


def unite(list1, list2):
    for i in range(len(list1)):
        try:
            list2.remove(list1[i])
        except ValueError:
            continue
    list1.extend(list2)
    return list1


def intersection(l1, l2):
    inter_list = []
    for i in range(len(l1)):
        for j in range(len(l2)):
            if l1[i] == l2[j]:
                inter_list.append(l2[j])
            else:
                continue
    return inter_list


def difference(l1,l2):
    diff_list = []
    for i in range(len(l1)):
        if l1[i] not in l2:
            diff_list.append(l1[i])
        else:
            continue
    for j in range(len(l2)):
        if l2[j] not in l1:
            diff_list.append(l2[j])
        else:
            continue
    return diff_list


def symmetric_diff(l1, l2, which = 0):
    sym_diff_list = []
    if which == 0:
        for i in range(len(l1)):
            if l1[i] not in l2:
                sym_diff_list.append(l1[i])
            else:
                continue
    else:
        for j in range(len(l2)):
            if l2[j] not in l1:
                sym_diff_list.append(l2[j])
            else:
                continue
    return sym_diff_list
