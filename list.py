ls = [1, 23, 23, 'asd']
ls1 = ['hhh', 5.6]
print(ls)
print(ls1, "\n")

ls.append(7.5)  # добовляет объект в конец списка
print(ls)
print(ls1, "\n")

ls1.extend(ls)  # добовляет объекты списка
print(ls)      # в конец другого списка
print(ls1, "\n")

ls1.remove(23)  # удаляет первый объект 23 из списка
print(ls1)
ls1.remove(23)
print(ls1, "\n")

ls.pop(2)      # удаляет объект с индексом 2
print(ls)      # и возвращает его значение
print(ls, ls.pop(), "\n")

print(ls1.index(5.6, 1, 5), "\n")
# возвращает индекс объекта 5.6,
# ищего его в пределах от 1 до 5 не включительно

ls.append(1)
print(ls)
print(ls.count(1), "\n")
# возвращает количество объектов 1

ls2 = [3, 4, 1, 2.0, 2.3, 9]
print(ls2, "\n")

ls2.sort()     # переставляет объекты в списке
print(ls2, "\n")  # по возрвствнию

ls2.reverse()  # реверсирует список
print(ls2, "\n")

ls1.clear()  # удаляет все объекты в списке
print(ls1, "\n")
