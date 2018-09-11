# !/usr/bin/env python3
# coding: utf-8


# 7. Написать аналог fromkeys.
def analog_from_keys(seq, value=None):
    d1 = {}
    for i in range(len(seq)):
        d1[i] = value
    return d1
