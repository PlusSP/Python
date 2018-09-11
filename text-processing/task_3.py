# !/usr/bin/env python3
# coding: utf-8

# 3. Определять набор слов и количество и частоту встречаемости каждого слова в тексте.


def sentence_processing(text):
    text = text.lower()
    text = text.replace('.\n', " ")
    text = text.replace(',', '')
    text = text.replace('.', '')
    text = text.replace('!', '')
    text = text.replace('?', '')
    text = text.replace(':', '')
    text = text.replace(';', '')
    text = text.replace('(', '')
    text = text.replace(')', '')
    text = text.replace('"', '')
    text = text.replace("'", '')
    text = text.replace('»', '')
    text = text.replace('«', '')
    text = text.replace('_', '')
    text = text.replace('–', '')
    text = text.replace('/', '')
    text = text.replace('\\', '')
    return words_processing(text)


def words_processing(text):
    words_list = text.split(' ')
    words_dict = {}
    words_dict = words_dict.fromkeys(words_list, 1)
    words_freq = words_dict.copy()
    for i in words_list:
        words_dict[i] = text.count(i)
        words_freq[i] = str(round(100 / (len(words_list)-text.count(i)) * text.count(i), 2)) + '%'
    return words_dict, words_freq
