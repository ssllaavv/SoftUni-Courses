
class sequence_repeat:
    def __init__(self, sequence, num: int):
        self.sequence = sequence
        self.num = num
        self.counter = -1

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter != self.num - 1:
            self.counter += 1
            index = self.counter % len(self.sequence)
            return list(self.sequence)[index]
        raise StopIteration


result = sequence_repeat('abc', 5)
for item in result:
    print(item, end='')




