# ----------------------------------------------------------------------------

# ошибки и исключения

# ----------------------------------------------------------------------------

# синктакситечие ошибки или ошибки синтаксического анализа


# while True print('Hello world')

# File "c:\Projects\LearningPython\ErrorsAndExceptions.py", line 10
#     while True print('Hello world')
#                ^^^^^
# SyntaxError: invalid syntax


# при ошибке выводит
#        имя файла
#        номер строки
#        часть проблемного кода со стрелками, указывающими на проблемную часть

# стрелки указаны не всегда верно

# ----------------------------------------------------------------------------

# исключения

# ошибка при выполнении синтаксически верного кода

# 10/0

# Traceback (most recent call last):
#   File "c:\Projects\LearningPython\ErrorsAndExceptions.py", line 31, in <module>
#     10/0
#     ~~^~
# ZeroDivisionError: division by zero

# в последней строчке выводится имя исключения
# и более подробное описание для данной ситуации

# имена стандартных исключений являются встроенными идентификаторами
# не являются ключевыми словами

# остальное выше назыается трассировкой стэка со строками исходного кода
# она не выводит строки прочитанные из стандартного ввода

# built-in exceptions - стандартные/встроенные исключения

# ----------------------------------------------------------------------------

# обработка исключений

# оператор try, за ним следует блок except

# сначала выполняется блок try

# если блок try выполнен без возникновения исключений
# блок except не выполняется

# если во время выполнения блока try возникает исключение 
# и имя исключения совпадает с хотя бы одним ключевым словом, 
# указанным после слова except

# выполение оставшейся части блока try пропускается
# и выполняется блок except с котором найдено совпадение

# может быть выполнено не более одного блока except

# если имя исключения не совпадает
# ни с одним ключевым словом, указанным в except,
# исключение передаётся в блок кода за пределы try и выводит ошибку

try:
    print(f"\nTry 1/0")
    1/0
except SystemError:
    ...
except ZeroDivisionError, SyntaxWarning:
    print(f"Failed 1/0\n")

# пример с выполением исключения ZeroDivisionError

# класс исключений, указанных в except, соответствует исключениям,
# которые соответствую экземплярам самого класса
# или одного из его производных классов

# класс каждого исключения является производным классом другого исключения
# но не наоборот

# BaseException - базовый класс всех исключений

# его подкласс (производный) класс Exception
# базовый класс для всех некритических исключений

# классы, не являющимися подклассами Exception, не обрабатываются,
# так как используются для указания на необходимость завершения программы

# такие как SystemExit (вызвается функцией sys.exit()) и KeyboardInterrupt,
# необходимые, если пользователь хочет прервать программу

# многие стандаотные модули определяют собственные классы исключений


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

# пример определения пользовательских классов исключений,
# производных друг от друга, и от BaseException

# так как классы A, B и C наследуются от BaseException, 
# они являются исключениями 

# если except A поствить первым среди except,
# в выводе будет

# A
# A
# A

# класс А является родительским классом для классов B и C,
# поэтому except A сработает для каждого из данных исключений 

# ----------------------------------------------------------------------------

# ключевое слово raise

# завершает ход выполнения программы 
# и вызывает указанное исключение в блоке try 

# ----------------------------------------------------------------------------

# при возникновении исключений
# могут возникать связанные с ними значения, 
# так называемые аргументы исключений

# наличие и типы аргументов зависят от самого аргумента

# при вызове исключений 
# после имени исключения в круглых скобках можно указать переменные

# указанные переменые привязаны к экземпляру исключения
# экеземпляр имеет атрибут (параметр) args, хранящий аргументы

# встроенные типы исключений определяют __str__(),
# которая выводит все аргументы без явного обращения к args


def raiseBaseException():
    raise BaseException('abc', 123)


try:
    raiseBaseException()
except BaseException as BE:
    print(type(BE))
    print(BE.args)
    print(BE)
    # __str__ позволяет напрямую выводить аргументы,
    # но может быть переопределен в подкласс исключений
    a, b = BE.args
    print(f"a = {a}\nb = {b}\n")
    # raise
    # повторный вызов raise вызовет исключение,
    # котороые было определено в предыдущем вызове raise
else:
    ...

# try может обрабатывать исключения, вызванные функциями

# после блока except можно добавить необязательный блок else
# он выполняется, если блок try не вызвал исключение

# имена Exception/BaseException можно использовать для перехвата
# почти всех исключений

# но рекомендуется как можно точнее указывать исключение,
# чтобы избежать неожиданных исключений

# ----------------------------------------------------------------------------

# цепочка исключений

# при вызове необрабатываемого исключения в блоке except, будет выведена ошибка
# с сылкой на обрабатываемое исключение (которое вызвало блок except)

# чтобы указать, что исключение является следствием другого
# можно использовать from, указав имя обрабатываемого исключения

# чтобы не показывать всю цепочку можно указать None

try:
    raiseBaseException()
except BaseException as BE:
    # raise Exception from BE
    # raise Exception from None
    ...

# ----------------------------------------------------------------------------

# блок finally

# послдений блок цепочки try/except/else/finally
# выполняется в любом случае

# если возникшее исключение не определено except
# или возникло в блоках except или else,
# оно будет сгенерировано после блока funally

# если в блоке finally вызваны операторы break, continue, return
# исключения после него не генерируются
# (не рекомендуется так делать)

# если в блоке try вызваны операторы break, continue, return,
# блок finally будет выполнен перед ними

# если в блоке finally вызван оператор return
# то он выполнится вместо return блока try

# не рекомендуется использовать return в блоке finally

# в реальных программа блок finally полезен
# для освобождения внешних ресурсов


def bool_fun():
    try:
        return False
    finally:
        ...


print(bool_fun(), '\n')

# ----------------------------------------------------------------------------

# множество несвязанных исключений

# функция ExceptionGroup() "оборачивает" список экземпляров исключений,
# позволяя использовать их одновременно

# сама функция является исключением,
# наследуется от Exception

# ExceptionGroup(msg, excs)

# msg - сообщение, комментарий к группе (строка),
# excs - последовательность исключений (может быть любая, желательно кортеж)

# BaseExceptionGroup(msg, excs) аналогично ExceptionGroup,
# только наследуется от BaseException


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
# среди исключений, указанных в группе

# except* извлекает исключения из группы

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

# примечания для исключений

# с помощью функции .add_note(string) можно добавлять примечания к исключению
# exception.add_note(string)

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
