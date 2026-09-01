# Ошибки и исключения.

# ----------------------------------------------------------------------------

# Синктакситечие ошибки или ошибки синтаксического анализа.

# while True print('Hello world')

# File "c:\Projects\LearningPython\ErrorsAndExceptions.py", line 10
#     while True print('Hello world')
#                ^^^^^
# SyntaxError: invalid syntax

# При ошибке выводит:
#        - имя файла;
#        - номер строки;
#        - часть проблемного кода со стрелками,
#          указывающими на проблемную часть.

# Стрелки указаны не всегда верно.

# ----------------------------------------------------------------------------

# Исключения.

# Ошибка при выполнении синтаксически верного кода.

# 10/0

# Traceback (most recent call last):
#   File "c:\Projects\LearningPython\ErrorsAndExceptions.py",
#                                                       line 31, in <module>
#     10/0
#     ~~^~
# ZeroDivisionError: division by zero

# В последней строчке выводится имя исключения
# и более подробное описание для данной ситуации.

# Имена стандартных исключений являются встроенными идентификаторами и
# не являются ключевыми словами.

# Остальное выше назыается трассировкой стэка со строками исходного кода.
# Она не выводит строки прочитанные из стандартного ввода.

# built-in exceptions - стандартные/встроенные исключения

# ----------------------------------------------------------------------------

# Обработка исключений.

# Оператор try
# За ним следует блок except.

# Сначала выполняется блок try.

# Если блок try выполнен без возникновения исключений,
# то блок except не выполняется.

# Если во время выполнения блока try возникает исключение
# и имя исключения совпадает с хотя бы одним ключевым словом,
# указанным после слова except,
# то выполение оставшейся части блока try пропускается
# и выполняется блок except с которым найдено совпадение.

# Может быть выполнено не более одного блока except.

# Если имя исключения не совпадает ни с одним ключевым словом,
# указанным в except, исключение передаётся в блок кода за пределы try
# и выводит ошибку.

try:
    print(f"\nTry 1/0")
    1/0
except SystemError:
    ...
except ZeroDivisionError, SyntaxWarning:
    print(f"Failed 1/0\n")

# Пример с выполением исключения ZeroDivisionError.

# Класс исключений, указанных в except,
# соответствует исключениям, которые соответствую экземплярам самого класса
# или одного из его производных классов.

# Класс каждого исключения является производным классом другого исключения.

# BaseException - базовый класс всех исключений.

# Класс Exception - его подкласс (производный) класс класса BaseException,
# базовый класс для всех некритических исключений.

# Классы, не являющимися подклассами Exception, не обрабатываются,
# т.к. используются для указания на необходимость завершения программы.

# Такие как SystemExit (вызвается функцией sys.exit()) и KeyboardInterrupt,
# необходимые, если пользователь хочет прервать программу.

# Многие стандартные модули определяют собственные классы исключений.


class A(BaseException):
    ...


class B(A):
    ...


class C(B):
    ...


for cls in [A, B, C]:
    try:
        raise cls()
    except C:
        print("C")
    except B:
        print("B")
    except A:
        print("A")

print()

# Пример определения пользовательских классов исключений,
# производных друг от друга, и от BaseException.

# Классы A, B и C являются исключениями, т.к. наследуются от BaseException.

# Если except A поствить первым среди except, в выводе будет:

# A
# A
# A

# Класс А является родительским классом для классов B и C,
# поэтому except A сработает для каждого из данных исключений первым.


class FF(BaseException):

    def __str__(self):
        print('Override __str__() in ff exeption')
        return super().__str__()


try:
    raise FF('123', '321')
except FF as gg:
    print(gg, '\n')

# Пример исключения, переопределяющего метод __str__().
# Оператор as после имени исключения позволяет ссылаться в блоке except
# на экземпляр исключения.

# ----------------------------------------------------------------------------

# Ключевое слово raise.

# Завершает ход выполнения программы и вызывает указанное исключение.

# ----------------------------------------------------------------------------

# При возникновении исключений могут возникать связанные с ними значения,
# т.н. аргументы исключений.

# Наличие и типы аргументов зависят от самого аргумента.

# При вызове исключений
# после имени исключения в круглых скобках можно указать переменные.

# Указанные переменые привязаны к экземпляру исключения.
# Экеземпляр имеет атрибут args, хранящий аргументы.

# Встроенные типы исключений переопределяют функцию __str__(),
# которая выводит все аргументы без явного обращения к args.


def raiseBaseException():
    raise BaseException('abc', 123)


try:
    raiseBaseException()
except BaseException as BE:
    print(type(BE))
    print(BE.args)
    print(BE)
    a, b = BE.args
    print(f"a = {a}\nb = {b}\n")
    # повторный вызов raise в блоке exept вызовет исключение,
    # котороые было определено в предыдущем вызове raise
else:
    ...

# try может обрабатывать исключения, вызванные функциями.

# После блока except можно добавить необязательный блок else.
# Данный блок выполняется, если блок try не вызвал исключение.

# Имена Exception/BaseException можно использовать для перехвата
# почти всех исключений.

# Но рекомендуется как можно точнее указывать исключение,
# чтобы избежать неожиданных исключений.

# ----------------------------------------------------------------------------

# Цепочка исключений.

