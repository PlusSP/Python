# !/usr/bin/env python3
# coding: utf-8

import task_1
import task_2
import task_3
import task_4
import task_5
import task_6
import task_7
import task_8

# Задача
# Написать программу с консольным интерфейсом. Программа должна выполнять следующие функции:

# 1. Читать текстовый файл с диска или загружать по url.
# 2. Подсчитывать количество предложений в тексте.
# 3. Определять набор слов и количество и частоту встречаемости каждого слова в тексте.
# 4. Определять набор букв в тексте и количество и частоту встречаемости каждой буквы в тексте.
# 5. Определять набор знаков препинаия и количество и частоту встречаемости каждого в тексте.
# 6. По каждому из пунктов 3-5 выводить результаты на экран.
# 7. По каждому из пунктов 3-5 выводить горизонтальную гистограмму.
# 8. Иметь возможность сохранить полученные результаты (включая гистограммы) в файл.
# *9.Хранить результаты анализа каждого текста в БД(для этого также требуется реализовать функцию конфигурирования программы)


user_input = input('''This program can read and analyse text.
If you want to read it from a file: enter "1"
If you want to read it from URL: enter "2"
>>>''')
while True:
    if user_input == '1':
        link = input("enter path to file like: ../example.txt: ")
        if link == "":
            text = task_1.read_text_from_file()
            break
        else:
            try:
                text = task_1.read_text_from_file(link)
                break
            except FileNotFoundError:
                print("File Not Found")
                continue
    elif user_input == '2':
        link = input('enter url like: "http://www.example.com" : ')
        if link == "":
            text = task_1.read_text_from_url()
            break
        else:
            try:
                text = task_1.read_text_from_url(link)
                break
            except IOError:
                print("Wrong URL")
                continue
    else:
        user_input = input("Wrong input, try again:\n>>>")
while True:
    user_input = input('''enter "1" to count number of sentences.
enter "2" to determine the set of words, their quantity and the frequency of occurrence of each word in the text.
enter "3" to determine the set of letters in the text, their quantity and frequency of occurrence of each letter in the text.
enter "4" to determine the number of punctuation marks their number and the frequency of occurrence of each in the text.
enter "quit" to quit.
>>>: ''')
    if user_input == '1':
        print("There are {} sentences in the text".format(task_2.count_sentences(text)))
        break
    elif user_input == '2':
        words_dict, words_freq = task_3.sentence_processing(text)
        user_input = input("Print results? y/n: ").lower()
        if user_input == "y":
            task_6.print_words(words_dict, words_freq)
            user_input = input("Show gistograms? y/n: ").lower()
            if user_input == 'y':
                task_7.gistogram(words_dict)
            elif user_input == 'n':
                pass
        elif user_input == "n":
            user_input = input("Show gistograms? y/n: ").lower()
            if user_input == 'y':
                task_7.gistogram(words_dict)
            elif user_input == 'n':
                pass
        user_input = input("Save results in file? y/n: ").lower()
        if user_input == 'y':
            task_8.save_results(words_dict, words_freq)
        elif user_input == 'n':
            continue
    elif user_input == '3':
        char_dict, char_freq = task_4.char_processing(text)
        user_input = input("Print results? y/n: ").lower()
        if user_input == "y":
            task_6.print_chars(char_dict, char_freq)
            user_input = input("Show gistograms? y/n: ").lower()
            if user_input == 'y':
                task_7.gistogram(char_dict)
            elif user_input == 'n':
                pass
        elif user_input == "n":
            user_input = input("Show gistograms? y/n: ").lower()
            if user_input == 'y':
                task_7.gistogram(char_dict)
            elif user_input == 'n':
                pass
        user_input = input("Save results in file? y/n: ").lower()
        if user_input == 'y':
            task_8.save_results(char_dict, char_freq)
        elif user_input == 'n':
            continue
    elif user_input == '4':
        marks_dict, marks_freq = task_5.punctuation_marks_stat(text)
        user_input = input("Print results? y/n: ").lower()
        if user_input == "y":
            task_6.print_marks(marks_dict, marks_freq)
            user_input = input("Show gistograms? y/n: ").lower()
            if user_input == 'y':
                task_7.gistogram(marks_dict)
            elif user_input == 'n':
                pass
        elif user_input == "n":
            user_input = input("Show gistograms? y/n: ").lower()
            if user_input == 'y':
                task_7.gistogram(marks_dict)
            elif user_input == 'n':
                pass
        user_input = input("Save results in file? y/n: ").lower()
        if user_input == 'y':
            task_8.save_results(marks_dict, marks_freq)
        elif user_input == 'n':
            continue
    elif user_input.lower() == "quit":
        break
    else:
        user_input = input("Wrong input, try again:\n>>>")
        continue
