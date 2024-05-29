class store_results:

    _log_file = "results.txt "

    def __init__(self, func):
        self.func = func

    def __call__(self, *args):
        log_string = f"Function '{self.func.__name__}' was called. Result: {self.func(*args)}"
        with open(self._log_file, "a") as file:
            file.write(log_string + "\n")
        return self.func(*args)


@store_results
def add(a, b):
    return a + b


@store_results
def mult(a, b):
    return a * b


add(2, 2)
mult(6, 4)
