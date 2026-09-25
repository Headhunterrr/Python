def send_delegator(delegator):
    def inner(*pa, **kwa):
        gen = delegator(*pa, **kwa)
        gen.send(None)
        return gen
    return inner


@send_delegator
def delegator(gen):
    result = yield from gen
    print(f"   Number     Square")
    for res in result:
        print(f"{res[0]:9d} {res[1]:10d}")


def generetor_squares():
    squares = []
    while True:
        try:
            num = yield
            for n in num:
                squares.append((n, n**2))
            print(f'Add number', end=' ')
            print(*num, sep=', ', end=' ')
            print('in array')
        except StopIteration:
            print('\nExit from generator!')
            break
    return squares


def event_loop():
    while True:
        x = input()
        match x:
            case "exit":
                try:
                    g.throw(StopIteration)
                except StopIteration:
                    break
            case x:
                try:
                    g.send(list(map(int, x.split())))
                except ValueError:
                    print("Please, enter numbers")


if __name__ == "__main__":
    g = delegator(generetor_squares())
    event_loop()
