a, b = 1, 1
while a < 10:  # последовательность Фибоначи
    a, b = b, a+b
    if a < 10:
        print(f"{a} --> ", end="")
    else:
        print(a, '\n')

# цикл for для колекции
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

# нумерация списка в список из списков
# начиная с пятёрки
list_numbers_index_list = list(enumerate(list_numbers, 5))
for i in list_numbers_index_list:
    print(i)
