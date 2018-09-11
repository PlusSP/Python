# !/usr/bin/env python3
# coding: utf-8

# #1 Написать программу, которая принимает от пользователя текстовую строку и выводит на экран её длину.

# user_input = input('введите строку: ')
# print('длина введённой строки: ', len(user_input))

# # 2. Написать программу, которая принимает от пользователя текстовую строку и выводит её длину без учёта пробелов.
#
# user_input = input('введите строку с пробелами: ')
# print('длина строки без учёта пробелов:', str(len(user_input)-user_input.count(' ')))
#
# # 3. Написать программу, которая принимает от пользователя текстовую строку и символ и выводит на экран количество вхождений символа в строку.
#
# user_input = input('введите строку: ')
# char_input = input('введите символ: ')
# print('символ', char_input, 'входит', user_input.count(char_input), 'раз в строку', user_input)
#
#  # 5 Написать программу, которая принимает строку и выводит её в обратном порядке.
#
# user_input = input('введите строку: ')
# print("строка в обратном порядке", user_input[-1:-600:-1])

# 6 Написать программу, которая принимает строку и число, делит её на равные части и меняет их местами.

# string_input = input('введите строку: ')
# num_input = int(input('введите количество срезов: '))
# parts_length = int(len(string_input)/num_input)
# print('строка', string_input, 'разделена на', num_input, 'части: ')
# first_index = int(len(string_input)) - parts_length
# second_index = len(string_input)
# i = num_input
# while i > 0:
#     print(string_input[first_index:second_index])
#     first_index -= parts_length
#     second_index -= parts_length
#     i -= 1
# if first_index >= 0:
#     print('остаток:', string_input[0:(len(string_input) % num_input)])


# # 7 Написать программу, которая принимает строку и число, делит её на равные части указанного размера и выводит полученные фрагменты в обратном порядке.
# #   Если крайний фрагмент содержит меньше символов чем указано, то дополнить его до нужного количества пробелами.

# string_input = input('введите строку: ')
# parts_length = int(input('введите длину срезов: '))
# num_parts = int(len(string_input)/parts_length)
# print('строка', string_input, 'разделена на части по', parts_length, 'символа: ')
# i = num_parts
# first_index = -1
# second_index = -parts_length
# while i > 0:
#     print(string_input[first_index:second_index-1:-1])
#     first_index -= parts_length
#     second_index -= parts_length
#     i -= 1
# if first_index >= -(len(string_input)):
#     print(string_input[first_index:-600:-1].ljust(parts_length, "_"))

# # 8 Написать программу, которая принимает строку и выводит её в таком виде, что чётные буквы в верхнем регистре, а нечётные в нижнем.

# string_input = input('введите строку: ')
# while string_input.isalpha() is False:
#     string_input = input('принимаются только буквенные символы: ')
# i = len(string_input)
# new_string = str()
# j = 0
# while i > 0:
#     if j % 2 == 0:
#         new_string += string_input[j].upper()
#     else:
#         new_string += string_input[j].lower()
#     i -= 1
#     j += 1
# print(new_string)


# # 9 Написать программу, которая определяет введено ли число или слово. Если невозможно определить, то повторить ввод.

# string_input = input('введите что-нибудь: ')
# while string_input.isalpha() is False and string_input.isdigit() is False:
#     string_input = input('принимаются либо цифры, либо буквы: ')
# if string_input.isalpha():
#     print(string_input, '- вы ввели слово')
# elif string_input.isdigit():
#     print(string_input, '- вы ввели число')


# 10 Написать программу, которая принимает целое число от 1 до 999 и вывести его текстом.

# user_input = int(input('введите число от 1 до 999: '))
# while 1 > user_input > 999 is False:
#     user_input = int(input('введите число от 1 до 999: '))
# string_output = str()
# num_dict = {1: 'один', 2: 'два', 3: 'три', 4: 'четыре', 5: 'пять', 6: 'шесть', 7: 'семь', 8: 'восемь', 9: 'девять',
#             10: 'десять', 11: 'одиннадцать', 12: 'двенадцать', 13: 'тринадцать', 14: 'четырнадцать', 15: 'пятнадцать',
#             16: 'шестнадцать', 17: 'семнадцать', 18: 'восемнадцать', 19: 'девятнадцать', 20: 'двадцать', 30: 'тридцать',
#             40: 'сорок', 50: 'пятьдесят', 60: 'шестьдесят', 70: 'семьдесят', 80: 'восемдесят', 90: 'девяносто', 100: 'сто',
#             200: 'двести', 300: 'триста', 400: 'четыреста', 500: 'пятьсот', 600: 'шестьсот', 700: 'семьсот', 800: 'восемьсот', 900: 'девятьсот'}
# if 1 <= user_input <= 19:
#     print('вы ввели: ', num_dict[user_input])
# elif 20 <= user_input <= 99:
#     if user_input % 10 == 0:
#         print('вы ввели: ', num_dict[user_input])
#     else:
#         string_output += num_dict[user_input - (user_input % 10)] + " " + num_dict[user_input % 10]
#         print('вы ввели: ', string_output)
# elif 100 <= user_input <= 999:
#     if user_input % 100 == 0:
#         print('вы ввели: ', num_dict[user_input])
#     elif user_input % 10 == 0:
#         print('вы ввели: ', num_dict[(user_input // 100) * 100], num_dict[(user_input % 100)])
#     else:
#         string_output += num_dict[(user_input // 100) * 100] + " "
#         if user_input % 100 < 20:
#             string_output += num_dict[user_input % 100]
#         else:
#             string_output += num_dict[((user_input % 100)//10) * 10] + " " + num_dict[user_input % 10]
#         print('вы ввели: ', string_output)

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
