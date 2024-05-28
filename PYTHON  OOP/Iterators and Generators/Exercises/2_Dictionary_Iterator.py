class dictionary_iter:
    def __init__(self, some_dict: dict):
        self.some_dict = some_dict
        self.list_ofTuples = [(k, v) for k, v in self.some_dict.items()]
        self.current_index = -1

    def __iter__(self):
        self.current_index = -1
        return self

    def __next__(self):
        if self.current_index == len(self.some_dict) - 1:
            raise StopIteration
        self.current_index += 1
        return self.list_ofTuples[self.current_index]


result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)

