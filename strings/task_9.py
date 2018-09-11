# !/usr/bin/env python3
# coding: utf-8

# 9 Написать программу, которая определяет введено ли число или слово. Если невозможно определить, то повторить ввод.

string_input = input('введите что-нибудь: ')
while string_input.isalpha() is False and string_input.isdigit() is False:
    string_input = input('принимаются либо цифры, либо буквы: ')
if string_input.isalpha():
    print(string_input, '- вы ввели слово')
elif string_input.isdigit():
    print(string_input, '- вы ввели число')

