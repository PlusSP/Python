# !/usr/bin/env python3
# coding: utf-8

# 1. Читать текстовый файл с диска или загружать по url.

import requests


def read_text_from_file(link_text="Plain Text.txt"):
    text = open(link_text)
    text1 = text.read()
    text.close()
    return text1


def read_text_from_url(url_link="https://acc.dl.osdn.jp/sfnet/a/ap/apkinstaller/Apk Installer/README.txt"):
    text = requests.get(url_link).text
    return text
