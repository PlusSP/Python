# !/usr/bin/env python3
# coding: utf-8

# Написать декоратор, который подсчитывает время работы функции. через метод Time
# Написать декоратор, который подсчитывает количество вызовов функции.
import time


def decorator_time_count(func):
    def wrapper():
        start_time = time.time()
        func()
        end_time = time.time()
        exe_time = end_time - start_time
        print("exe_time = " + str(exe_time))
    return wrapper()


@decorator_time_count
def some_func():
    print('i am func')
    list1 = []
    for i in range(5):
        list1.append(i * 100)


some_func
