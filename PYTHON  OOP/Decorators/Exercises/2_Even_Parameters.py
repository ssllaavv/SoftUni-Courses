def even_parameters(function):
    def wrapper(*args):
        if all(isinstance(p, int) and p % 2 == 0 for p in args):
            return function(*args)
        return 'Please use only even numbers!'
    return wrapper


@even_parameters
def multiply(*nums):
    result = 1
    for num in nums:
        result *= num
    return result


print(multiply(2, 4, 6, 8))
print(multiply(2, 4, 9, 8))

