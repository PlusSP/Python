# !/usr/bin/env python3
# coding: utf-8

# 4. Написать программу, сливающую произвольное количество словарей. Повторяющиеся ключи должны
#  переименовываться с добавлением цифры. Например ключ "key", присутсвующий в нескольких словарях
#  должен быть заменён на "key-1", "key-2" и т.д.


def dict_input():
    d1 = {}
    while True:
        key_input = input("enter key: ")
        if key_input == 'done':
            break
        else:
            value_input = input('enter value: ')
            if key_input.isalpha():
                if value_input.isdigit():
                    d1[key_input] = int(value_input)
                else:
                    continue
            else:
                continue
    return d1


# 1. Написать программу, которая принимает от пользователя пары ключей (строка) и значений (число)
#  и выводит на экран указанные пары построчно, а также общее количество пар.
def dict_strins_output(d1):
    i = 0
    for key, value in d1.items():
        print(key, value)
        i += 1
    return "number of pairs: " + str(i)
