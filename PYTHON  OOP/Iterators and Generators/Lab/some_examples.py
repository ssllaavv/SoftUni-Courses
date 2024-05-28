# iterable = [1, 2, 3, 4, 5]
#
#
# iter_object = iter(iterable)
# while True:
#     try:
#         element = next(iter_object)
#         print(element)
#
#     except StopIteration:
#         break


# def first_n(num: int):
#     n = 0
#     while n <= num:
#         yield n
#         n += 1
#
#
# sum_first_n = sum(first_n(4))
# print(sum_first_n)


def my_gen():
    n = 1
    print('This is printed first')
    yield n

    n += 1
    print('This is printed second')
    yield n

    n += 1
    print('This is printed at last')
    yield n


print(list(my_gen()))



