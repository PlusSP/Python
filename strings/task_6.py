# !/usr/bin/env python3
# coding: utf-8

# 6 Написать программу, которая принимает строку и число, делит её на равные части и меняет их местами.

string_input = input('введите строку: ')
num_input = int(input('введите количество срезов: '))
parts_length = int(len(string_input)/num_input)
print('строка', string_input, 'разделена на', num_input, 'части: ')
first_index = int(len(string_input)) - parts_length
second_index = len(string_input)
i = num_input
while i > 0:
    print(string_input[first_index:second_index])
    first_index -= parts_length
    second_index -= parts_length
    i -= 1
if first_index >= 0:
    print('остаток:', string_input[0:(len(string_input) % num_input)])

