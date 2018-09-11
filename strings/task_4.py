# !/usr/bin/env python3
# coding: utf-8

# *4. Написать программу, которая принимает от пользователя текстовую строку и выводит на экран все символы, которые в ней встречаются и количество их вхождений.

# Пример:
#     На вход подаётся строка "Привет! Меня зовут Артём!"
#     Вывод должен быть "п: 1, р: 2, и: 1, в: 2, е: 2, т: 3, !: 2, м: 2, н: 1, я: 1, з: 1, о: 1, у: 1, а: 1, ё: 1"
# Примечание:
#     Можно использовать только строки и целые. Другие типы данных запрещены.

string_input = input('введите строку для анализа: ')
i = 0
output_string = str()
while i < len(string_input):
    output_string += string_input[i] + ': ' + str(string_input.count(string_input[i]))
    string_input = string_input.replace(string_input[i], '')
    if len(string_input) > 0:
        output_string += ", "
print(output_string)
