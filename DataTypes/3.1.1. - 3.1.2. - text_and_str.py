
# \n переносит на следующую строку

print('First line \nSecond line\n')

print("Hello, "
      "there! \n")

# r игнорирует \ в следующих ковычках

print(r"C:\users\name"'\n')

# тройные ковычки испльзуют несколько стпрок
# \ в конце строки убирает перенос строки

print('''\
1 line
2 line \
3 line
''')

hello = "Hello, there!"

# [] показывает символ строки с индексом
# , указанным в скобках

print(hello[0])
print(hello[2])

# можно использовать индекс, начиная с конца строки
# индекс -1 указывает на последний символ строки

# символ     P   y   t   h   o   n
# индекс     0   1   2   3   4   5
# индекс    -6  -5  -4  -3  -2  -1

print(hello[-1])
print(hello[-3], '\n')

# с помщью : можно выводить диапозон символов

print(hello[:2])  # индекс 2 включительно
print(hello[2:])  # индекс 2 не включительно
print(hello[:2] + hello[2:])
print(hello[:-2])
print(hello[-2:], '\n')


# str - неизменный класс

# hello[0] = 'A'
# данная операция выдаст ошибку:

# TypeError:
# 'str' object does not support item assignment
