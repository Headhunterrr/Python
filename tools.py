a, b = 1, 1
while a < 10:  # последовательность Фибоначи
    a, b = b, a+b
    if a < 10:
        print(a, end=' -> ')
    else:
        print(a, '\n')

# цикл for для колекции
fruits = {'banana': 2, 'apple': 49, 'lime': 37}
for fruit, amount in fruits.items():
    if amount <= 10:
        print('Few', fruit + "s")
    else:
        print('Many', fruit + "s")
print()

# цикл for для списка
list_number = [64, 7, 26, 133, 98, 23, 89]
for i in list_number:
    print(f"{list_number.index(i) + 1}'s number - {i}")
