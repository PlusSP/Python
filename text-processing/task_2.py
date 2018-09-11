# !/usr/bin/env python3
# coding: utf-8

# 2. Подсчитывать количество предложений в тексте.


def count_sentences(text):
    number_of_sentences = text.count('...')
    number_of_sentences += text.count('?!.')
    number_of_sentences += text.count('?..')
    number_of_sentences += text.count('!..')
    number_of_sentences += text.count('?!') - text.count('?!.')
    number_of_sentences += text.count('?') - text.count('?!') - text.count('?..')
    number_of_sentences += text.count('!') - text.count('?!') - text.count('!..')
    number_of_sentences += text.count('.') - 3*text.count('...') - 2*text.count('?..') - 2*text.count('!..') - text.count('?!.')
    return number_of_sentences
