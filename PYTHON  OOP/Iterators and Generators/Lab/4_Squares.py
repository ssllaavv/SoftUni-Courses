
def squares(num):

    # # 1
    # for n in range(1, num + 1):
    #     yield n * n

    # 2
    n = 1
    while n <= num:
        yield n * n
        n += 1


print(list(squares(5)))
