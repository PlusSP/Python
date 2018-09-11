# !/usr/bin/env python3
# coding: utf-8

# 4. Определять набор букв в тексте и количество и частоту встречаемости каждой буквы в тексте.


def char_processing(text):
    text = text.lower()
    text = text.replace("\n", '')
    char_dict = {}
    char_dict = char_dict.fromkeys(text)
    char_freq = char_dict.copy()
    for key in char_dict.keys():
        char_dict[key] = text.count(key)
        char_freq[key] = str(round(100 / (len(text) - text.count(key)) * text.count(key), 2)) + '%'
    return char_dict, char_freq
