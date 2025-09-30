print('First line \nSecond line\n')

print(r"C:\users\name"'\n')
print("Hello, "
      "there! \n")
# r игнорирует \ в следующих ковычках
# несколько ковычек можно ставить рядом
# и на разных строках

print('''\
1 line
2 line \
3 line
''')
# \ в конце строки убирает перенос строки

hello = "Hello, there!"
print(hello[0])  # показывает символ строки
print(hello[2])  # с определенным индексом
print(hello[-1])  # можно использовать индекс
print(hello[-3], '\n')  # начиная с конца строки
# индекс -1 указывает на последний символ строки

print(hello[:2])  # индекс 2 включительно
print(hello[2:])  # индекс 2 не включительно
print(hello[:2] + hello[2:])  # так же можно выводить
print(hello[:-2])  # диапозон индексов
print(hello[-2:], '\n')

# символ     P   y   t   h   o   n
# индекс     0   1   2   3   4   5
# индекс    -6  -5  -4  -3  -2  -1

# hello[0] = 'A'
# Строки - неизменяемые, поэтому
# данная операция выдаст ошибку
# TypeError:
# 'str' object does not support item assignment
