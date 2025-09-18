import gc


gc.disable()

x = [2]
print(id(x))
print(x, '\n')

y = x[:]
print(id(y))
print(y, '\n')

x = y[:]
print(id(x))
print(x, '\n')

y = [3]
print(id(y))
print(y, '\n')
