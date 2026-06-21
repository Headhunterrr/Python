import decimal
from heapq import heapify, heappop, heappush
import bisect
from array import array
import gc
import weakref
import logging
import struct
import os.path
import time
from string import Template
import locale
import textwrap
import pprint
import reprlib

# ----------------------------------------------------------------------------

# модуль reprlib
# кастомизированная версия repr()
# для сокращенного отображения больших вложений

print()
print(reprlib.repr('fsdfsdfasdffdasdfasdfasfasdfsadfasfasfsdfasdfasfasdfasdf'))
print(reprlib.repr(3485720394857234587432095873598749587209572394857309485744))
print(reprlib.repr({'a', 'b', 'c', 'd', 'e',
      'f', 'g', 'h', 'y', 'u', 'i', 'i'}), "\n  ")

# ----------------------------------------------------------------------------

# модуль pprint
# позволяет более читабельно и красиво выводить данные

pprint.pprint(
    {"a": 1, "b": {"ba": 12, "bb": {"bba": 221, "bbb": 222}}, "c": 3}, width=10)

# ----------------------------------------------------------------------------

# модуль textwarp
# форматирует абзацы на определенную ширину

doc = """The wrap() method is just like fill() except that it returns
a list of strings instead of one big string with newlines to separate
the wrapped lines."""

print('\n'.lstrip())
print(textwrap.fill(doc, width=55), '\n',)

# ----------------------------------------------------------------------------

# модуль locale
# предоставляет доступ, к базе данных специфичных форматов данных

print(locale.setlocale(locale.LC_ALL, 'English_United States.1252'))

conv = locale.localeconv()          # get a mapping of conventions
print(conv, '\n')
x = 1234567.8

print(locale.format_string("%d", x, grouping=True))

print(locale.format_string("%s%.*f",
                           (conv['currency_symbol'], conv['frac_digits'], x),
                           grouping=True),
      '\n')

# ----------------------------------------------------------------------------

# класс Templete модуля string
# предоставляет простой синтаксиз форматирования текста

# *Templete с англ. шаблон*

text = Template("Hello, ${name}!")
print(text.substitute(name="Jhon"))

# safe_substitute не выводит ошибку при отсутствии ключевого аргумента,
# оставляя строковое включение в исходном виде

print(text.safe_substitute(), '\n')

# ----------------------------------------------------------------------------

# в подклассе Template можно настроить свой разделитель


class CustomDelimiter(Template):
    delimiter = '('


photofiles = ['img_1074.jpg', 'img_1076.jpg', 'img_1077.jpg']
t, date = CustomDelimiter("he_he_({d}_(n(f"), time.strftime('%y.%m.%d')

for i, filename in enumerate(photofiles):
    base, ext = os.path.splitext(filename)
    newname = t.substitute(d=date, n=i+1, f=ext)
    print('{0}  -->  {1}'.format(filename, newname))
print()

# пример, изменяющий имена файлов

# ----------------------------------------------------------------------------

# модуль struct
# предоставляет функции pack() и unpack()

# которое позволяют читать заголовки файлов без использования zipfile

with open('FileFor.zip', 'rb') as f:
    data = f.read()

start = 0

while True:
    start += 14
    fields = struct.unpack('<IIIHH', data[start:start+16])
    crc32, comp_size, uncomp_size, filenamesize, extra_size = fields
    if filenamesize == 0:
        break

    start += 16
    filename = data[start:start+filenamesize]
    start += filenamesize
    extra = data[start:start+extra_size]
    print(f"{str(filename, encoding="utf-8"):23}",
          hex(crc32), comp_size, uncomp_size)

    start += extra_size + comp_size

print()

# ----------------------------------------------------------------------------

# модуль threading
# позволяет использовать многопоточность

# ----------------------------------------------------------------------------

# модуль logging
# позволяет выводить сообщения и записывать их в файл

logging.error('Text of error')
print()

# ----------------------------------------------------------------------------

# модуль weakref
# позволяет отслеживать объект без создания ссылки

# для того, чтобы заработал "сборщик мусора" и освободилась память,
# необходимо удалить все ссылки на объект


class A:
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return str(self.value)


aa = A(20)
cc = aa

del aa
print(cc, '\n')

# пример, когда при удалении одной ссылки, память не освобождается

a, d = A(10), weakref.WeakValueDictionary()
d['primary'] = a
print(d['primary'])

del a
print(gc.collect())

try:
    print(d['primary'])
except KeyError:
    print()


# пример, когда при удалении ссылки, освобождается память

# ----------------------------------------------------------------------------

# модуль array
# предоставляет класс array, который позволяет хранить только целые числа,
# тем самым занимая меньше памяти

a = array('h', [123, 456])
print(a, '\n')

# ----------------------------------------------------------------------------

# модуль bisect
# предоставляет различные функции сортировки списков

index = [(1, 'apple'), (2, 'kiwi'), (4, 'banana')]
bisect.insort(index, (3, 'mandarin'))
print(index)

# ----------------------------------------------------------------------------

# модуль heapq
# позволяет работать с кучами

data = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]

heapify(data)
print(data)

# переводит список в кучу, помещает наименьшее значение в начало

heappush(data, 2)
print(data)

# добавляет элемент по возрастанию

[print(f"{heappop(data)}", end=' ') for i in range(3)]
print('\n')

# выводит наименьшее значение

# ----------------------------------------------------------------------------

# модуль decimal
# предоставляет возможности и тип данных для вычислений с плавающей запятой
# с высокой точностью

decimal.getcontext().prec = 20
print(decimal.Decimal(1) / decimal.Decimal(7))

# ----------------------------------------------------------------------------
