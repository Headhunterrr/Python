ls = [1, 23, 23, 'asd']
ls1 = ['hhh', 5.6]
print(ls)
print(ls1, "\n")

ls.append(7.5)
print(ls)
print(ls1, "\n")

ls1.extend(ls)
print(ls)
print(ls1, "\n")

ls1.remove(23)
print(ls1)
ls1.remove(23)
print(ls1, "\n")

ls.pop(2)
print(ls)
print(ls, ls.pop(), "\n")

print(ls1.index(5.6, 1, 5), "\n")

ls.append(1)
print(ls)
print(ls.count(1), "\n")

ls2 = [3, 4, 1, 2.0, 2.3, 9]
print(ls2, "\n")

ls2.sort()
print(ls2, "\n")

ls2.reverse()
print(ls2, "\n")

ls1.clear()
print(ls1, "\n")
