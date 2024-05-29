
# def hello_function():
#     def say_hi():
#         return "Hi"
#     return say_hi
#
#
# hello = hello_function()
# print(hello())




# def print_message(message):
#     def message_sender():
#         "Nested Function"
#         print(message)
#     message_sender()
#
#
# print_message("Some random message")


from functools import wraps

# def uppercase_decorator(function):
#     @wraps(function)
#     def wrapper():
#         result = function()
#         uppercase_result = result.upper()
#         return uppercase_result
#
#     return wrapper

# from time import time
# import time as tm
#
#
# def measure_time(func):
#     def wrapper(*args, **kwargs):
#         start = time()
#         result = func(*args, **kwargs)
#         end = time()
#         print(end - start)
#         return result
#     return wrapper
#
#
# @measure_time
# def say_hi():
#     tm.sleep(5)
#     """Saying Hi"""
#     return "hello there"
#
#
# print(say_hi.__name__) # wrapper
# print(say_hi.__doc__)  # None
#
#
# print(say_hi())


def repeat(times):
    def decorator(function):
        def wrapper(*args, **kwargs):
            for _ in range(times):
                function(*args, **kwargs)
        return wrapper

    return decorator


@repeat(5)
def say_hi():
    print("Hello")


say_hi()
