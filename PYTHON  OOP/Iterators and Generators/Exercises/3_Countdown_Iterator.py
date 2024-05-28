
class countdown_iterator:
    def __init__(self, count: int):
        self.count = count
        self.current = count

    def __iter__(self):
        self.current = self.count
        return self

    def __next__(self):
        if self.current > -1:
            self.current -= 1
            return self.current + 1
        raise StopIteration


iterator = countdown_iterator(10)
for item in iterator:
    print(item, end=" ")


