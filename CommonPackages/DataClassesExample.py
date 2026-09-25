import dataclasses


@dataclasses.dataclass
class data:
    a: int
    b: int = 1
    c: str = ''
    d: tuple = ()
    e: dict = dataclasses.field(default_factory=dict)
    f: list[int] = dataclasses.field(default_factory=list)


d = data(1)
print(d.__dict__, '\n')
print(*dataclasses.fields(d), sep='\n\n')  # print(d.__dataclass_fields__)


@dataclasses.dataclass
class Point:
    x: int
    y: int


@dataclasses.dataclass
class Points:
    mylist: list[Point]


point = Point(10, 20)
print(f"\n{dataclasses.asdict(point)}")
print(dataclasses.asdict(point, dict_factory=tuple))
print(dataclasses.astuple(point))
assert dataclasses.asdict(point) == {'x': 10, 'y': 20}

points = Points([Point(0, 0), Point(10, 4)])
print(f"\n{dataclasses.asdict(points)}")
print(dataclasses.asdict(points))
print(dataclasses.astuple(points))
assert dataclasses.asdict(points) == {'mylist': [
    {'x': 0, 'y': 0}, {'x': 10, 'y': 4}]}


@dataclasses.dataclass
class post_processing():
    a: int = 1
    b: int = 1
    c: int = dataclasses.field(init=False)

    def __post_init__(self):
        self.c = self.a + self.b


a = post_processing()
print(a.c)


@dataclasses.dataclass
class Base:
    x: float = 15.0
    y: int = 0


@dataclasses.dataclass
class Child(Base):
    z: int = 10
    x: int = 15

    # def __init__(self,
    #              x: int = 15,
    #              y: int = 0,
    #              z: int = 10):


@dataclasses.dataclass
class with_list:
    x: list = dataclasses.field(default_factory=list)

    def add(self):
        self.x.append(1)


x1, x2 = with_list(), with_list()
x1.add()
print(x1.x, x2.x)
assert x1.x is not x2.x
assert with_list().x is not with_list().x
