def fibonacci():
    m = 0
    n = 1
    yield 0
    yield 1

    while True:
        l = n + m
        yield l
        m = n
        n = l


generator = fibonacci()
for i in range(7):
    print(next(generator))
