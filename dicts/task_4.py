# !/usr/bin/env python3
# coding: utf-8

# 4. Написать программу, сливающую произвольное количество словарей. Повторяющиеся ключи должны
#  переименовываться с добавлением цифры. Например ключ "key", присутсвующий в нескольких словарях
#  должен быть заменён на "key-1", "key-2" и т.д.


def dict_merge(*args):
    dict_sum = {}
    index = 0
    for i in args:
        z = list(i.keys())
        for j in range(len(z)):
            if dict_sum.get(z[j]) == None:
                continue
            else:
                dict_sum[z[j] + str(index)] = dict_sum.get(z[j])
        dict_sum.update(i)
        index += 1
        z.clear()
    return dict_sum


d1 = {'q': 1, 'w': 2, 'e': 1, 'r': 4}
d2 = {'t': 1, 'y': 1, 'q': 2, 'e': 2}
d3 = {'t': 2, 'z': 1, 'q': 3, 'x': 5, 'e': 43, 'w': 4}
d5 = {'a': 32, 'q': 23}


d4 = dict_merge(d1, d2, d3, d5)
print(d4)
