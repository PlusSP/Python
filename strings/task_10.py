# !/usr/bin/env python3
# coding: utf-8

# 10 Написать программу, которая принимает целое число от 1 до 999 и вывести его текстом.

user_input = int(input('введите число от 1 до 999: '))
while 1 > user_input > 999 is False:
    user_input = int(input('введите число от 1 до 999: '))
string_output = str()
num_dict = {1: 'один', 2: 'два', 3: 'три', 4: 'четыре', 5: 'пять', 6: 'шесть', 7: 'семь', 8: 'восемь', 9: 'девять',
            10: 'десять', 11: 'одиннадцать', 12: 'двенадцать', 13: 'тринадцать', 14: 'четырнадцать', 15: 'пятнадцать',
            16: 'шестнадцать', 17: 'семнадцать', 18: 'восемнадцать', 19: 'девятнадцать', 20: 'двадцать', 30: 'тридцать',
            40: 'сорок', 50: 'пятьдесят', 60: 'шестьдесят', 70: 'семьдесят', 80: 'восемдесят', 90: 'девяносто', 100: 'сто',
            200: 'двести', 300: 'триста', 400: 'четыреста', 500: 'пятьсот', 600: 'шестьсот', 700: 'семьсот', 800: 'восемьсот', 900: 'девятьсот'}
if 1 <= user_input <= 19:
    print('вы ввели: ', num_dict[user_input])
elif 20 <= user_input <= 99:
    if user_input % 10 == 0:
        print('вы ввели: ', num_dict[user_input])
    else:
        string_output += num_dict[user_input - (user_input % 10)] + " " + num_dict[user_input % 10]
        print('вы ввели: ', string_output)
elif 100 <= user_input <= 999:
    if user_input % 100 == 0:
        print('вы ввели: ', num_dict[user_input])
    elif user_input % 10 == 0:
        print('вы ввели: ', num_dict[(user_input // 100) * 100], num_dict[(user_input % 100)])
    else:
        string_output += num_dict[(user_input // 100) * 100] + " "
        if user_input % 100 < 20:
            string_output += num_dict[user_input % 100]
        else:
            string_output += num_dict[((user_input % 100)//10) * 10] + " " + num_dict[user_input % 10]
        print('вы ввели: ', string_output)

