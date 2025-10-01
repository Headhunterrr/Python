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

print(fib(10))
# функция всегда что-то возвращает
# если не отсутствует returne
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

# существует 3 варианта указания аргументов
# при вызове функций
# 1. указываются только обязательные аргументы
# 2. указывается один из обязательных аргументов
# 3. указываются все аргументы

# in проверяет, содержит ли
