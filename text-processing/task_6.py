# !/usr/bin/env python3
# coding: utf-8

# 6. По каждому из пунктов 3-5 выводить результаты на экран.


def print_words(words_dict, freq_dict):
    print("Набор слов и их количество в тексте:")
    for key, val in words_dict.items():
        if 10 < val < 20:
            times = "раз"
        else:
            if 1 < int(str(val)[len(str(val))-1]) < 5:
                times = "раза"
            else:
                times = 'раз'
        print("слово '{key}' встречается {val} {times}, встречаемость - {freq}".format(key=key, val=val, times=times,
                                                                                       freq=freq_dict[key]))
    pass


def print_chars(chars_dict, chars_freq):
    print("Набор букв и их количество в тексте:")
    for key, val in chars_dict.items():
        if 10 < val < 20:
            times = "раз"
        else:
            if 1 < int(str(val)[len(str(val))-1]) < 5:
                times = "раза"
            else:
                times = 'раз'
        print("буква '{key}' встречается {val} {times}, встречаемость - {freq}".format(key=key, val=val, times=times,
                                                                                       freq=chars_freq[key]))
    pass


def print_marks(marks_dict, marks_freq):
    print("Набор букв и их количество в тексте:")
    for key, val in marks_dict.items():
        if 10 < val < 20:
            times = "раз"
        else:
            if 1 < int(str(val)[len(str(val))-1]) < 5:
                times = "раза"
            else:
                times = 'раз'
        print("символ '{key}' встречается {val} {times}, встречаемость - {freq}".format(key=key, val=val, times=times,
                                                                                        freq=marks_freq[key]))
    pass
