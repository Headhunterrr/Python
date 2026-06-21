import unittest
import doctest
import zlib
import datetime as dt
from urllib.request import urlopen
import statistics
import random
import math
import argparse
import os
import re
import sys
import glob

# ----------------------------------------------------------------------------

# краткий тур по стандартной библиотеки Python

# ----------------------------------------------------------------------------

# модуль os
# предоставляет функции для взаимодействия с операционной системой

# print(f"{dir(os)}")
# print(f"{help(os)}")

# модуль shutil
# предоставляет высокоуровневый интерфейс
# для управления файлами и каталогами

# ----------------------------------------------------------------------------

# модуль glob
# предовляет функцию, которая возвращает список файлов текущей директории,
# найденных по шаблону

print(f"\n\n{glob.glob("*.py")}\n")

# ----------------------------------------------------------------------------

# при вызове файла из командной строки и вводе аргументов при вызове
# данные аргументы сохраняются в списке sys.argv

# первым элементом списка является имя вызываемого файла или путь к нему
# в зависимости от того, от куда он вызывается

print(f"{sys.argv}\n")

# ----------------------------------------------------------------------------

# модуль argparse
# предоствляется функции для более сложной обработки командной строки

# parser = argparse.ArgumentParser(
#     prog='top',
#     description='Show top lines from each file')
# parser.add_argument('filenames', nargs='+')
# parser.add_argument('-l', '--lines', type=int, default=10)
# args = parser.parse_args()

# пример
# с передачей одного или нескольких имён файлов
# и оптимальным колличеством строк

# ----------------------------------------------------------------------------

# модуль sys
# содержит атрибуты stdin, stdout, stderr

sys.stderr.write('Warning, log file not found starting a new one')

# такой вариант выводит сообщение об ошибках
# даже когда вывод stdout был перенаправлен

# ----------------------------------------------------------------------------

# модуль re
# предостваляет инструменты регулярных выражений
# для продвинутой обработки строк

print(re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest'))

print(re.sub(r'(\b[a-z]+) \1', r'\1', 'cat in the the hat'), "\n")

# ----------------------------------------------------------------------------

# модуль math
# предоставляет функции, работающие с числами с плавующей запятой

print(math.cos(math.pi / 4))
print(math.log(1024, 2), "\n")

# ----------------------------------------------------------------------------

# модуль random
# предоставляет функции случайного выбора

print(random.choice(['apple', 'pear', 'banana']))

print(random.sample(range(100), 10))

print(random.random())     # float [0.0, 1.0)

print(random.randrange(6), "\n")  # random range(6)

# ----------------------------------------------------------------------------

# модуль statistics
# предоставляет функции базовых статических опреаций

data = [2.75, 1.75, 1.25, 0.25, 0.5, 1.25, 3.5]

print(statistics.mean(data))  # среднее арефметическое

data1 = [1, 2, 4, 5, 134]
print(statistics.median(data1))  # центрально значение отсортированного списка

print(statistics.variance(data), "\n")  # дисперсия

# ----------------------------------------------------------------------------

# модуль urllib.request
# позволяет извлекать данные из URL

with urlopen('https://docs.python.org/3/') as response:
    for line in response:
        line = line.decode()             # Convert bytes to a str
        if 'updated' in line:
            # Remove trailing newline
            print(line.rstrip().lstrip(), "\n")

# ----------------------------------------------------------------------------

# модуль smtplib
# позволяет отправлять электронные письма

# ----------------------------------------------------------------------------

# модуль datetime
# позволяет выполнять операции с датами и временем

print(dt.date.today())
print(dt.date.today() - dt.date(2000, 10, 16), "\n")

# ----------------------------------------------------------------------------

# модули zlib, gzip, bz2, lzma, zipfile, tarfile
# поддерживают арихивацию и сжатие общих данных

string1 = b'Hello, world! Hello, Erth! Hello, world! Hello, Erth!'
print(len(string1))

zipString1 = zlib.compress(string1)
print(zipString1)
print(len(zipString1))

print(zlib.decompress(zipString1), "\n")

# ----------------------------------------------------------------------------

# модуль doctest
# предоставляет функции, которые проводят для функций тесты,
# указанные в их документации


def printHello():
    """Print string "Hello!"

    >>> printHello()
    Hello!
    """
    print("Hello!")


print(doctest.testmod(), '\n')

# ----------------------------------------------------------------------------

# модуль unittest
# аналогично doctest тестирует функции, позволяя более детально настроить тест


class Tests(unittest.TestCase):

    def test_Hello(self):
        self.assertEqual(printHello(), None)


unittest.main()

# ----------------------------------------------------------------------------
