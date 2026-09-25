import pathlib

p = pathlib.Path('.')
print(*p.iterdir(), sep='\n', end='\n\n')

print(*list(p.glob('**/*.py')), sep='\n', end='\n\n')