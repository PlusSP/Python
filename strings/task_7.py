# !/usr/bin/env python3
# coding: utf-8

# 7 Написать программу, которая принимает строку и число, делит её на равные части указанного размера и выводит полученные фрагменты в обратном порядке.
#   Если крайний фрагмент содержит меньше символов чем указано, то дополнить его до нужного количества пробелами.

string_input = input('введите строку: ')
parts_length = int(input('введите длину срезов: '))
num_parts = int(len(string_input)/parts_length)
print('строка', string_input, 'разделена на части по', parts_length, 'символа: ')
i = num_parts
first_index = -1
second_index = -parts_length
while i > 0:
    print(string_input[first_index:second_index-1:-1])
    first_index -= parts_length
    second_index -= parts_length
    i -= 1
if first_index >= -(len(string_input)):
    print(string_input[first_index:-600:-1].ljust(parts_length, "_"))

