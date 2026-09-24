import pathlib
import pandas 

p = pathlib.Path('.')
print(*p.iterdir(), sep='\n', end='\n\n')

print(*list(p.glob('**/*.py')), sep='\n', end='\n\n')
pandas._config