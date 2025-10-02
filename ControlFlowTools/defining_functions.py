def fib(n):         # объявили новую функцию с именем fib
    a, b = 1, 1     # получает данные на вход в переменную n
    while a < n:    # выводит числа Фибоначи до n
        print(a, end=' ')
        a, b = b, a + b
    print('\n')


fib(2000)  # принимает на вход 2000 и передает на внутреннюю переменную n
print(fib)
fib        # не принимает на вход ничего, так как ее не вызвали

f = fib    # другие имена могут указывать на эту функию
f(100)     # и вызывать функию через себя
print(f)

print(fib(10), "\n")
# сама функция всегда что-то возвращает
# если отсутствует returne содержанием
# то возвращается None


# def ask_ok(prompt, retries=4, reminder='Please try again!'):
#     print()
#     while True:
#         reply = input(prompt + "\n")
#         if reply in {'y', 'ye', 'yes', 'Y', 'Ye', 'Yes'}:
#             print(f"Nice!", '\n')
#             return True
#         if reply in {'n', 'no', 'nop', 'nope', 'N', 'No', 'Nop', 'Nope'}:
#             print(f"It's so bad, man!", '\n')
#             return False
#         retries = retries - 1
#         if retries < 0:
#             raise ValueError('invalid user response')
#         print(reminder)


# ask_ok('Do you want bear?')
# ask_ok('Do you want bear?', 2)

# in проверяет, совпадает ли аргумент на входе
# с хотя бы одним элементом последовательности

# существует несколько вариантов
# указания необязательных аргументов
# при вызове функций
# - не указываются необязательные аргументы
# - указывается 1+ необязательных аргументов

# значениие аргумента по умолчанию,
# присвается ТОЛЬКО в момент определения функции

i = 5


def f(arg=i):
    print(arg, "\n")


i = 6
f()  # выведет 5

# значение аргумента по умолчанию
# присвается  в момент определения функции


def f1(a, L=[]):
    print(f"Befor append() {type(L)}")
    L.append(a)
    print(f"After append() {type(L)}")
    return L


print(f1(1))  # [1]
print(f1(2))  # [1, 2]
print(f1(3), '\n')  # [1, 2, 3]

# если объект аргумента изменяемый
# то он будет сохранять предыдущие изменения


def f2(a, L=None):
    print(f"Befor append() {type(L)}")
    if L is None:
        L = []
    L.append(a)
    print(f"After append() {type(L)}")
    return L


print(f2(1))  # [1]
print(f2(2))  # [2]
print(f2(3), "\n")  # [3]

# если объект аргумента неизменяемый
# то при новом вызове функции
# он останет таким, каким был
# в момент определения функции

# так как при каждом вызове функции
# он не изменялся

# ключевые слова соответствую имени переменной
# указанной при определеннии функции

# используют их при вызове функции
# для передачи орпеделенного значения/аргумента
# определенной переменной функции

# ключевое_слово = аргумент | kwarg = value
# Keyword argument or kwarg


def hello(age, name, profession='unemployed', place='Copenhagen'):
    print(f"Hello! My name is {name}")
    print(f"I from {place}")
    print(f"I'm {age}, i'm {profession}", '\n')


hello(16, 'Mark')  # аргумент
# без ключевого слова - позиционный
