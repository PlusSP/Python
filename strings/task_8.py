# !/usr/bin/env python3
# coding: utf-8

# 8 Написать программу, которая принимает строку и выводит её в таком виде, что чётные буквы в верхнем регистре, а нечётные в нижнем.

string_input = input('введите строку: ')
while string_input.isalpha() is False:
    string_input = input('принимаются только буквенные символы: ')
i = len(string_input)
new_string = str()
j = 0
while i > 0:
    if j % 2 == 0:
        new_string += string_input[j].upper()
    else:
        new_string += string_input[j].lower()
    i -= 1
    j += 1
print(new_string)

