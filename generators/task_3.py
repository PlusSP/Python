# !/usr/bin/env python3
# coding: utf-8

# 3. Написать программу, которая принимает путь к текстовому файлу и букву
#  и выводит список слов, которые начинаются с указанной буквы.


def read_text(link_text):
    text = open(link_text)
    text_line = text.readlines()
    for i in range(len(text_line)):
        line_list = text_line[i].split(" ")
        for j in range(len(line_list)):
            yield line_list[j]


def gen_find_words(gen, char):
    words_list = []
    while True:
        try:
            i = next(gen)
            if i.startswith(char.lower()) or i.startswith(char.upper()):
                words_list.append(i)
            else:
                continue
        except StopIteration:
            break
    return words_list


R = read_text("Text_Example.txt")
print(gen_find_words(R, 'ф'))
