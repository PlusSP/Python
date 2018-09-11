# !/usr/bin/env python3
# coding: utf-8

# 8. Иметь возможность сохранить полученные результаты (включая гистограммы) в файл.


def save_results(count_dict, freq_dict):
    file = open("Processing_Results.txt", "a")
    file.write("Beginning of the report.\n")
    for key, val in count_dict.items():
        file.write("'{key}' встречается {val} раз, встречаемость - {freq}\n".format(key=key, val=val, freq=freq_dict[key]))
    file.write(" "*20+"_"*120+ "\n")
    for key, val in count_dict.items():
        file.write(key.rjust(20, ' ') + "|" + "█"*val + "\n")
    file.write("End of the report.\n")
    file.close()
