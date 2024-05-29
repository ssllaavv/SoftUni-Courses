
def logged(function):
    def wrapper(*args):

        result = f"you called {function.__name__}{args}\n" \
                 f"it returned {function(*args)}"

        return result
    return wrapper


@logged
def sum_func(a, b):
    return a + b


print(sum_func(1, 4))



