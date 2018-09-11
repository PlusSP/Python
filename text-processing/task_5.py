# !/usr/bin/env python3
# coding: utf-8

# 5. Определять набор знаков препинаия и количество и частоту встречаемости каждого в тексте.


def punctuation_marks_stat(text):
    marks_dict = {}
    marks_dict_output = {}
    num_of_marks = 0
    marks_dict["\n"] = text.count('\n')
    marks_dict[","] = text.count(',')
    marks_dict["."] = text.count('.')
    marks_dict["!"] = text.count('!')
    marks_dict["?"] = text.count('?')
    marks_dict[":"] = text.count(':')
    marks_dict[";"] = text.count(';')
    marks_dict['"'] = text.count('"')
    marks_dict["«"] = text.count('«')
    marks_dict["»"] = text.count('»')
    marks_dict["'"] = text.count("'")
    marks_dict["-"] = text.count('-')
    marks_dict["_"] = text.count('_')
    marks_dict["("] = text.count('(')
    marks_dict[")"] = text.count(')')
    marks_dict["–"] = text.count('–')
    for key, val in marks_dict.items():
        if val != 0:
            marks_dict_output[key] = val
    marks_dict_freq = marks_dict_output.copy()
    for val in marks_dict_output.values():
        num_of_marks += val
    for key, val in marks_dict_output.items():
        marks_dict_freq[key] = str(round((100 / (num_of_marks - val) * val), 2)) + '%'
    return marks_dict_output, marks_dict_freq

# text = 'Юрию Плаксину 72 года. юрию И хорошо бы каждому в этом возрасте показывать хотя бы по\х\ожий уровень бодрости.\nЧеловек, который организовал успешный бизнес на шестом десятке лет, без потери скорости челночит по цехам своего завода, что-то придумывает и не теряет интереса к происходящему.\nГоворит, назвал предприятие в честь старшей дочери.\nДиректором является супруга. Помимо старшей дочери, на «Виктории» работают ее муж и сестра. Вот такой семейный бизнес по-белорусски. Коллеги-родственники отмечают, что это не всегда просто, но как-то справляются.'
# print(punctuation_marks_stat(text))