# При вызове необрабатываемого исключения в блоке except,
# будет выведена ошибка с сылкой на обрабатываемое исключение.

# Чтобы указать, что исключение является следствием другого,
# можно использовать from, указав имя обрабатываемого исключения.

# Чтобы не показывать всю цепочку можно указать None.

try:
    raiseBaseException()
except BaseException as BE:
    # raise Exception from BE
    # raise Exception from None
    ...

# ----------------------------------------------------------------------------

# Блок finally.

# Послдений блок цепочки try/except/else/finally выполняется в любом случае.

# Если возникшее исключение не определено except
# или возникло в блоках except или else,
# оно будет сгенерировано после блока funally.

# Если в блоке finally вызваны операторы break, continue, return
# исключения после него не генерируются (не рекомендуется так делать).

# Если в блоке try вызваны операторы break, continue, return
# блок finally будет выполнен перед ними.

# Если в блоке finally вызван оператор return,
# то он выполнится вместо return блока try.

# Не рекомендуется использовать return в блоке finally.

# В реальных программа блок finally полезен для освобождения внешних ресурсов.


def bool_fun():
    try:
        return True
    finally:
        # return False
        ...

print(bool_fun(), '\n')

# ----------------------------------------------------------------------------

# Множество несвязанных исключений.

# Функция ExceptionGroup() "оборачивает" список экземпляров исключений,
# позволяя использовать их одновременно.

# Сама функция является исключением и наследуется от Exception.

# ExceptionGroup(msg, excs), где:
#       - msg - сообщение, комментарий к группе (строка);
#       - excs - последовательность исключений
#         (может быть любая, желательно кортеж).

# BaseExceptionGroup(msg, excs) аналогично ExceptionGroup,
# только наследуется от BaseException.


def BExceptionGroup():
    exceptions = (SystemExit("Error 1"), StopIteration("Error 14"))
    raise BaseExceptionGroup("Houston, we have a problem!", exceptions)

# BExceptionGroup()

#   + Exception Group Traceback (most recent call last):
#   |   File "c:\Projects\LearningPython\ErrorsAndExceptions.py", line 272, in <module>
#   |     BExceptionGroup()
#   |     ~~~~~~~~~~~~~~~^^
#   |   File "c:\Projects\LearningPython\ErrorsAndExceptions.py", line 270, in BExceptionGroup
#   |     raise BaseExceptionGroup("Houston, we have a problem!", exceptions)
#   | BaseExceptionGroup: Houston, we have a problem! (2 sub-exceptions)
#   +-+---------------- 1 ----------------
#     | SystemExit: Error 1
#     +---------------- 2 ----------------
#     | StopIteration: Error 14
#     +------------------------------------


try:
    BExceptionGroup()
except BaseException as be:
    print(f"Class \"{be}\" is {type(be)}\n")


# except* позволяет выборочно обрабатывать определенные исключения
# среди исключений, указанных в группе.

# except* извлекает исключения из группы.

def BExceptionGroup1():
    raise BaseExceptionGroup("Group 1",
                             (SyntaxError(1),
                              SystemError(12),
                              SystemExit(13),
                              StopAsyncIteration(14),
                              BaseExceptionGroup("Group 2",
                                                 (SystemExit(2),
                                                  StopIteration(21),
                                                  StopAsyncIteration(22)))))


# try:
#     BExceptionGroup1()
# except* SystemExit as e:
#     print(f"SystemExit is going\n")
# except* StopAsyncIteration as e:
#     print(f"StopAsyncIteration is going\n")

# SystemExit is going

# StopAsyncIteration is going

#   + Exception Group Traceback (most recent call last):
#   |   File "c:\Projects\LearningPython\ErrorsAndExceptions.py", line 310, in <module>
#   |     BExceptionGroup1()
#   |     ~~~~~~~~~~~~~~~~^^
#   |   File "c:\Projects\LearningPython\ErrorsAndExceptions.py", line 298, in BExceptionGroup1
#   |     raise BaseExceptionGroup("Group 1",
#   |     ...<7 lines>...
#   |                                                  StopAsyncIteration(22)))))
#   | ExceptionGroup: Group 1 (3 sub-exceptions)
#   +-+---------------- 1 ----------------
#     | SyntaxError: 1
#     +---------------- 2 ----------------
#     | SystemError: 12
#     +---------------- 3 ----------------
#     | ExceptionGroup: Group 2 (1 sub-exception)
#     +-+---------------- 1 ----------------
#       | StopIteration: 21
#       +------------------------------------

# ----------------------------------------------------------------------------

# Примечания для исключений.

# С помощью функции .add_note(string) можно добавлять примечания к исключению:
# exception.add_note(string).

try:
    raiseBaseException()
except BaseException as be:
    be.add_note("Line 1 about exception\nLine 2 about exception")
    # raise

# Traceback (most recent call last):
#   File "c:\Projects\LearningPython\ErrorsAndExceptions.py", line 350, in <module>
#     raiseBaseException()
#     ~~~~~~~^^
#   File "c:\Projects\LearningPython\ErrorsAndExceptions.py", line 165, in raiseBaseException
#     raise BaseException('abc', 123)
# BaseException: ('abc', 123)
# Line 1 about exception
# Line 2 about exception

# ----------------------------------------------------------------------------
