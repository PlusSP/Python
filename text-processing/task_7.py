# !/usr/bin/env python3
# coding: utf-8

# 7. По каждому из пунктов 3-5 выводить горизонтальную гистограмму.


def gistogram(count_dict):
    print(" "*20+"_"*120)
    for key, val in count_dict.items():
        print(key.rjust(20, ' ') + "|" + "█"*val)
    print(" "*20+"_"*120)
