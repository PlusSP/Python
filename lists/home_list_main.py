# !/usr/bin/env python3
# coding: utf-8

import numbers_sum
import minimal_num
import repeating_elements
import sort_list
import strings_list
import lists_comparison
import matrix
import set_methods
import combinations

# 9. Написать программу выводящую все возможные комбинации пар элементо из двух списков.

if __name__ == '__main__':
    user_input = input('''для суммирования списка чисел введите: 1
        для выведения максимального и минимального числa введите: 2
        для вывода списка неповторяющихся чисел введите: 3
        для сортировки списка введите: 4
        для программы принимающую список строк и число и выводящую список из слов, длина которых меньше указанного числа введите: 5
        для сравнения двух списков введите: 6
        для транспонирования матрицы введите: 7
        для операций с множествами используя только списки введите: 8
        для вывода всех возможных комбинаций пар элементо из двух списков введите: 9
        : ''')
    if user_input == '1':
        print(numbers_sum.numbers_sum(numbers_sum.list_input()))
    elif user_input == '2':
        print(minimal_num.minimal_num(numbers_sum.list_input()))
    elif user_input == '3':
        print(repeating_elements.repeat(numbers_sum.list_input()))
    elif user_input == '4':
        print(sort_list.sort(numbers_sum.list_input()))
    elif user_input == '5':
        print(strings_list.max_length(strings_list.list_of_strings(), int(input("enter max length of strings"))))
    elif user_input == '6':
        print(lists_comparison.comparison(strings_list.list_of_strings(), strings_list.list_of_strings()))
    elif user_input == '7':
        list1 = [[1,2,3],
                 [4,5,6],
                 [7,8,9]]
        list2 = [[1,2,3,4],
                 [5,6,7,8]]
        print(list1)
        print(matrix.transposition(list1))
        print(list2)
        print(matrix.transposition(list2))
    elif user_input == '8':
        list1 = [1, 5, 3,7, 8, 9]
        list2 = [1, 2, 3, 4]
        print(set_methods.symmetric_diff(list1, list2, 1))
    elif user_input == '9':
        list1 = [1,2,3]
        list2 = [1,2,3,4]
        print(combinations.all(list1, list2))
    else:
        print("invalid input")
