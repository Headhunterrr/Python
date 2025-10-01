from enum import Enum


a, b = 1, 1
while a < 10:  # последовательность Фибоначи
    a, b = b, a+b
    if a < 10:
        print(f"{a} --> ", end="")
    else:
        print(a, '\n')

# цикл for для словаря
fruits = {'banana': 2, 'apple': 49, 'lime': 37}
for fruit, amount in fruits.items():
    if amount <= 10:
        print(f"Few {fruit}s")
    else:
        print(f"Many {fruit}s")
print()

# цикл for для списка
list_numbers = [64, 7, 26, 133, 98, 23, 89]
for i in list_numbers:
    print(f"{list_numbers.index(i) + 1}'s number - {i}")
print()

# нумерация списка в словарь
# начиная с единицы
list_numbers_index_dict = dict(enumerate(list_numbers, 1))
for i in list_numbers_index_dict:
    print(f"{i} : {list_numbers_index_dict[i]}")
print()

# нумерация списка в список из кортежей
# начиная с пятёрки
list_numbers_index_list = list(enumerate(list_numbers, 5))
for i in list_numbers_index_list:
    print(i)
print()

# оператор continue
for num in range(2, 10):
    if num % 2 == 0:
        print(f"Found an even number {num}")
        continue  # заканчивает итерацию цикла
    print(f"Found an odd number {num}")  # и начинает следующую
print()

# оператор break
for n in range(2, 10):
    for x in range(2, n):  # <-- то есть вот этот
        if n % x == 0:
            print(f"{n} equals {x} * {n//x}")
            break  # заканчивает цикл, в котором находится
    else:  # если в цилке не выполнился оператор break
        print(f"{n} is prime  number")
    # после цилка выполняется строка else
    # если цикл был прерван (не только с помощью break)
    # то else пропуска
print()


def pass_():
    pass   # pass ничего не выполняет, используется как заглушка
    ...    # ... аналогично pass


point = (3, 3)
match point:      # сопоставляет значние со значениями в case
    case (0, 0):  # и выводит инструкцию первого совпавшего значения
        print(f"Point in center")
    case (0, y):  # может сопоставлять несколько переменных
        print(f"Point on Ox")
    case (x, 0):
        print(f"Point on Oy")

    case (x, y):  # переменные подающиеся на вход можно
        print(f"Point --> x = {x}, y = {y}")  # использовать дальше

    case (x, y) if x == y:  # можно добваить условие if оно проверяется после
        print(f"Point --> x = y = {y}")  # сопоставления с case

    case _:       # _ - условие, которое гарантировно выполнится
        print(f"Is not point")  # выолняется, если остальные не выполненны
print()


class Color(Enum):
    RED = 'red'
    GREEN = 'green'
    BLUE = 'blue'


color = Color('red')
match color:                # пример с именованными константами
    case Color.RED:
        print("I see red!")
    case Color.GREEN:
        print("Grass is green")
    case Color.BLUE:
        print("I'm feeling the blues :(")

# примеры и разъяснения есть в документе PEP 636
