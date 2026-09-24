import random
import numpy

mat1 = numpy.array([[random.randint(0, 9) for _ in range(5)]
                   for _ in range(5)])
mat2 = numpy.array([[random.randint(0, 9) for _ in range(5)]
                   for _ in range(5)])

print(*mat1, sep='\n', end='\n\n')
print(*mat2, sep='\n', end='\n\n')

mat_mulp = mat1 @ mat2
print(*mat_mulp, sep='\n', end='\n\n')
